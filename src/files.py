import csv, os

def checks_csv():
    #It returns all the files in that folder.
    files = os.listdir("data")
    csv_files = [f for f in files if f.endswith(".csv")] #Save to use only the CSV files
    
    #save if there is only one
    if len(csv_files) == 1:
        return f'data/{csv_files[0]}'
    elif len(csv_files) > 1:
        print(f"These .csv files have been found\n{csv_files}")
        file = input("Enter the file name with the extension:  ").strip().lower()
        for f in csv_files:
            if f == file:
                return file # that returns the name of the entered file
        #I entered the CSV file name incorrectly.
        return None
    else:
        return None


def save_csv(inventory,route, include_header): #6 ***********************
    if not inventory:
        return print(f"{'-' * 10}Inventory is empty {'-' * 10} ")
    try:
        #If there is no header, it is put into w mode to overwrite, otherwise into a mode to add.
        mode = 'w' if include_header else 'a'
        with open(route, mode, encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            
            if include_header:
                writer.writerow(['Id','Title','Description', 'Priority', 'Status'])

                for task in inventory:
                    writer.writerow([task['id'],task['title'], task['description'], task['priority'], task['status']])
                
            return print('The data has been successfully saved')
        
    except PermissionError:
        #just in case
        return print(f"{'-' * 10} You don't have write permissions {'-' * 10}")
    except Exception as e:
        return print(f"{'-' * 10} General error saving the file {'-' * 10}\n {e}") #just in case
    

def upload_csv(inventory): #7 ***********************
    try:
        route = checks_csv()  # Search for CSV files in data
        if route is None:
            return print(f"{'-' * 10} There are no CSV files or the name you entered is incorrect {'-' * 10}")

        with open(f'data/{route}', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)  
            header = next(reader)  # to read the header

            # If there are not exactly 3 columns, it fails.
            try:
                col_id, col_title, col_description, col_priority, col_status = header
            except ValueError:
                return print(f"{'-' * 10} Error in the expected header; this file cannot be loaded {'-' * 10}")
            
            # Validate that the header names are as expected, regardless of capitalization/spaces
            expected = ['id', 'title', 'description', 'priority', 'status']
            if [col.lower().strip() for col in header] != expected:
                return print(f"{'-' * 10} The header doesn't match the expected format {'-' * 10}")

            # enumerate starts at 2 because row 1 is the header
            for row in reader:
                id, title, description, priority, status = row  # for each row stores the values

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
                

        print(f"{len(inventory)} products loaded successfully")
        return inventory

    except FileNotFoundError:
        print(f"{'-' * 10} File not found {'-' * 10}")
    except Exception as e:
        print(f"{'-' * 10} General error loading the file {'-' * 10}\n {e}")