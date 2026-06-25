# SDD Skill: Spec-Driven Development Automation

Skill especializado para automatizar el workflow completo de **Spec-Driven Development (SDD)** en Claude Code.

## ¿Qué es SDD?

Spec-Driven Development es una metodología que trata las **especificaciones ejecutables como el artifact primario** del desarrollo de software. Los agentes IA generan código a partir de especificaciones precisas, no a la inversa.

Ref: [Documento de referencia SDD](../../../WORKSPACE/SDD/SUMMARY.md)

## Cómo Usar Este Skill

### Invocación Básica (Conversacional)

```
/sdd
"Quiero crear una API REST de gestión de tareas con TypeScript"
```

El skill te guiará a través de 6 fases:

1. **Constitution** - Reglas inmutables del proyecto
2. **Specify** - Especificación de funcionalidad (EARS syntax)
3. **Clarify** - Resolver ambigüedades
4. **Plan** - Plan técnico y contratos API
5. **Tasks** - Descomposición en tareas atómicas
6. **Implement** - Generación de código (multi-agent)
7. **Validate** - Verificación y testing

### Invocación por Fase

```
/sdd --phase plan
"Refina el plan técnico para la API de tareas"
```

El skill cargará el estado actual y te permitirá refinar esa fase específica.

### Validación

```
/sdd --validate
```

Valida que especificaciones cumplan EARS, que código respete contratos, etc.

## Fases del Workflow

### Phase 0: Constitution
Define las reglas NO-NEGOTIABLES del proyecto:
- Stack tecnológico (TypeScript, Python, Go, etc.)
- Requisitos de testing (coverage %, frameworks)
- Políticas de seguridad (hashing, encryption, etc.)
- Restricciones arquitectónicas
- Convenciones de código

**Salida:** `.specify/constitution.md`

### Phase 1: Specify
Describe QUÉ funcionalidad quieres, usando **EARS syntax**:

```
# EARS Patterns:

Ubiquitous: The [system] SHALL [response]
  → "The system SHALL hash passwords using bcrypt with cost factor 12"

Event-Driven: WHEN [trigger], THE system SHALL [response]
  → "WHEN a user submits a login form, THE system SHALL validate credentials"

State-Driven: WHILE [state], THE system SHALL [response]
  → "WHILE the system is in maintenance mode, THE system SHALL return HTTP 503"

Unwanted: IF [condition], THEN [response]
  → "IF password validation fails 3×, THEN lock account for 15 minutes"

Optional: WHERE [feature], THE system SHALL [response]
  → "WHERE SSO is enabled, THE system SHALL validate against SAML IdP"
```

**Salida:** `.specify/features/NNN-name/spec.md`

### Phase 2: Clarify
El skill detecta ambigüedades en tu especificación y te hace preguntas:
- "¿User creation date o update date para sorting?"
- "¿UTC siempre o timezone local?"
- "¿Email validation regex específico?"

**Salida:** `spec.md` refinado sin ambigüedades

### Phase 3: Plan
Define CÓMO implementarás la funcionalidad:
- Tech stack específico
- Schemas de base de datos
- Contracts API (OpenAPI YAML)
- State machines
- Security boundaries

**Salida:** `.specify/features/NNN-name/plan.md`

### Phase 4: Tasks
Descomposición en tareas atómicas:
```
## Task 1: Create password hashing utility
- Input: raw password string
- Output: bcrypt hash (cost 12)
- Files: src/utils/password.ts
- Test: src/utils/password.test.ts
- Success: All tests pass, no edge cases

## Task 2: Create User model
- Input: username, email, hashed_password
- Output: User entity in database
- Files: src/models/User.ts, migrations/001_create_users.sql
- Test: src/models/User.test.ts
- Success: CRUD operations validated
```

**Salida:** `.specify/features/NNN-name/tasks.md`

### Phase 5: Implement (Multi-Agent)

El skill orquesta **3 agentes** con roles adversariales:

```
COORDINATOR
  ├─→ Lee specification.md, plan.md, constitution.md
  ├─→ Asigna tareas a IMPLEMENTOR
  └─→ Supervisa a VERIFIER

IMPLEMENTOR
  ├─→ Recibe: task description + constraints
  ├─→ Genera: código TypeScript/Python/Go
  └─→ Entrega a VERIFIER

VERIFIER (Opposition Target)
  ├─→ Audita código contra constitution.md
  ├─→ Valida que respete spec
  ├─→ Busca edge cases no cubiertos
  └─→ Rechaza si hay violaciones
```

**Salida:** Código generado en `src/`

