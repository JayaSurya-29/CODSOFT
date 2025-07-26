class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list!")
            return
        
        print("\nYour To-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")
    
    def mark_completed(self, task_number):
        try:
            if 1 <= task_number <= len(self.tasks):
                self.tasks[task_number-1]["completed"] = True
                print(f"Task {task_number} marked as completed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def delete_task(self, task_number):
        try:
            if 1 <= task_number <= len(self.tasks):
                removed_task = self.tasks.pop(task_number-1)
                print(f"Task '{removed_task['task']}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_num = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(task_num)
        elif choice == "4":
            todo_list.view_tasks()
            task_num = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_num)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()