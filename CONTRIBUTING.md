# Contributing to SDD Skill

¡Gracias por tu interés en contribuir al skill SDD para Claude Code! Este documento explica cómo puedes ayudar.

## 🎯 Áreas Prioritarias para Contribuciones

### 1. **Implementación de Phases 2-6** (Alta Prioridad)
- **Phase 2: Clarify** - Detectar y resolver ambigüedades automáticamente
- **Phase 3: Plan** - Generar OpenAPI/AsyncAPI specs desde requirement
- **Phase 4: Tasks** - Descomponer plan en tareas atómicas
- **Phase 5: Implement** - Multi-agent code generation (Coordinator/Implementor/Verifier)
- **Phase 6: Validate** - Automatizar tests, coverage, EARS compliance

**Ubicación:** `sdd-skill/phases/`

### 2. **GitHub Integration** (Media Prioridad)
- Repository creation
- Issue creation from tasks.md
- PR generation with code
- Branch management

**Ubicación:** `sdd-skill/integrations/github.py`

### 3. **Claude API Integration** (Media Prioridad)
- Code generation using Claude API
- Streaming responses
- Token counting and optimization
- Model selection (Sonnet/Opus)

**Ubicación:** `sdd-skill/integrations/claude_api.py` (nuevo)

### 4. **Multi-Agent Orchestration** (Avanzado)
Implementar los 3 agentes:
- **Coordinator** - Leer specs, asignar tareas, supervisar
- **Implementor** - Generar código según task
- **Verifier** - Validar código contra constitution

**Ubicación:** `sdd-skill/agents/` (nuevo)

### 5. **Testing** (Media Prioridad)
- Unit tests para todos los modules
- Integration tests para workflow completo
- Edge case tests

**Ubicación:** `tests/`

### 6. **Documentation** (Baja Prioridad)
- Más ejemplos
- Troubleshooting guide
- Video tutorials
- Blog posts

## 🚀 Cómo Contribuir

### 1. Fork el Repositorio
```bash
git clone https://github.com/tu-usuario/sdd-skill.git
cd sdd-skill
git checkout -b feature/mi-feature
```

### 2. Instalar Dependencias
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r sdd-skill/requirements.txt
```

### 3. Implementar tu Cambio

**Nombra tu rama descriptivamente:**
- `feature/phase-2-clarify` para nuevas features
- `fix/ears-validator-bug` para fixes
- `docs/add-examples` para documentación

### 4. Escribir Tests

```python
# tests/test_ears_validator.py
import pytest
from sdd_skill.validators.ears_validator import EARSValidator

def test_ubiquitous_pattern():
    validator = EARSValidator()
    spec = "The system SHALL hash passwords using bcrypt"
    result = validator.validate(spec)
    assert result['valid'] == True
```

**Correr tests:**
```bash
pytest tests/ -v
```

### 5. Commit y Push

```bash
git add .
git commit -m "Add Phase 2: Clarify implementation

- Detect ambiguous terms automatically
- Ask clarification questions
- Update spec.md with resolved requirements
- Tests for clarification logic

Fixes #123"

git push origin feature/mi-feature
```

**Mensaje de commit:** 
- Línea 1: Resumen breve (50 chars)
- Línea en blanco
- Líneas adicionales: Contexto y detalles
- Referencia a issues: `Fixes #123`

### 6. Crear Pull Request

En GitHub:
1. Crea PR desde tu fork a `jorsenc/sdd-skill:master`
2. Llena el template (descripción, testing, screenshots)
3. Espera review

## 📋 Checklist para PRs

- [ ] ✅ Tests nuevos/modificados pasan
- [ ] ✅ Cobertura de código >= 80%
- [ ] ✅ Documentación actualizada (docstrings, README)
- [ ] ✅ Changelog updated
- [ ] ✅ No breaking changes (o documentados)
- [ ] ✅ Commits bien mensajeados

## 🐛 Reportar Issues

