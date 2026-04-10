from database.db import get_connection
from utils.logger import log_info, log_error
import json

class TaskService:

    def add_task(self, title):
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
            conn.commit()

            log_info("Task added")

        except Exception as e:
            log_error(str(e))
            print("Error adding task:", e)

        finally:
            cur.close()
            conn.close()

    def get_tasks(self):
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("SELECT * FROM tasks ORDER BY id")
            tasks = cur.fetchall()

            return tasks

        except Exception as e:
            log_error(str(e))
            print("Error fetching tasks:", e)
            return []

        finally:
            cur.close()
            conn.close()

    def complete_task(self, task_id):
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("UPDATE tasks SET status = TRUE WHERE id = %s", (task_id,))
            conn.commit()

            log_info(f"Task {task_id} completed")

        except Exception as e:
            log_error(str(e))
            print("Error completing task:", e)

        finally:
            cur.close()
            conn.close()

    def delete_task(self, task_id):
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
            conn.commit()

            log_info(f"Task {task_id} deleted")

        except Exception as e:
            log_error(str(e))
            print("Error deleting task:", e)

        finally:
            cur.close()
            conn.close()

    def search_task(self, keyword):
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("SELECT * FROM tasks WHERE title ILIKE %s", (f"%{keyword}%",))
            tasks = cur.fetchall()

            return tasks

        except Exception as e:
            log_error(str(e))
            print("Error searching task:", e)
            return []

        finally:
            cur.close()
            conn.close()

    def filter_tasks(self, status):
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("SELECT * FROM tasks WHERE status = %s", (status,))
            tasks = cur.fetchall()

            return tasks

        except Exception as e:
            log_error(str(e))
            print("Error filtering tasks:", e)
            return []

        finally:
            cur.close()
            conn.close()

    def export_json(self):
        try:
            tasks = self.get_tasks()

            data = []
            for t in tasks:
                data.append({
                    "id": t[0],
                    "title": t[1],
                    "status": t[2]
                })

            with open("tasks.json", "w") as f:
                json.dump(data, f, indent=4)

            log_info("Exported tasks to JSON")

        except Exception as e:
            log_error(str(e))
            print("Error exporting JSON:", e)