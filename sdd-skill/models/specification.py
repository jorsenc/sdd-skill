"""
Specification Model for EARS-compliant Requirements

Representa una especificación EARS y valida su estructura
"""

from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from enum import Enum


class EARSPatternType(Enum):
    """Tipos de patrones EARS"""
    UBIQUITOUS = "ubiquitous"
    EVENT_DRIVEN = "event_driven"
    STATE_DRIVEN = "state_driven"
    UNWANTED = "unwanted"
    OPTIONAL = "optional"
    UNKNOWN = "unknown"


@dataclass
class RequirementStatement:
    """Representa una declaración de requisito EARS"""
    pattern_type: EARSPatternType
    text: str
    line_number: int
    is_valid: bool = True
    validation_errors: List[str] = None

    def __post_init__(self):
        if self.validation_errors is None:
            self.validation_errors = []


class Specification:
    """Modelo de Especificación EARS"""

    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.requirements: List[RequirementStatement] = []
        self.sections: Dict[str, List[RequirementStatement]] = {}

    def add_requirement(self, pattern_type: EARSPatternType, text: str, line_number: int) -> None:
        """Agrega un requisito a la especificación"""
        req = RequirementStatement(
            pattern_type=pattern_type,
            text=text,
            line_number=line_number
        )
        self.requirements.append(req)

    def add_section(self, section_name: str, requirements: List[RequirementStatement]) -> None:
        """Agrupa requisitos por sección"""
        self.sections[section_name] = requirements

    def get_by_pattern(self, pattern_type: EARSPatternType) -> List[RequirementStatement]:
        """Retorna todos los requisitos de un tipo específico"""
        return [r for r in self.requirements if r.pattern_type == pattern_type]

    def get_ubiquitous(self) -> List[RequirementStatement]:
        """Retorna requisitos Ubiquitous"""
        return self.get_by_pattern(EARSPatternType.UBIQUITOUS)

    def get_event_driven(self) -> List[RequirementStatement]:
        """Retorna requisitos Event-Driven"""
        return self.get_by_pattern(EARSPatternType.EVENT_DRIVEN)

    def get_state_driven(self) -> List[RequirementStatement]:
        """Retorna requisitos State-Driven"""
        return self.get_by_pattern(EARSPatternType.STATE_DRIVEN)

    def get_unwanted_behavior(self) -> List[RequirementStatement]:
        """Retorna requisitos Unwanted Behavior"""
        return self.get_by_pattern(EARSPatternType.UNWANTED)

    def get_optional(self) -> List[RequirementStatement]:
        """Retorna requisitos Optional"""
        return self.get_by_pattern(EARSPatternType.OPTIONAL)

    def count_requirements(self) -> int:
        """Retorna cantidad total de requisitos"""
        return len(self.requirements)

    def count_by_pattern(self, pattern_type: EARSPatternType) -> int:
        """Retorna cantidad de requisitos por tipo"""
        return len(self.get_by_pattern(pattern_type))

    def is_valid(self) -> bool:
        """Verifica si todas las especificaciones son válidas"""
        return all(r.is_valid for r in self.requirements)

    def get_validation_summary(self) -> Dict[str, Any]:
        """Retorna resumen de validación"""
        return {
            'total_requirements': self.count_requirements(),
            'ubiquitous': self.count_by_pattern(EARSPatternType.UBIQUITOUS),
            'event_driven': self.count_by_pattern(EARSPatternType.EVENT_DRIVEN),
            'state_driven': self.count_by_pattern(EARSPatternType.STATE_DRIVEN),
            'unwanted': self.count_by_pattern(EARSPatternType.UNWANTED),
            'optional': self.count_by_pattern(EARSPatternType.OPTIONAL),
            'is_valid': self.is_valid(),
            'total_errors': sum(len(r.validation_errors) for r in self.requirements),
        }

    def export_markdown(self) -> str:
        """Exporta especificación a formato markdown"""
        lines = [f"# {self.title}\n"]

        if self.description:
            lines.append(f"{self.description}\n")

        # Export by pattern type
        patterns_and_names = [
            (EARSPatternType.UBIQUITOUS, "Ubiquitous Requirements"),
            (EARSPatternType.EVENT_DRIVEN, "Event-Driven Requirements"),
            (EARSPatternType.STATE_DRIVEN, "State-Driven Requirements"),
            (EARSPatternType.UNWANTED, "Unwanted Behavior Handling"),
            (EARSPatternType.OPTIONAL, "Optional/Conditional Requirements"),
        ]

        for pattern_type, section_name in patterns_and_names:
            reqs = self.get_by_pattern(pattern_type)
            if reqs:
                lines.append(f"\n## {section_name}\n")
                for req in reqs:
                    lines.append(f"- {req.text}\n")

        return "".join(lines)