### Formato para Bugs

```markdown
## Descripción
(Describe el bug de forma clara)

## Steps to Reproduce
1. ...
2. ...
3. ...

## Comportamiento Actual
(Lo que pasó)

## Comportamiento Esperado
(Lo que debería pasar)

## Información Adicional
- Python version: 3.11
- OS: Windows 11
- Phase: Specify
```

### Formato para Features

```markdown
## Descripción
(Describe la feature)

## Motivación
(Por qué la necesitas)

## Propuesta
(Cómo debería funcionar)

## Alternativas Consideradas
(Otros enfoques)
```

## 📚 Estándares de Código

### Python Style
- Seguir **PEP 8**
- Usar **type hints** (`def foo(x: str) -> int:`)
- **Docstrings** en format Google

```python
def validate_ears(spec_content: str) -> Dict[str, Any]:
    """Valida especificación contra patrones EARS.
    
    Args:
        spec_content: Contenido del archivo spec.md
        
    Returns:
        Dict con resultado de validación y errores
        
    Raises:
        ValueError: Si spec_content está vacío
    """
    if not spec_content:
        raise ValueError("spec_content cannot be empty")
    # ...
```

### Commits
- Commits pequeños y focalizados
- Mensajes claros y descriptivos
- 1 feature/fix por commit (cuando sea posible)

### Branches
- `feature/` - Nuevas features
- `fix/` - Fixes de bugs
- `docs/` - Documentación
- `refactor/` - Refactorings
- `test/` - Tests

## 🎓 Aprendiendo el Código

### Estructura Principal
1. **main.py** - Entry point, CLI orchestrator
2. **validators/** - EARS validator
3. **phases/** - Implementación de 7 fases
4. **models/** - Data models (Project, Specification)
5. **integrations/** - GitHub, Git, Claude API

### Diagrama de Flujo
```
main.py (CLI)
  ├─→ ConstitutionPhase (Phase 0)
  ├─→ SpecifyPhase (Phase 1)
  ├─→ ClarifyPhase (Phase 2)
  ├─→ PlanPhase (Phase 3)
  ├─→ TasksPhase (Phase 4)
  ├─→ ImplementPhase (Phase 5)
  └─→ ValidatePhase (Phase 6)

EARSValidator
  ├─→ _matches_ears_pattern()
  ├─→ _check_ambiguous_terms()
  └─→ _validate_keyword_capitalization()

SDDProject
  ├─→ read_constitution()
  ├─→ write_specification()
  └─→ save_state()
```

## 🔄 Workflow de Review

1. **Submission** - PR creado con descripción
2. **Automated checks** - Tests, linting, type checking
3. **Code Review** - Mantainers revisan cambios
4. **Suggestions** - Si necesita ajustes
5. **Approval** - Cuando está listo
6. **Merge** - Se integra a master

## ⚡ Mejoras Rápidas (Good for First Contributions)

Si recién empiezas, estos son buenos primeros cambios:

- [ ] Añadir más ejemplos en `examples/`
- [ ] Mejorar docstrings
- [ ] Arreglar typos/ortografía
- [ ] Añadir more EARS examples
- [ ] Mejorar error messages
- [ ] Actualizar README con tips nuevos

## 📖 Recursos

- [Python Coding Standards](https://pep8.org/)
- [Git Best Practices](https://git-scm.com/docs/gittutorial)
- [SDD Documentation](./sdd-skill/SKILL.md)
- [EARS Syntax Reference](./sdd-skill/SKILL.md#ears-syntax-reference)

## 💬 Preguntas?

- Abre un **Discussion** en GitHub
- Comenta en el **Issue** relacionado
- Lee [SKILL.md](./sdd-skill/SKILL.md) para documentación

## 🙏 Gracias

¡Gracias por contribuir a hacer SDD Skill mejor para todos! 🎉

---

**Recordatorio:** Al contribuir, aceptas que tu código sea usado bajo la licencia del proyecto.
