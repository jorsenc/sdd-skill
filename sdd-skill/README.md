# SDD Skill - Spec-Driven Development para Claude Code

## 🚀 Inicio Rápido

### Instalación
El skill está listo en `~/.claude/skills/sdd/`

### Uso Básico

**Crear un nuevo proyecto SDD:**
```
/sdd
"Quiero crear una API REST de tareas con TypeScript"
```

El skill te guiará a través de:
1. **Constitution** - Reglas del proyecto
2. **Specify** - Especificación EARS
3. **Clarify** - Resolver ambigüedades
4. **Plan** - Plan técnico
5. **Tasks** - Descomposición
6. **Implement** - Generar código
7. **Validate** - Verificar calidad

### Refinamiento Parcial

Si quieres refinar solo una fase:
```
/sdd --phase plan
"Cambia el stack a Python en lugar de TypeScript"
```

### Validación

Valida especificaciones sin hacer cambios:
```
/sdd --validate
```

---

## 📋 Estructura del Skill

```
~/.claude/skills/sdd/
├── SKILL.md              # Documentación completa
├── main.py               # Orquestador principal
├── README.md             # Este archivo
├── validators/
│   ├── ears_validator.py # Validador EARS
│   └── __init__.py
├── phases/
│   ├── constitution.py   # Phase 0
│   ├── specify.py        # Phase 1
│   ├── clarify.py        # Phase 2
│   ├── plan.py           # Phase 3
│   ├── tasks.py          # Phase 4
│   ├── implement.py      # Phase 5
│   ├── validate.py       # Phase 6
│   └── __init__.py
├── models/
│   ├── project.py        # Modelo SDDProject
│   ├── specification.py  # Modelo Specification
│   └── __init__.py
├── integrations/
│   ├── github.py         # GitHub Integration
│   ├── local_repo.py     # Git Management
│   └── __init__.py
└── templates/
    ├── constitution.md
    ├── spec.md
    └── plan.md
```

---

## 📚 EARS Syntax Quick Reference

| Patrón | Sintaxis | Ejemplo |
|--------|----------|---------|
| **Ubiquitous** | `The system SHALL [response]` | "The system SHALL hash passwords using bcrypt cost 12" |
| **Event-Driven** | `WHEN [trigger], THE system SHALL [response]` | "WHEN user clicks submit, THE system SHALL validate email" |
| **State-Driven** | `WHILE [state], THE system SHALL [response]` | "WHILE user offline, THE system SHALL queue requests" |
| **Unwanted** | `IF [condition], THEN [response]` | "IF login fails 3×, THEN lock account 15 min" |
| **Optional** | `WHERE [feature], THE system SHALL [response]` | "WHERE SSO enabled, THE system SHALL use SAML" |

**⚠️ Reglas Estrictas:**
- ✅ Use "SHALL" (never "should", "must", "will")
- ✅ UPPERCASE keywords: WHEN, WHILE, WHERE, THE SYSTEM SHALL
- ❌ Ban ambiguous terms: "timely", "efficient", "user-friendly"
- ✅ Be specific: "bcrypt cost 12" not "securely hash"

---

## 🔄 Workflow Example

```
Usuario: /sdd "Crearé un API de pagos"

Skill: Phase 0: CONSTITUTION
  - Lenguaje? TypeScript
  - Framework? Express.js
  - Database? PostgreSQL
  → Guardado en .specify/constitution.md

Skill: Phase 1: SPECIFY (EARS)
  Usuario escribe:
    The system SHALL store card tokens encrypted with AES-256
    WHEN user submits payment, THE system SHALL validate with Stripe
    IF card declined, THEN return HTTP 402
  → Guardado en .specify/features/001-main/spec.md

Skill: Phase 2: CLARIFY
  Encontré ambigüedades:
    1. ¿Guardar tokens en DB o solo Stripe?
    2. ¿Reintentar fallido payment? ¿Cuántas veces?
  Usuario responde...

Skill: Phase 3: PLAN
  Tech: Express + PostgreSQL + Stripe API
  Schemas: users, payments, card_tokens tables
  API Contracts: POST /payments, GET /payments/{id}
  → Guardado en .specify/features/001-main/plan.md

Skill: Phase 4: TASKS
  Task 1: Create card tokenization utility
  Task 2: Create Payment model
  Task 3: Create payment endpoint
  → Guardado en .specify/features/001-main/tasks.md

Skill: Phase 5: IMPLEMENT
  COORDINATOR orquesta:
    IMPLEMENTOR: genera código
    VERIFIER: audita contra spec
  ✅ Code generation complete
  → src/ con código listo

Skill: Phase 6: VALIDATE
  ✅ Tests pass (100% coverage)
  ✅ Code respects API contracts
  ✅ No EARS violations
  → Proyecto listo
```

---

## 🛠️ Development Status

**MVP v0.1 (Current):**
- ✅ Structure & scaffolding
- ✅ EARS validator
- ✅ Phase 0: Constitution
- ✅ Phase 1: Specify (basic)
- 🚧 Phase 2-6: Stub implementations
- 🚧 GitHub integration
- 🚧 Multi-agent orchestration

**Next (v0.2):**
- Full Phase 2-6 implementations
- Claude API integration for code gen
- GitHub repo creation & issue sync
- Multi-agent Coordinator/Implementor/Verifier
- Property-based testing support

---

## 📖 Full Documentation

See [SKILL.md](./SKILL.md) for complete documentation, including:
- All 7 phases in detail
- EARS syntax complete reference with examples
- GitHub integration guide
- Troubleshooting
- Architecture decisions

---

## 🔗 References

- **SDD Methodology:** See `~/WORKSPACE/SDD/SUMMARY.md`
- **EARS Syntax:** Requirements engineering standard from aerospace/medical
- **Design by Contract:** Bertrand Meyer (1986)
- **Transaction Cost Economics:** Oliver Williamson framework

---

## 💡 Tips

1. **Invest in Constitution early** - This becomes the guardrails for AI generation
2. **EARS syntax matters** - Each requirement maps 1:1 to a test case
3. **Iterate specs, not code** - Changing spec regenerates plan/tasks/code
4. **Use git for .specify/** - Version your specifications alongside code
5. **Start small** - Use Level 1 (Spec-First) for prototypes, Level 2 (Spec-Anchored) for production

---

## 🐛 Troubleshooting

**"ModuleNotFoundError":**
```bash
cd ~/.claude/skills/sdd/
python main.py
```

**"EARS validation failed":**
- Check each line matches one of 5 EARS patterns
- Use UPPERCASE for keywords (WHEN, WHILE, WHERE, THE SYSTEM SHALL)
- Avoid ambiguous terms

**"GitHub integration not working":**
- Requires GitHub token in environment: `GITHUB_TOKEN=...`
- Currently in development - use manually for now

---

## 📧 Contact & Support

- Documentación completa: [SKILL.md](./SKILL.md)
- Referencia SDD: `~/WORKSPACE/SDD/SUMMARY.md`
- Issues/Bugs: Report in Claude session

---

**Made with ❤️ for Spec-Driven Development in Claude Code**
