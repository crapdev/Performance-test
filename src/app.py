
from services import add_task, show_task, search_task, update_task, delete_task
from files import save_csv,upload_csv

inventory= []


print("\n--- Welcome to Notion ---")

def choice():
    option = 1
    while option > 0 and option < 9:
        try:
            option = int(input("""\nEnter what you want to do:
1. Add Task 
2. Show Task
3. Search Task
4. Update Task
5. Delete Task
6. Save taks to CSV
7. Load task from CSV
8. Exit
..."""))

            if option == 1:
                add_task(inventory)
            elif option ==2:
                show_task(inventory)
            elif option == 3:
                search_task(inventory)
            elif option == 4:
                update_task(inventory)
            elif option == 5:
                delete_task(inventory)
            elif option == 6:
                save_csv(inventory, route='data/inventory.csv', include_header=True)
            elif option == 7:
                upload_csv(inventory)
            elif option == 8:
                return print('\nThanks for used our services')
            else:
                print(f"\n{'-' * 10} Invalid input {'-' * 10}")
                choice()
        #in case I miss a value error in the functions
        except ValueError:
            print(f"\n{'-' * 10} Invalid input {'-' * 10}")
            choice()

choice()


#Todo esta bien lo unico es que no pregunta al usuario en el cargar csv Sobrescribir inventario actual? 
# y si se carga un csv, al momento de agregar las nuevas tareas empieza desde 0, sin importar el csv
