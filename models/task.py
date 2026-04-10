class Task:
    def __init__(self, title, status=False):
        self.title = title
        self.status = status

    def __str__(self):
        return f"Task(title={self.title}, status={self.status})"