from services.task_service import TaskService

class TaskController:

    def __init__(self):
        self.service = TaskService()

    def add(self):
        title = input("Enter task: ")
        if not title:
            print("Task cannot be empty!")
            return
        self.service.add_task(title)
        print("Task added!")

    def list(self):
        tasks = self.service.get_tasks()
        if not tasks:
            print("No tasks found")
            return

        for t in tasks:
            status = "Done" if t[2] else "Pending"
            print(f"ID: {t[0]} | {t[1]} | {status}")

    def complete(self):
        task_id = int(input("Enter task ID: "))
        self.service.complete_task(task_id)
        print("Task completed!")

    def delete(self):
        task_id = int(input("Enter task ID: "))
        self.service.delete_task(task_id)
        print("Task deleted!")

    def search(self):
        keyword = input("Enter keyword: ")
        tasks = self.service.search_task(keyword)

        for t in tasks:
            status = "Done" if t[2] else "Pending"
            print(f"ID: {t[0]} | {t[1]} | {status}")

    def filter(self):
        print("1. Completed\n2. Pending")
        choice = input("Choose: ")

        status = True if choice == "1" else False
        tasks = self.service.filter_tasks(status)

        for t in tasks:
            status_text = "Done" if t[2] else "Pending"
            print(f"ID: {t[0]} | {t[1]} | {status_text}")

    def export(self):
        self.service.export_json()
        print("Exported to tasks.json")