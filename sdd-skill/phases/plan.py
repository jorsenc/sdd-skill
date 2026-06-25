"""Phase implementation stub for plan"""
from models.project import SDDProject

class PlanPhase:
    def __init__(self, project: SDDProject):
        self.project = project

    def run_interactive(self) -> None:
        print("Phase: Plan")
        print("⚠️  This phase is under development")
        print("For now, please use the plan file to continue.")
