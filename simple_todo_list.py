# simple-python-project
# Name: Nadeen
# Project Title: Simple To-Do List Program

tasks = []

while True:
    print("\nSimple To-Do List")
    print("1. Finish your Homework")
    print("2. Clean your desk")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        task = input("Finish your Homework: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")a
