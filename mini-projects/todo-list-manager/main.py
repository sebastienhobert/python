from os import removedirs


def display_menu():
    print("\nTo-Do List Menu:")
    print('1. Add a task')
    print('2. View tasks')
    print('3. Remove a task')
    print('4. Exit')

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')

def view_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input ("Enter your choice (1/2/3/4): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4")

if __name__ == "__main__":
    main()