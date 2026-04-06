#***********  help functions   ********************
#ask if they want to try again
def options_(end,start):
    if end - start == 1:
        def yesornot():
            try:
                retry = int(input(f'\nInvalid input, do you wanna try again?\n1.YES!\n2.NO!'))
                #It repeats if you don't enter 1 or 2
                if retry != 1 and retry != 2:
                    return yesornot()
                return retry 
            #If you enter text, you must re-enter one of the two options.
            except ValueError:
                return yesornot()
        return yesornot()

    #update data
    else:
        def thr_option():
            try:
                retry = int(input(f'\nEnter what you want to change...\n1.Title!\n2.description!\n3.priority\n4.Status \n5.None'))
                #It repeats when a different number between 1 and 5 is entered.
                if retry != 1 and retry != 2 and retry != 3 and retry != 4 and retry !=5:
                    return thr_option()
                return retry 
            #It repeats if you enter text in the numbers
            except ValueError:
                print(f"\n{'-' * 10}Invalid input {'-' * 10}")
                return thr_option()
        return thr_option()


def get_task_data():
    retry = 1
    # Loop to continue requesting product data until it is entered correctly, with output
    while retry != 2:
        try:
            #data entry
            title = input("Enter the task title:  ").strip().lower()
            description = input("Enter the task description:  ").strip().lower()

            #Repeat until it enters correctly.
            n_pri = int(input('Enter the task priority:\n1.High\n2.Medium\n3.Low\n:'))
            priority = ""
            #if he made a mistake
            while n_pri != 1 and n_pri != 2 and n_pri != 3:
                print(f"\n{'-' * 10}Invalid input {'-' * 10}")
                n_pri = int(input('Enter the task priority:\n1.High\n2.Medium\n3.Low\n:'))
            if n_pri ==1 :
                priority = "high"
            elif n_pri == 2 :
                priority = "medium"
            elif n_pri == 3 :
                priority = "low"
            
            #Repeat until it enters correctly.
            n_st = int(input('Enter the task status:\n1.to do\n2.Done\n:'))
            status =""
            #if he made a mistake
            while n_st != 1 and n_st != 2:
                print(f"\n{'-' * 10}Invalid input {'-' * 10}")
                n_st = int(input('Enter the task status:\n1.to do\n2.Done\n:'))
            if n_st == 1:
                status = "to do"
            elif n_st == 2:
                status = "done"

            #return correctly data
            return title, description, priority, status
        
        except ValueError: #If this happens, it's because you entered text when entering a number.
            retry = options_(2,1) #ask if they want to try again after making a mistake
            if retry == 2:
                return None #return none if he did not want to try again

# ************   ACTIONS    *************
id = 0
def add_task(inventory): #1 ---
    global id
    #just in case
    print('\nNote: Do not use spaces or accents unless necessary.')

    result = get_task_data() #Request the data
    title, description, priority, status = result
    #If there's nothing, it's because I don't save anything.
    if result is None:
        return print(f"\n{'-' * 10} No products were saved {'-' * 10}")
    
    #Dictionary outline task
    task = {
        'id': id,
        'title': title,
        'description': description,
        'priority': priority,
        'status': status
    }
    #save
    inventory.append(task)
    id += 1
    #successfully saved
    return print(f"\nTask '{title}', with priority '{priority}', with status '{status}', with id '{id-1}'  has been successfully saved. ")


def show_task(inventory): #2 **************
    if not inventory:
        return print(f"{'-' * 10}There are no tasks {'-' * 10} ")
    # display the tasks in order
    for i,task in enumerate(inventory,1):
        print(f'Task {i}.ID: {task["id"]} | {task["title"]} | Description: {task ["description"]}| Priority: {task ["priority"]} | State: {task["status"]} ')

def search_task(inventory): #3 **************
    s_task = input("\nEnter an ID, title, or status of the task you want to search for. \n Example: '1' or 'first task' or 'to do':  ").strip().lower()

    #in case you enter ID
    try:
        id = int(s_task)
    except ValueError:
        pass
    
    #search task
    for task in inventory:
        if task['id'] == id:
            return print(f'Task found!\n {task}')
        if task['title'] == s_task or task['status'] == s_task:
            return print(f'Task found!\n {task}')

    return print(f" {'-' * 10} Product not found! {'-' * 10}")
    


def update_task(inventory): #4 **************
    id = int(input('\nEnter the ID of the task you want to update '))
    for task in inventory:
        #if you find it change
        if task['id'] == id:

            option = int(input('\nDo you like chage everything or not?\n1.YES!\n2.NO!'))
            while option > 0 and option < 3:

                if option == 1:
                    result = get_task_data() #Request the data
                    title, description, priority, status = result
                    #If there's nothing, it's because I don't save anything.
                    if result is None:
                        return print(f"\n{'-' * 10} No products were saved {'-' * 10}")
                    
                    #successfully update
                    task['title'],task['description'],task['priority'],task['status'] = title, description, priority, status
                    return print(f"\nTask '{title}', with priority '{priority}', with status '{status}', with id '{id}'  has been successfully update. ")
                
                if option == 2:#change just one thing
                    option = options_(4,1)
                    if option == 1:
                        task['title'] = input('Enter the task title to update:  ').strip().lower()
                        return print(f"\ntask '{task['title']}' updated to inventory  ")
                    
                    elif option == 2:
                        task['description'] = input('Enter the task description to update:  ').strip().lower()
                        return print(f"\nTask '{task['title']}' updated to inventory with description {task['description']} ")
                    
                    elif option == 3:
                        n_pri = int(input('\nEnter the task priority:\n1.High\n2.Medium\n3.Low\n:'))
                        priority = ""
                        #if he made a mistake
                        while n_pri != 1 and n_pri != 2 and n_pri != 3:
                            print(f"\n{'-' * 10}Invalid input {'-' * 10}")
                            n_pri = int(input('Enter the task priority:\n1.High\n2.Medium\n3.Low\n:'))
                        if n_pri ==1 :
                            priority = "high"
                        elif n_pri == 2 :
                            priority = "medium"
                        elif n_pri == 3 :
                            priority = "low"
                        task['priority'] = priority
                        return print(f"\nTask '{task['title']}' updated to inventory with priority {task['priority']} ")
                    
                    elif option == 4:
                        n_st = int(input('\nEnter the task status:\n1.to do\n2.Done\n:'))
                        status =""
                        #if he made a mistake
                        while n_st != 1 and n_st != 2:
                            print(f"\n{'-' * 10}Invalid input {'-' * 10}")
                            n_st = int(input('Enter the task status:\n1.to do\n2.Done\n:'))
                        if n_st == 1:
                            status = "to do"
                        elif n_st == 2:
                            status = "done"
                        task['status'] = status
                        return print(f"\nTask '{task['title']}' updated to inventory with status {task['status']} ")
                    else:
                        return print(f"{'-' * 10} No task have been updated! {'-' * 10}")

    return print(f" {'-' * 10} Task not found to update! {'-' * 10}")
    
                            
                
def delete_task(inventory): #5 ***********************
    id = int(input('\nEnter the task id to delete: '))
    for task in inventory:
        #if you find it delete
        if task['id'] == id:
            inventory.remove(task)
            return print(f"Task with id'{id}' deleted  ")

    return print(f"{'-' * 10} Task not found! {'-' * 10}")
