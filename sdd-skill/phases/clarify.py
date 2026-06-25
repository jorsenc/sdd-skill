"""Phase implementation stub for clarify"""
from models.project import SDDProject

class ClarifyPhase:
    def __init__(self, project: SDDProject):
        self.project = project

    def run_interactive(self) -> None:
        print("Phase: Clarify")
        print("⚠️  This phase is under development")
        print("For now, please use the plan file to continue.")
