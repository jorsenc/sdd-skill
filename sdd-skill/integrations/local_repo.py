"""Local Repository Management"""
from pathlib import Path

class LocalRepository:
    def __init__(self, path):
        self.path = Path(path)

    def init(self, remote_url=None):
        print(f"Initializing git repo at {self.path}")

    def commit(self, message):
        print(f"Git commit: {message}")