### Phase 6: Validate
Verificaciones automáticas:
- ✅ Tests pass (100% coverage según constitution)
- ✅ Código respeta contratos API (OpenAPI validation)
- ✅ Sin violaciones EARS en spec
- ✅ Static analysis (linting, type checking)
- ✅ Property-based testing (edge cases)

**Salida:** Reporte de validación + proyecto listo

## EARS Syntax Reference

| Patrón | Template | Ejemplo | Cuándo |
|--------|----------|---------|--------|
| **Ubiquitous** | The [system] SHALL [response] | "The system SHALL store passwords hashed" | Comportamientos universales, invariantes |
| **Event-Driven** | WHEN [trigger], THE system SHALL [response] | "WHEN user clicks submit, THE system SHALL validate form" | Reacciones a eventos |
| **State-Driven** | WHILE [state], THE system SHALL [response] | "WHILE offline, THE system SHALL queue requests" | Acciones durante estados específicos |
| **Unwanted Behavior** | IF [condition], THEN [response] | "IF validation fails 3×, THEN lock account" | Manejo de errores, edge cases |
| **Optional** | WHERE [condition], THE system SHALL [response] | "WHERE multi-lang enabled, THE system SHALL translate UI" | Features condicionales |

### Reglas EARS Estrictas
- ✅ USE: "SHALL" (nunca "should", "will", "must")
- ✅ USE: KEYWORDS en MAYÚSCULAS (WHEN, WHILE, WHERE, THE SYSTEM SHALL)
- ❌ BAN: Términos ambiguos ("timely", "efficient", "user-friendly", "properly")
- ✅ MAP: Cada línea EARS → 1 caso de test

## Estructura de Proyecto Generado

```
my-api/
├── .specify/                          # Artefactos SDD versionados
│   ├── constitution.md                # Reglas del proyecto
│   └── features/
│       └── 001-user-auth/
│           ├── spec.md                # Especificación EARS
│           ├── plan.md                # Plan técnico
│           └── tasks.md               # Descomposición
│
├── src/                               # Código generado
│   ├── models/
│   ├── controllers/
│   ├── services/
│   ├── utils/
│   └── __tests__/
│
├── migrations/                        # DB migrations
├── .github/                           # GitHub workflows
├── package.json / pyproject.toml / go.mod
└── README.md
```

## GitHub Integration

El skill puede opcionalmente:
- Crear repositorio en GitHub
- Sincronizar `.specify/` a repo automáticamente
- Crear Issues a partir de `tasks.md`
- Crear PRs con código generado
- Vincular commits a especificaciones

**Uso:**
```
/sdd --github
"Crea repo en GitHub para my-api"
```

## Iteración y Refinamiento

El modelo de SDD es iterativo. Puedes:

1. **Crear proyecto** → Constitution → Spec → Implement
2. **Refinar** → `/sdd --phase spec` y mejorar especificación
3. **Regenerar** downstream → plan.md y tasks.md se actualizan automáticamente
4. **Re-implement** → Código se regenera respetando nuevas specs

No pierdes trabajo: `.specify/` es versionado en git.

## Debugging y Validación Manual

Si el skill no funciona como esperas:

```
/sdd --validate
```

Esto te mostrará:
- ❌ Violaciones EARS en spec.md
- ❌ Inconsistencias entre spec y plan
- ❌ Tareas malformadas
- ❌ Contratos API rotos

## Limitaciones y Cuidados

1. **No abuses de ceremony:** Usa SDD Level 1 (Spec-First) para prototipos rápidos, Level 2 (Spec-Anchored) para producción
2. **Mantén specs simples:** No especifiques cada pixel o cada línea de lógica
3. **EARS requiere precisión:** Invertir tiempo en escribir especificaciones EARS buenas acelera todo lo demás
4. **Los agentes no son perfectos:** Siempre revisa código generado; el skill no reemplaza código review humano

## Troubleshooting

**"Error: spec.md tiene sintaxis EARS inválida"**
- Revisa que cada línea siga uno de los 5 patrones EARS
- Usa mayúsculas para WHEN, WHILE, WHERE, THE SYSTEM SHALL
- Elimina términos ambiguos

**"Error: plan.md no alinca con spec.md"**
- `/sdd --phase plan` y vuelve a refinar manualmente
- El skill detectará inconsistencias

**"Código generado no respeta constitution.md"**
- VERIFIER lo rechazará automáticamente
- Revisa que constitution.md esté correctamente especificado
- Intenta regenerar

## Licencia y Referencia

Este skill implementa metodología Spec-Driven Development basada en:
- Microsoft Spec-Driven Development guide (2025-2026)
- GitHub Spec Kit
- EARS syntax (requirements engineering)
- Design by Contract (Bertrand Meyer)

Documento de referencia: [SUMMARY.md](../../../WORKSPACE/SDD/SUMMARY.md)
