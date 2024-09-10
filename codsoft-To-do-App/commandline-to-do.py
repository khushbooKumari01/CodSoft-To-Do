#This is our Heading
print("***********************************************************")
print("*                        To-Do-App                        *")
print("***********************************************************")
#we Take list data type
performTask =[]

# we create function for all operation
def add_task():
    """ Adding task Information"""
    task=input("Enter Your Task :")
    performTask.append(task)
    print("Your task add successfully")

#code for update task
def update_task(task_number, new_task):
    """Updates an existing task with a new task description."""
    if 0 < task_number <= len(performTask):
        old_task = performTask[task_number - 1]
        performTask[task_number - 1] = new_task
        print(f"Task '{old_task}' updated to '{new_task}'.")
    else:
        print("Invalid task number.")


# code for delete task
def delete_task():
    if len(performTask) ==0:
        print('no tasks to delete')
    else:
        print('task')
        for i,tasks in enumerate(performTask):
            print(f'{i+1}.{tasks}')
            option=int(input("Enter the task number to delete"))
            if 0<option <=len(performTask):
                del performTask[option-1]
                print('Task deleted successfully')
            else:
                print("Wrong Task Number")


#code for display task
def view_task():
    """All Display Your Task"""
    if len(performTask) ==0:
        print("No Tasks.")
    else:
        print("Menu of Task")
        for i,task in enumerate(performTask):
            print(f'{i+1}.{task}')


def main():
    while True:
        print("\n----Manage Your Task----")
        print("1.Add Task")
        print("2.Update Task")
        print("3.Delete Task")
        print("4.view Task")
        print("5.Stop")
        option = int(input("Enter Your Task Number"))
        if option == 1:
            add_task()
        elif option ==2:
            task_number = int(input("Enter task number to update: "))
            new_task = (input("Enter the new task: "))
            update_task(task_number, new_task)

        elif option == 3:
            delete_task()

        elif option==4:
            view_task()
        elif option==5:
            break
        else:print("Wrong Task Number.Please try again")
if __name__ =="__main__":
    main()


