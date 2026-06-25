"""
Phase 0: Constitution

Define las reglas NO-NEGOTIABLES del proyecto:
- Stack tecnológico
- Requisitos de testing
- Políticas de seguridad
- Restricciones arquitectónicas
"""

from models.project import SDDProject


class ConstitutionPhase:
    """Fase 0: Establecer Constitution del proyecto"""

    CONSTITUTION_TEMPLATE = """# Project Constitution

## Technology Stack
- **Language:**
- **Framework:**
- **Database:**
- **Testing Framework:**

## Testing Requirements
- **Minimum Coverage:** 80%
- **Testing Strategy:** Unit + Integration
- **CI/CD Pipeline:**

## Security Policies
- **Password Hashing:** bcrypt (cost factor 12)
- **Session Management:** JWT tokens
- **Data Encryption:**

## Architectural Constraints
- **Code Organization:**
- **Dependency Management:**
- **API Style:** RESTful

## Coding Standards
- **Linter:**
- **Code Style:**
- **Type Checking:** Enabled
"""

    def __init__(self, project: SDDProject):
        self.project = project

    def run_interactive(self) -> None:
        """Guía interactivo para crear Constitution"""
        print("Voy a ayudarte a definir la CONSTITUTION de tu proyecto.")
        print("Esta es la 'DNA' de reglas inmutables que guiarán todo el desarrollo.\n")

        # Recolectar información
        print("1️⃣  TECHNOLOGY STACK")
        language = input("   ¿Lenguaje principal? (TypeScript/Python/Go/Rust): ").strip()
        framework = input("   ¿Framework principal? (Next.js/FastAPI/Gin/etc): ").strip()
        database = input("   ¿Base de datos? (PostgreSQL/MongoDB/etc): ").strip()

        print("\n2️⃣  TESTING & QUALITY")
        min_coverage = input("   ¿Cobertura mínima de tests? (default 80%): ").strip() or "80"
        testing_framework = input("   ¿Framework de testing? (jest/pytest/vitest/etc): ").strip()

        print("\n3️⃣  SECURITY POLICIES")
        password_hashing = input("   ¿Password hashing? (default: bcrypt cost 12): ").strip() or "bcrypt cost 12"
        session_mgmt = input("   ¿Session management? (default: JWT): ").strip() or "JWT"

        print("\n4️⃣  ARCHITECTURAL CONSTRAINTS")
        architecture = input("   ¿Patrón arquitectónico? (Clean/DDD/MVC/etc): ").strip()
        api_style = input("   ¿Estilo API? (default: RESTful): ").strip() or "RESTful"

        # Generar Constitution
        constitution_content = f"""# {self.project.metadata_dict.get('name', 'Project')} Constitution

## Technology Stack
- **Language:** {language}
- **Framework:** {framework}
- **Database:** {database}
- **Testing Framework:** {testing_framework}

## Testing Requirements
- **Minimum Coverage:** {min_coverage}%
- **Testing Strategy:** Unit + Integration + E2E
- **CI/CD Pipeline:** GitHub Actions

## Security Policies
- **Password Hashing:** {password_hashing}
- **Session Management:** {session_mgmt}
- **Token Expiration:** 24 hours
- **HTTPS Only:** Yes

## Architectural Constraints
- **Code Organization:** Modular by domain
- **Dependency Management:** Strict versioning
- **API Style:** {api_style}
- **Naming Conventions:** camelCase (code), snake_case (DB)

## Coding Standards
- **Linter:** Enabled + Pre-commit hooks
- **Code Style:** Consistent formatting
- **Type Checking:** Strict mode enabled
- **Documentation:** JSDoc/Docstrings for public APIs

## Non-Negotiable Rules
1. All code changes must have corresponding tests
2. No hardcoded secrets in source code
3. Database migrations must be reversible
4. API changes require contract documentation
5. All errors must be explicitly typed
"""

        # Guardar Constitution
        self.project.write_constitution(constitution_content)
        print("\n✅ Constitution creada y guardada en .specify/constitution.md\n")
        print(constitution_content)
