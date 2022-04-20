'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''

# Create our Checklist
checklist = 

# Define Functions
def create(item):
    # Create item code here

def read(index):
    # Read code here

def update(index, item):
    # Update code here

def destroy(index):
    # Destroy code here

def mark_completed(index):
    # Add code here that marks an item as completed

def list_all_items():
    # List all items code here

def user_input(prompt):
    # Get user input here

def select(function_code):
    # User Selection Code here

    # Create item example
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

running = True

while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)