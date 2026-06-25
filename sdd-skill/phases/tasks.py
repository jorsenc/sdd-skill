"""Phase implementation stub for tasks"""
from models.project import SDDProject

class TasksPhase:
    def __init__(self, project: SDDProject):
        self.project = project

    def run_interactive(self) -> None:
        print("Phase: Tasks")
        print("⚠️  This phase is under development")
        print("For now, please use the plan file to continue.")
