"""Phase implementation stub for validate"""
from models.project import SDDProject

class ValidatePhase:
    def __init__(self, project: SDDProject):
        self.project = project

    def run_interactive(self) -> None:
        print("Phase: Validate")
        print("⚠️  This phase is under development")
        print("For now, please use the plan file to continue.")
