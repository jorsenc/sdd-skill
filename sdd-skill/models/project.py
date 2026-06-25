"""
Models for SDD Project Management

Mantiene el estado del proyecto a lo largo del workflow:
- Constitution (reglas inmutables)
- Specifications (EARS)
- Plans (técnico)
- Tasks (descomposición)
- Generated Code
"""

import json
from pathlib import Path
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, asdict
import datetime


@dataclass
class ProjectMetadata:
    """Metadata del proyecto SDD"""
    created_at: str
    updated_at: str
    name: str
    description: str
    version: str = "1.0.0"
    sdd_level: int = 2  # 1=Spec-First, 2=Spec-Anchored, 3=Spec-as-Source


class SDDProject:
    """Gestor de estado del proyecto SDD"""

    def __init__(self, project_dir: Path):
        self.project_dir = Path(project_dir)
        self.specify_dir = self.project_dir / '.specify'
        self.src_dir = self.project_dir / 'src'
        self.metadata_file = self.specify_dir / 'metadata.json'

        # Create directories
        self.specify_dir.mkdir(parents=True, exist_ok=True)
        self.src_dir.mkdir(parents=True, exist_ok=True)

        # Load or initialize metadata
        self._load_or_create_metadata()

    def _load_or_create_metadata(self) -> None:
        """Carga o crea metadata del proyecto"""
        if self.metadata_file.exists():
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                self.metadata_dict = json.load(f)
        else:
            self.metadata_dict = {
                'created_at': datetime.datetime.now().isoformat(),
                'updated_at': datetime.datetime.now().isoformat(),
                'name': 'SDD Project',
                'description': '',
                'version': '1.0.0',
                'sdd_level': 2,
            }

    def save_state(self) -> None:
        """Guarda metadata del proyecto"""
        self.metadata_dict['updated_at'] = datetime.datetime.now().isoformat()
        self.metadata_file.parent.mkdir(parents=True, exist_ok=True)

        with open(self.metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata_dict, f, indent=2)

    def constitution_exists(self) -> bool:
        """Verifica si constitution.md existe"""
        return (self.specify_dir / 'constitution.md').exists()

    def spec_exists(self) -> bool:
        """Verifica si spec.md existe"""
        return (self.specify_dir / 'features' / '001-main' / 'spec.md').exists()

    def plan_exists(self) -> bool:
        """Verifica si plan.md existe"""
        return (self.specify_dir / 'features' / '001-main' / 'plan.md').exists()

    def tasks_exist(self) -> bool:
        """Verifica si tasks.md existe"""
        return (self.specify_dir / 'features' / '001-main' / 'tasks.md').exists()

    def code_exists(self) -> bool:
        """Verifica si código fue generado"""
        python_files = list(self.src_dir.glob('**/*.py'))
        ts_files = list(self.src_dir.glob('**/*.ts'))
        go_files = list(self.src_dir.glob('**/*.go'))

        return len(python_files) > 0 or len(ts_files) > 0 or len(go_files) > 0

    def read_constitution(self) -> Optional[str]:
        """Lee contenido de constitution.md"""
        path = self.specify_dir / 'constitution.md'
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return None

    def read_spec(self) -> Optional[str]:
        """Lee contenido de spec.md"""
        path = self.specify_dir / 'features' / '001-main' / 'spec.md'
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return None

    def read_plan(self) -> Optional[str]:
        """Lee contenido de plan.md"""
        path = self.specify_dir / 'features' / '001-main' / 'plan.md'
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return None

    def read_tasks(self) -> Optional[str]:
        """Lee contenido de tasks.md"""
        path = self.specify_dir / 'features' / '001-main' / 'tasks.md'
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        return None

    def write_constitution(self, content: str) -> None:
        """Escribe constitution.md"""
        path = self.specify_dir / 'constitution.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    def write_spec(self, content: str) -> None:
        """Escribe spec.md"""
        path = self.specify_dir / 'features' / '001-main' / 'spec.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    def write_plan(self, content: str) -> None:
        """Escribe plan.md"""
        path = self.specify_dir / 'features' / '001-main' / 'plan.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    def write_tasks(self, content: str) -> None:
        """Escribe tasks.md"""
        path = self.specify_dir / 'features' / '001-main' / 'tasks.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    def write_code(self, file_path: str, content: str) -> None:
        """Escribe archivo de código generado"""
        full_path = self.src_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def get_metadata(self) -> Dict[str, Any]:
        """Retorna metadata actual del proyecto"""
        return self.metadata_dict

    def update_metadata(self, **kwargs) -> None:
        """Actualiza campos de metadata"""
        for key, value in kwargs.items():
            if key in self.metadata_dict:
                self.metadata_dict[key] = value
        self.save_state()
