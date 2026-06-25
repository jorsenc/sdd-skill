"""
EARS (Easy Approach to Requirements Syntax) Validator

Valida que especificaciones cumplan con patrones EARS estrictos:
- Ubiquitous: The [system] SHALL [response]
- Event-Driven: WHEN [trigger], THE system SHALL [response]
- State-Driven: WHILE [state], THE system SHALL [response]
- Unwanted: IF [condition], THEN [response]
- Optional: WHERE [condition], THE system SHALL [response]

Ref: Microsoft/GitHub Spec-Driven Development Guide (2025-2026)
"""

import re
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass


@dataclass
class EARSViolation:
    """Representa una violación de EARS syntax"""
    line_number: int
    line_text: str
    violation_type: str
    message: str


class EARSValidator:
    """Validador de sintaxis EARS para especificaciones"""

    # Patrones EARS validos
    EARS_PATTERNS = {
        'ubiquitous': r'^The system SHALL .+$',
        'event_driven': r'^WHEN .+, THE system SHALL .+$',
        'state_driven': r'^WHILE .+, THE system SHALL .+$',
        'unwanted': r'^IF .+, THEN .+$',
        'optional': r'^WHERE .+, THE system SHALL .+$',
    }

    # Términos ambiguos que NO están permitidos
    AMBIGUOUS_TERMS = {
        'timely': 'Usa timeouts específicos en lugar de "timely"',
        'efficient': 'Especifica métricas concretas en lugar de "efficient"',
        'user-friendly': 'Describe comportamiento específico en lugar de "user-friendly"',
        'properly': 'Sé específico sobre qué significa "properly"',
        'appropriate': 'Define criterios objetivos en lugar de "appropriate"',
        'various': 'Enumera casos específicos en lugar de "various"',
        'should': 'Usa "SHALL" en lugar de "should"',
        'must': 'Usa "SHALL" en lugar de "must"',
        'will': 'Usa "SHALL" en lugar de "will"',
        'might': 'Usa "SHALL" o describe condición específica',
    }

    def __init__(self):
        self.violations: List[EARSViolation] = []

    def validate(self, spec_content: str) -> Dict[str, Any]:
        """
        Valida especificación completa

        Args:
            spec_content: Contenido del archivo spec.md

        Returns:
            Dict con resultado de validación y lista de errores
        """
        self.violations = []
        lines = spec_content.split('\n')

        for line_num, line in enumerate(lines, 1):
            # Skip empty lines and headers
            if not line.strip() or line.startswith('#'):
                continue

            # Check if line matches any EARS pattern
            if not self._matches_ears_pattern(line):
                self._add_violation(
                    line_num,
                    line,
                    'INVALID_PATTERN',
                    f'No cumple con patrón EARS. Esperado uno de: '
                    f'Ubiquitous, Event-Driven, State-Driven, Unwanted, Optional'
                )

            # Check for ambiguous terms
            ambiguous_found = self._check_ambiguous_terms(line)
            for term, suggestion in ambiguous_found:
                self._add_violation(
                    line_num,
                    line,
                    'AMBIGUOUS_TERM',
                    f'Término ambiguo "{term}": {suggestion}'
                )

            # Check for uppercase keywords
            if self._contains_ears_keywords(line):
                self._validate_keyword_capitalization(line_num, line)

            # Check for prohibited modal verbs
            if self._contains_prohibited_modal(line):
                self._add_violation(
                    line_num,
                    line,
                    'WRONG_MODAL_VERB',
                    'Usa "SHALL" en lugar de "should", "must", "will"'
                )

        # Return result
        return {
            'valid': len(self.violations) == 0,
            'total_lines': len([l for l in lines if l.strip() and not l.startswith('#')]),
            'violations_count': len(self.violations),
            'violations': [
                {
                    'line': v.line_number,
                    'type': v.violation_type,
                    'message': v.message,
                    'text': v.line_text[:80] + ('...' if len(v.line_text) > 80 else '')
                }
                for v in self.violations
            ],
            'errors': [f"Line {v.line_number}: {v.message}" for v in self.violations]
        }

    def _matches_ears_pattern(self, line: str) -> bool:
        """Verifica si la línea cumple algún patrón EARS"""
        line = line.strip()

        # Allow comment lines
        if line.startswith('-') or line.startswith('*'):
            return True

        # Check each pattern
        for pattern in self.EARS_PATTERNS.values():
            if re.match(pattern, line):
                return True

        return False

    def _check_ambiguous_terms(self, line: str) -> List[Tuple[str, str]]:
        """Busca términos ambiguos en la línea"""
        found = []
        line_lower = line.lower()

        for term, suggestion in self.AMBIGUOUS_TERMS.items():
            if re.search(r'\b' + term + r'\b', line_lower):
                found.append((term, suggestion))

        return found

    def _contains_ears_keywords(self, line: str) -> bool:
        """Verifica si la línea contiene keywords EARS"""
        keywords = ['WHEN', 'WHILE', 'WHERE', 'THE', 'SYSTEM', 'SHALL', 'IF', 'THEN']
        return any(kw in line for kw in keywords)

    def _validate_keyword_capitalization(self, line_num: int, line: str) -> None:
        """Valida que keywords EARS estén en mayúsculas"""
        keywords = ['when', 'while', 'where', 'the', 'system', 'shall', 'if', 'then']

        for kw in keywords:
            # Check for lowercase versions
            if re.search(r'\b' + kw + r'\b', line, re.IGNORECASE):
                match = re.search(r'\b' + kw + r'\b', line)
                if match and match.group(0) != kw.upper():
                    self._add_violation(
                        line_num,
                        line,
                        'LOWERCASE_KEYWORD',
                        f'Keyword "{kw.upper()}" debe estar en mayúsculas'
                    )

    def _contains_prohibited_modal(self, line: str) -> bool:
        """Verifica uso de verbos modales prohibidos"""
        prohibited = ['should', 'must', 'will', 'might']
        line_lower = line.lower()

        for modal in prohibited:
            if re.search(r'\b' + modal + r'\b', line_lower):
                return True

        return False

    def _add_violation(self, line_num: int, line: str, violation_type: str, message: str) -> None:
        """Agrega una violación a la lista"""
        self.violations.append(EARSViolation(
            line_number=line_num,
            line_text=line,
            violation_type=violation_type,
            message=message
        ))

    @staticmethod
    def get_ears_help() -> str:
        """Retorna texto de ayuda para EARS syntax"""
        return """
╔═══════════════════════════════════════════════════════════════╗
║               EARS SYNTAX GUIDE - Spec-Driven Development     ║
╚═══════════════════════════════════════════════════════════════╝

PATRÓN 1: UBIQUITOUS (Invariantes Universales)
──────────────────────────────────────────────
Syntax: The system SHALL [response]
Uso: Comportamientos que siempre ocurren, sin gatillos externos

✅ CORRECTO:
   The system SHALL hash passwords using bcrypt with cost factor 12
   The system SHALL validate email format using RFC 5322 regex
   The system SHALL store all timestamps in UTC

❌ INCORRECTO:
   The system should hash passwords
   The system will validate emails
   The system SHALL hash passwords efficiently


PATRÓN 2: EVENT-DRIVEN (Reacciones a Eventos)
──────────────────────────────────────────────
Syntax: WHEN [trigger], THE system SHALL [response]
Uso: Comportamientos reactivos a eventos externos

✅ CORRECTO:
   WHEN a user submits the login form, THE system SHALL validate credentials against bcrypt
   WHEN a payment webhook is received, THE system SHALL verify HMAC signature
   WHEN the API receives a DELETE request, THE system SHALL soft-delete the resource

❌ INCORRECTO:
   When user logs in, the system validates
   WHEN user logs in THE system SHALL validate
   WHEN user logs in, the system should validate


PATRÓN 3: STATE-DRIVEN (Acciones Continuas en Estados)
───────────────────────────────────────────────────────
Syntax: WHILE [state], THE system SHALL [response]
Uso: Comportamientos durante estados específicos

✅ CORRECTO:
   WHILE the system is in maintenance mode, THE system SHALL return HTTP 503
   WHILE the user session is inactive for 15 minutes, THE system SHALL log out
   WHILE the database is offline, THE system SHALL queue requests in memory

❌ INCORRECTO:
   When system is down, it returns 503
   WHILE system down THE system SHALL return 503
   If system in maintenance, returns 503


PATRÓN 4: UNWANTED BEHAVIOR (Manejo de Errores)
────────────────────────────────────────────────
Syntax: IF [condition], THEN [response]
Uso: Respuestas a errores, edge cases, condiciones peligrosas

✅ CORRECTO:
   IF password validation fails 3×, THEN lock the account for 15 minutes
   IF input exceeds 1000 characters, THEN reject request with HTTP 400
   IF user attempts unauthorized access, THEN log incident and notify admin

❌ INCORRECTO:
   If validation fails, error occurs
   IF validation fails THE system SHALL lock
   When validation fails 3 times, lock account


PATRÓN 5: OPTIONAL/CONDITIONAL (Features Condicionales)
───────────────────────────────────────────────────────
Syntax: WHERE [feature active], THE system SHALL [response]
Uso: Comportamientos que dependen de configuración/permisos

✅ CORRECTO:
   WHERE the enterprise SSO module is enabled, THE system SHALL validate tokens against SAML IdP
   WHERE multi-language support is active, THE system SHALL translate UI to user's locale
   WHERE rate limiting is configured, THE system SHALL reject requests exceeding 100/minute

❌ INCORRECTO:
   If SSO enabled, validate against SAML
   WHERE SSO enabled the system validates
   When SSO is on, SAML validation happens


╔═══════════════════════════════════════════════════════════════╗
║                      REGLAS ESTRICTAS                         ║
╚═══════════════════════════════════════════════════════════════╝

✅ DO:
  • Usa "SHALL" exclusivamente (nunca "should", "must", "will", "might")
  • Usa MAYÚSCULAS para keywords: WHEN, WHILE, WHERE, THE SYSTEM SHALL, IF, THEN
  • Sé específico: "bcrypt cost factor 12" no "securely hash"
  • Incluye métricas: "15 minutes" no "timely", "100/min" no "efficiently"
  • Uno-a-uno con tests: Cada línea EARS → 1 caso de test

❌ DON'T:
  • Términos ambiguos: "timely", "efficient", "user-friendly", "properly", "appropriate", "various"
  • Verbos modales alternativos: "should", "must", "will", "might"
  • Características complejas: "Implementa autenticación" (demasiado amplio)
  • Especificaciones negativas: "El sistema no hará X" (describe qué hace, no qué no)


╔═══════════════════════════════════════════════════════════════╗
║                    EJEMPLOS DE SPEC BUENA                    ║
╚═══════════════════════════════════════════════════════════════╝

# User Authentication Specification

The system SHALL hash passwords using bcrypt with cost factor 12.
The system SHALL store hashed passwords in the users.password_hash column.

WHEN a user submits the login form, THE system SHALL:
  1. Validate that email field is non-empty
  2. Query users table by email
  3. Compare submitted password against stored hash using bcrypt.compare()
  4. Return JWT token if match, HTTP 401 if mismatch

WHILE a user session is active, THE system SHALL maintain JWT in memory.

WHILE the user is inactive for 15 minutes, THE system SHALL invalidate JWT.

IF login attempt fails 3 consecutive times, THEN lock account for 15 minutes.

IF JWT token is expired, THEN return HTTP 401 Unauthorized.

WHERE multi-factor authentication is enabled, THE system SHALL:
  1. Send OTP to user's registered phone
  2. Require OTP entry before issuing final JWT

"""
