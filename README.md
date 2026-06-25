# 🚀 SDD Skill - Spec-Driven Development para Claude Code

Una herramienta completa para automatizar **Spec-Driven Development** en Claude Code con especificaciones ejecutables EARS.

**Status:** ✅ MVP v0.1 | **GitHub:** https://github.com/jorsenc/sdd-skill | **License:** MIT

---

## 📖 Documentación Rápida

### 👤 Empezar (Elige tu ruta)

| Si eres... | Lee primero | Tiempo |
|-----------|------------|--------|
| **Usuario nuevo** | [🎯 Quick Start](#quick-start) | 5 min |
| **Desarrollador** | [👨‍💻 Para Desarrolladores](#para-desarrolladores) | 10 min |
| **Queriendo aprender SDD** | [📚 SDD Methodology](./docs/SDD_METHODOLOGY.md) | 30 min |

---

## 🎯 Quick Start

### Instalación
```bash
cd sdd-skill
pip install -r requirements.txt
python main.py
```

### Desde Claude Code
```
/sdd
"Voy a crear una API REST con TypeScript"
```

El skill te guía a través de:
1. **Constitution** - Reglas del proyecto
2. **Specification** - Requisitos EARS
3. **Clarify** → **Plan** → **Tasks** → **Implement** → **Validate** (v0.2+)

### Ejemplo Real
Ver [sdd-skill/examples/simple_api.md](./sdd-skill/examples/simple_api.md) - Tutorial completo (Todo API)

---

## 📚 Documentación Principal

### 🎯 Skill SDD (Cómo Usar)

**[sdd-skill/SKILL.md](./sdd-skill/SKILL.md)** (28 KB) - **Documentación completa**
- ¿Qué es SDD?
- Las 7 fases explicadas
- EARS syntax con 5 patrones y ejemplos
- CLI comandos y opciones
- Troubleshooting y FAQs

**[sdd-skill/README.md](./sdd-skill/README.md)** (3 KB) - **Quick reference**
- Instalación rápida
- Comandos disponibles
- Estructura del skill

---

### 👨‍💻 Para Desarrolladores

**[CONTRIBUTING.md](./CONTRIBUTING.md)** - Cómo contribuir
- Áreas prioritarias (Phases 2-6, integrations)
- Workflow de contribución
- Estándares de código Python
- Checklist para PRs

**[CHANGELOG.md](./CHANGELOG.md)** - Historial y roadmap
- v0.1 (actual) - Phases 0-1, EARS validator
- v0.2 (próximo) - Phases 2-6, GitHub integration
- v1.0 (target) - Workflow completo

---

### 📚 Aprender SDD

**[docs/Desarrollo Guiado por Especificaciones.md](./docs/Desarrollo%20Guiado%20por%20Especificaciones.md)** - Documento completo en Markdown (68KB)
- Investigación académica completa
- SDD theory y foundations
- Maturity levels y workflows
- EARS syntax reference
- Multi-agent patterns y case studies
- Enterprise adoption strategies

**[docs/SDD_METHODOLOGY.md](./docs/SDD_METHODOLOGY.md)** - Resumen condensado
- Historia de SDD
- Transaction Cost Economics (base teórica)
- Design by Contract
- EARS syntax reference
- Casos de uso empresariales

**[docs/Desarrollo Guiado por Especificaciones.docx](./docs/)** - Documento original (Word)

---

## 📁 Estructura del Proyecto

```
sdd-skill/
├── 🎯 main.py                  # Entry point - CLI orchestrator
├── SKILL.md                    # Documentación principal ⭐
├── README.md                   # Quick start
├── requirements.txt            # Dependencias Python
│
├── validators/
│   └── ears_validator.py       # Validador EARS (5 patrones)
│
├── phases/
│   ├── constitution.py         # Phase 0 ✅
│   ├── specify.py              # Phase 1 ✅
│   └── {clarify,plan,tasks,implement,validate}.py  # Phases 2-6 🚧
│
├── models/
│   ├── project.py              # Proyecto SDD
│   └── specification.py        # Especificación EARS
│
├── integrations/
│   ├── github.py               # GitHub API (v0.2)
│   └── local_repo.py           # Git management
│
├── templates/
│   ├── constitution.md
│   ├── spec.md
│   └── plan.md
│
└── examples/
    └── simple_api.md           # Ejemplo completo
```

---

## 🎓 EARS Syntax (Referencia Rápida)

| Patrón | Template | Ejemplo |
|--------|----------|---------|
| **Ubiquitous** | `The system SHALL [response]` | "The system SHALL hash passwords using bcrypt" |
| **Event-Driven** | `WHEN [trigger], THE system SHALL [response]` | "WHEN user submits, THE system SHALL validate" |
| **State-Driven** | `WHILE [state], THE system SHALL [response]` | "WHILE offline, THE system SHALL queue requests" |
| **Unwanted** | `IF [condition], THEN [response]` | "IF login fails 3×, THEN lock account" |
| **Optional** | `WHERE [feature], THE system SHALL [response]` | "WHERE SSO enabled, THE system SHALL use SAML" |

**Reglas:** Use "SHALL" (never should/must) • UPPERCASE keywords • Ban ambiguous terms • Be specific

**Más:** [sdd-skill/SKILL.md](./sdd-skill/SKILL.md)

---

## ✨ Estado Actual (v0.1)

### ✅ Funcionando
- EARS Validator (5 patrones, ambiguous term detection)
- Phase 0: Constitution (complete)
- Phase 1: Specify (complete)
- CLI orchestrator (4 modes)
- Documentación profesional

### 🚧 Framework Ready (v0.2)
- Phases 2-6 (structure ready, logic pending)
- GitHub integration
- Claude API code generation
- Multi-agent orchestration

---

## 🔗 Links Importantes

| Recurso | Link |
|---------|------|
| **GitHub Repo** | https://github.com/jorsenc/sdd-skill |
| **Skill Guide** | [sdd-skill/SKILL.md](./sdd-skill/SKILL.md) |
| **Contributing** | [CONTRIBUTING.md](./CONTRIBUTING.md) |
| **Example Project** | [sdd-skill/examples/simple_api.md](./sdd-skill/examples/simple_api.md) |
| **Version History** | [CHANGELOG.md](./CHANGELOG.md) |
| **SDD Theory** | [docs/SDD_METHODOLOGY.md](./docs/SDD_METHODOLOGY.md) |

---

## 🚀 Próximos Pasos

### Para Usuarios
1. Leer [sdd-skill/SKILL.md](./sdd-skill/SKILL.md) (15 min)
2. Ejecutar `python sdd-skill/main.py` (5 min)
3. Ver [sdd-skill/examples/simple_api.md](./sdd-skill/examples/simple_api.md) (20 min)

### Para Desarrolladores
1. Fork en GitHub: https://github.com/jorsenc/sdd-skill
2. Leer [CONTRIBUTING.md](./CONTRIBUTING.md)
3. Elegir tarea en [CHANGELOG.md](./CHANGELOG.md) (v0.2)
4. Hacer PR

---

## 📊 Estadísticas

| Métrica | Valor |
|---------|-------|
| **Código Python** | ~1,500 LOC |
| **Documentación** | 50+ KB |
| **Archivos** | 25+ |
| **Fases Funcionales** | 2/7 (Phases 0-1) ✅ |
| **EARS Patrones** | 5/5 ✅ |

---

## ❓ Preguntas Frecuentes

**¿Funciona ya?**  
Phases 0-1 ✅, Phases 2-6 🚧 (framework listo para v0.2)

**¿Cómo instalar?**  
```bash
cd sdd-skill && pip install -r requirements.txt
```

**¿Cómo usar?**  
```bash
python main.py  # o /sdd desde Claude Code
```

**¿Cómo contribuir?**  
Ver [CONTRIBUTING.md](./CONTRIBUTING.md)

**¿Dónde reportar bugs?**  
GitHub Issues: https://github.com/jorsenc/sdd-skill/issues

---

## 📄 Archivos en Este Repositorio

| Archivo | Descripción |
|---------|-------------|
| **README.md** | Este archivo (índice principal) |
| **CONTRIBUTING.md** | Guía para contribuidores |
| **CHANGELOG.md** | Historial de versiones y roadmap |
| **LICENSE** | MIT License (open source) |
| **.gitignore** | Configuración Git |
| **docs/** | Documentación de referencia |
| **sdd-skill/** | 🎯 Skill principal |

---

## 🎯 Misión

Automatizar **Spec-Driven Development** en Claude Code para:
- ✅ Eliminar ambigüedad en requisitos
- ✅ Crear especificaciones ejecutables
- ✅ Reducir revisiones de código
- ✅ Mejorar la calidad del software
- ✅ Escalar desarrollo con IA

---

## 🔄 Basado En

- **Microsoft Spec-Driven Development** (2025-2026)
- **GitHub Spec Kit**
- **EARS Syntax** (Requirements Engineering)
- **Design by Contract** (Bertrand Meyer)
- **Transaction Cost Economics** (Oliver Williamson)

---

## 📞 Contacto

- **GitHub:** https://github.com/jorsenc/sdd-skill
- **Issues:** Crear issue en GitHub para bugs/features
- **Discussions:** GitHub discussions para preguntas

---

**¡Empieza ahora!** 👉 [sdd-skill/SKILL.md](./sdd-skill/SKILL.md)

---

*Spec-Driven Development Skill v0.1 • MIT License • Open Source*
