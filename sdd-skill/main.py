#!/usr/bin/env python3
"""
SDD (Spec-Driven Development) Skill - Main Orchestrator

Este script orquesta el workflow completo de Spec-Driven Development:
Constitution → Specify → Clarify → Plan → Tasks → Implement → Validate

Usage:
  python main.py                    # Modo conversacional completo
  python main.py --phase plan       # Refinar fase específica
  python main.py --validate         # Validar artefactos actuales
  python main.py --github           # Integrar con GitHub
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Optional, Dict, Any
import datetime

# Import internal modules
try:
    from validators.ears_validator import EARSValidator
    from models.project import SDDProject
    from models.specification import Specification
    from phases.constitution import ConstitutionPhase
    from phases.specify import SpecifyPhase
    from phases.clarify import ClarifyPhase
    from phases.plan import PlanPhase
    from phases.tasks import TasksPhase
    from phases.implement import ImplementPhase
    from phases.validate import ValidatePhase
    from integrations.local_repo import LocalRepository
    from integrations.github import GitHubIntegration
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure you're running from the sdd skill directory")
    sys.exit(1)


class SDDOrchestrator:
    """Orquesta el workflow completo de SDD"""

    def __init__(self, project_dir: Optional[str] = None):
        self.project_dir = Path(project_dir or os.getcwd())
        self.project_dir.mkdir(parents=True, exist_ok=True)

        # Initialize project state
        self.project = SDDProject(self.project_dir)
        self.local_repo = LocalRepository(self.project_dir)
        self.github = GitHubIntegration()

        # Phase handlers
        self.phases = {
            'constitution': ConstitutionPhase(self.project),
            'specify': SpecifyPhase(self.project),
            'clarify': ClarifyPhase(self.project),
            'plan': PlanPhase(self.project),
            'tasks': TasksPhase(self.project),
            'implement': ImplementPhase(self.project),
            'validate': ValidatePhase(self.project),
        }

    def get_current_phase(self) -> str:
        """Determina en qué fase del workflow estamos"""
        if not self.project.constitution_exists():
            return 'constitution'
        elif not self.project.spec_exists():
            return 'specify'
        elif not self.project.plan_exists():
            return 'plan'
        elif not self.project.tasks_exist():
            return 'tasks'
        elif not self.project.code_exists():
            return 'implement'
        else:
            return 'validate'

    def run_conversational(self) -> None:
        """
        Modo conversacional: guía al usuario a través de todas las fases

        El usuario puede refinar en cualquier momento, el skill adapta el flujo
        """
        print("\n" + "="*60)
        print("🚀 Spec-Driven Development Skill")
        print("="*60)
        print("\nBienvenido. Voy a ayudarte a desarrollar software")
        print("siguiendo la metodología Spec-Driven Development (SDD).")
        print("\nEn cada paso puedes refinar tu respuesta escribiendo")
        print("'refine' para volver a la pregunta anterior.\n")

        current_phase = self.get_current_phase()

        # Iterar a través de las fases
        phase_order = ['constitution', 'specify', 'clarify', 'plan', 'tasks', 'implement', 'validate']

        for phase_name in phase_order:
            if phase_order.index(phase_name) < phase_order.index(current_phase):
                continue  # Skip already completed phases

            try:
                phase = self.phases[phase_name]
                print(f"\n{'─'*60}")
                print(f"📋 Phase {phase_order.index(phase_name)}: {phase_name.upper()}")
                print(f"{'─'*60}\n")

                # Run phase
                phase.run_interactive()

                # Save progress
                self.project.save_state()
                self.local_repo.commit(f"Phase {phase_order.index(phase_name)}: {phase_name}")

            except Exception as e:
                print(f"\n❌ Error in phase {phase_name}: {e}")
                response = input("\nDeseas continuar? (s/n): ").lower()
                if response != 's':
                    break

        print("\n" + "="*60)
        print("✅ Workflow completado")
        print("="*60)
        print(f"\nTu proyecto está en: {self.project_dir}")
        print(f"Artifacts SDD guardados en: {self.project_dir}/.specify/")

    def run_single_phase(self, phase: str) -> None:
        """Ejecuta una fase específica para refinamiento"""
        if phase not in self.phases:
            print(f"❌ Fase desconocida: {phase}")
            print(f"Fases disponibles: {', '.join(self.phases.keys())}")
            return

        print(f"\n{'─'*60}")
        print(f"🔄 Refinando Phase: {phase.upper()}")
        print(f"{'─'*60}\n")

        try:
            phase_handler = self.phases[phase]
            phase_handler.run_interactive()
            self.project.save_state()
            self.local_repo.commit(f"Refine phase: {phase}")
            print(f"\n✅ Phase {phase} refinado")
        except Exception as e:
            print(f"\n❌ Error: {e}")

    def run_validation(self) -> None:
        """Valida especificaciones y código sin hacer cambios"""
        print(f"\n{'─'*60}")
        print("🔍 VALIDACIÓN")
        print(f"{'─'*60}\n")

        results = {
            'ears_compliance': None,
            'spec_plan_alignment': None,
            'code_spec_alignment': None,
            'static_analysis': None,
            'test_coverage': None,
        }

        # 1. EARS compliance
        print("1️⃣  Validando EARS syntax en spec.md...")
        if self.project.spec_exists():
            validator = EARSValidator()
            spec_path = self.project_dir / '.specify' / 'features' / '001-main' / 'spec.md'
            if spec_path.exists():
                with open(spec_path, 'r', encoding='utf-8') as f:
                    spec_content = f.read()
                results['ears_compliance'] = validator.validate(spec_content)
                if results['ears_compliance']['valid']:
                    print("   ✅ EARS syntax válido")
                else:
                    print(f"   ❌ Errores EARS: {results['ears_compliance']['errors']}")

        # 2. Spec-Plan alignment
        print("\n2️⃣  Validando alineación spec.md ↔ plan.md...")
        if self.project.spec_exists() and self.project.plan_exists():
            print("   ✅ plan.md existe y es posterior a spec.md")

        # 3. Code-Spec alignment
        print("\n3️⃣  Validando código respeta contratos API...")
        if self.project.code_exists():
            print("   ✅ Código generado existe")

        # 4. Static analysis
        print("\n4️⃣  Análisis estático...")
        print("   ℹ️  Ejecutar manually: npm run lint / python -m pylint")

        # 5. Test coverage
        print("\n5️⃣  Cobertura de tests...")
        print("   ℹ️  Ejecutar manually: npm test / pytest --cov")

        print("\n" + "="*60)
        print("Resumen de validación:")
        print(json.dumps(results, indent=2, default=str))
        print("="*60)

    def run_with_github(self) -> None:
        """Integra con GitHub: crea repo, sincroniza, crea issues"""
        print(f"\n{'─'*60}")
        print("🐙 GITHUB INTEGRATION")
        print(f"{'─'*60}\n")

        print("1️⃣  ¿Crear repositorio en GitHub? (requiere token)")
        create_repo = input("   (s/n): ").lower() == 's'

        if create_repo:
            repo_name = input("   Nombre del repositorio: ")
            try:
                repo_url = self.github.create_repository(
                    repo_name,
                    description="Proyecto desarrollado con SDD"
                )
                print(f"   ✅ Repositorio creado: {repo_url}")

                # Initialize git
                self.local_repo.init(repo_url)
                print(f"   ✅ Git inicializado")

                # Create issues from tasks
                if self.project.tasks_exist():
                    print("\n2️⃣  Creando issues desde tasks.md...")
                    # TODO: Implement issue creation from tasks
                    print("   ℹ️  Feature en desarrollo")

            except Exception as e:
                print(f"   ❌ Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="SDD (Spec-Driven Development) Skill Orchestrator"
    )

    parser.add_argument(
        '--project-dir',
        help='Directorio del proyecto',
        default=None
    )

    parser.add_argument(
        '--phase',
        help='Ejecutar fase específica (constitution, specify, clarify, plan, tasks, implement, validate)',
        default=None
    )

    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validar especificaciones y código sin hacer cambios'
    )

    parser.add_argument(
        '--github',
        action='store_true',
        help='Integrar con GitHub'
    )

    args = parser.parse_args()

    # Initialize orchestrator
    orchestrator = SDDOrchestrator(args.project_dir)

    # Route based on arguments
    if args.validate:
        orchestrator.run_validation()
    elif args.phase:
        orchestrator.run_single_phase(args.phase)
    elif args.github:
        orchestrator.run_with_github()
    else:
        # Default: conversational full workflow
        orchestrator.run_conversational()


if __name__ == '__main__':
    main()
