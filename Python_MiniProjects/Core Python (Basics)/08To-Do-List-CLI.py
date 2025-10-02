tasks=[] 

def showMenu():
    print("----Welcome to To-Do List CLI---")
    print("""
            1. View Tasks
            2. Add Task 
            3. Delete Task
            4. Update Task
            5. Exit
    """)

while True:
    showMenu()
    choice=int(input("Enter Choice from 1-5:"))

    if choice==1:
        print("You selected Choice 1-View Task")
        if not tasks:
            print("No Tasks to display")
        else:
            for i, task in enumerate(tasks,start=1):
                print(f"{i}-{task}")
    elif choice==2:
        print("You selected Choice 2-Add Task")
        newTask = input("Enter the Task:")
        tasks.append(newTask)
        print("New Task Added")
    elif choice==3: 
        print("You selected Choice 3-Delete Task")
        if not tasks:
            print("No Tasks to delete")
        else:
            try:
                num=int(input("Enter the Task no to delete"))
                if num >1 and num <=len(tasks):
                    removedTask=tasks.pop(num-1)
                    print("Task has been deleted")
                else:
                    print("Invalid Task")   
            except ValueError:
                print("Invalid Selection")

    elif choice == 4:  
        print("You selected Choice 4-Update Task")
        if not tasks:
            print("No tasks to update")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}-{task}")
            try:
                num = int(input("Enter the Task number to update: "))
                if 1 <= num <= len(tasks):
                    new_task = input("Enter the new task: ")
                    tasks[num - 1] = new_task
                    print("Task updated successfully")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number")
    elif choice==5:   
        print("You selected Choice 5-Exit")
        print("Exiting... Goodbye!")
        break
    else:
        print("Sorry!!! You selected an wrong choice")