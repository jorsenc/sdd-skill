"""Phase 1: Specification - Write EARS requirements"""
from models.project import SDDProject

class SpecifyPhase:
    def __init__(self, project: SDDProject):
        self.project = project

    def run_interactive(self) -> None:
        print("Phase 1: SPECIFICATION (EARS Syntax)\n")
        print("Describe QUÉ funcionalidad quieres implementar.")
        print("Usa patrones EARS (Ubiquitous, Event-Driven, State-Driven, etc.)\n")

        description = input("Descripción breve de la funcionalidad: ").strip()
        print("\nAhora escribe los requisitos en EARS syntax.")
        print("Puedes pegar múltiples líneas. Escribe 'DONE' en línea nueva para terminar:\n")

        requirements_lines = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            if line.strip():
                requirements_lines.append(line)

        spec_content = f"""# Specification: {description}

## Overview
{description}

## Requirements (EARS Format)

{chr(10).join(requirements_lines)}
"""

        self.project.write_spec(spec_content)
        print("\n✅ Specification guardada\n")
        print(spec_content)
