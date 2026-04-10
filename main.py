from controllers.task_controller import TaskController

controller = TaskController()

while True:
    print("\n==== TASK MANAGER ====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Filter Tasks")
    print("7. Export to JSON")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        controller.add()

    elif choice == "2":
        controller.list()

    elif choice == "3":
        controller.complete()

    elif choice == "4":
        controller.delete()

    elif choice == "5":
        controller.search()

    elif choice == "6":
        controller.filter()

    elif choice == "7":
        controller.export()

    elif choice == "8":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")