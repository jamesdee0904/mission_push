class Task:
    tasks = []   # class variable to store all tasks
    task_counter = 0

    def __init__(self, description):
        Task.task_counter += 1
        self.id = Task.task_counter
        self.description = description

    @classmethod
    def add_task(cls, description):
        task = Task(description)
        cls.tasks.append(task)
        return f"Task added successfully (ID: {task.id})"

    @classmethod
    def view_tasks(cls):
        if not cls.tasks:
            return "No tasks yet."
        result = "To-Do List:\n"
        for task in cls.tasks:
            result += f"ID: {task.id}, Task: {task.description}\n"
        return result.strip()

    @classmethod
    def update_task(cls, task_id, new_description):
        for task in cls.tasks:
            if task.id == task_id:
                task.description = new_description
                return "Task updated successfully"
        return "Task not found"

    @classmethod
    def delete_task(cls, task_id):
        for task in cls.tasks:
            if task.id == task_id:
                cls.tasks.remove(task)
                return "Task deleted successfully"
        return "Task not found"


# ----------------
# Example Run
# ----------------

while True:
    task = input("Enter task: ")
    ask = input("Add another [y/n]: ")
    print(Task.add_task(task)) # task == "write"

    if ask.lower() == 'n':
        break

print(Task.view_tasks())

print(Task.update_task(2, "read"))
print(Task.view_tasks())
print(Task.delete_task(2))
print(Task.view_tasks())


###########

'''
class ToDo:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

    def viewTask(self):
        print(f"Task: {self.description}, Due: {self.due_date}")


# List to hold multiple task objects
tasks = []

# Ask how many tasks the user wants to add
#num = int(input("How many tasks do you want to add? "))

while True:
    desc = input("Enter task description: ")
    due = input("Enter due date: ")
    task = ToDo(desc, due)  # create object
    tasks.append(task)      # store in list
    ask = input("Enter another task? [y/n]: ")

    if ask.lower() == 'y':
        True
    elif ask.lower == 'n':
        break
    else:
        break

# Display all tasks
print("\n--- To-Do List ---")
for t in tasks:
    t.viewTask()
'''