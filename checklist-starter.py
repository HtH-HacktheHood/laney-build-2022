'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''

# Create our Checklist
checklist = []

# Define Functions
def create(item):
    # Create item code here
    checklist.append(item)

    return print( f"{item} was added to the checklist: {checklist}" )

def read(index):
    # Read code here
    return print(f"{checklist[index]} is at the {index} position")

def update(index, item):
    # Update code here
    old_item = checklist[index]
    checklist[index] = f'[ ] {item}'

    return print(f"{old_item} was changed to {item}")

def destroy(index):
    # Destroy code here
    old_item = checklist[index]
    checklist.pop(index)

    return print(f"{old_item} was deleted from checklist")

def mark_completed(index):
    # Add code here that marks an item as completed

    if "*" not in checklist[index]:
        checklist[index] = f'[*] {checklist[index]}'

        return print(f"{checklist[index]} was marked completed")
        
    else:
        
        return print(f"That item was marked completed already")

    

def list_all_items():
    # List all items code here

    completed = 0
    incomplete = []

    for item in checklist:

        if "*" not in item:
            incomplete.append(item)
            
        else:
            completed += 1

    for ele in incomplete:
        print(ele)
    
    return print(f'\n{completed} tasks have been finished already')

    

def select(function_code):
    # User Selection Code here

    # Create item example
    if function_code == "C":
        input_item = input("Enter an element to add to the list: ")
        create(input_item)
        running = True

        return running

    elif function_code == "R":
        input_item = input("Enter the index position you are trying to access in the list: ")
        read(int(input_item))
        running = True

        return running

    elif function_code == "U":
        input_index = input("Enter the index position you are trying to update in the list: ")
        input_item = input("Enter the element you are trying to update to the list: ")
        update(int(input_index), input_item)
        running = True
        
        return running

    elif function_code == "D":
        input_index = input("Enter the index position of the element you want to delete: ")
        destroy(int(input_index))
        running = True

        return running

    elif function_code == "M":
        input_index = input("Enter the index position of the element you want to mark completed: ")
        mark_completed(int(input_index))
        running = True

        return running

    elif function_code == "L":
        list_all_items()
        running = True

        return running

    else:
        print("Please enter a valid checklist command!")
        
        running = True

        return running

running = True

while running:
    selection = input(
        "Press C to add to list, R to Read from list, U to update an existing entry, D to delete an element in the list list, M to mark an item completed, L to list out items and Q to quit: ").upper()
    running = select(selection)