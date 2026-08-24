from enum import Enum

"""
1. program is a prototype for a to do list app for my database systems class.
2. As of now, I am setting it up as a CLI because I need to learn some SQL and file management first.
3. Initially, i like to set things up using the imperative paradigm, and plan to refactor to OOP once I know more.
    a. I look at this step similar to a sketch before you paint. Once I know the general shapes and colors i want,
       then i can start to fill in the painting.
    b. the other thing this does, it help me to understand the relationships the I am potentially working with.
       Relationships among classes can get complicated pretty quick, so I like to know what I want first.
"""

##############ACTION BLOCK####################

class ActionType(Enum):
    SHOW_LIST = 1
    ADD_ITEM = 2
    REMOVE_ITEM = 3
    EXIT = 4


valid_choices_map = {
    1: "Show List",
    2: "Add Item",
    3: "Remove Item",
    4: "Exit Program"
}

"""
        ACTION FUNCTIONS
        *these all do what they say they'll do.
        *each function takes in the main to do list and modifies it accordingly, except for exit_program... that one exits.
"""
def show_list(to_do_list):
    print(f'ToDo List: {to_do_list}')


def add_item(to_do_list):
    item = input("Enter the item you wish to ADD to the ToDO List: ")
    to_do_list.append(item)
    print(f'Adding "{item}" to list...')


def remove_item(to_do_list):
    item = input("Enter the item you wish to REMOVE from the ToDO List: ")
    if item in to_do_list:
        to_do_list.remove(item)
    else:
        print(f'"{item}" is not in {to_do_list}...')

def exit_program():
    print("Bye!")

#because I wanted to use enums to represent the actions, i had to come up with a workaround. 
#this dictionary maps enums to the desired function call. 
#is it entirely necessary? not really, but I wanted to learn and use enums in python... so here we are.  
action_map = {
    ActionType.SHOW_LIST: show_list,
    ActionType.ADD_ITEM: add_item,
    ActionType.REMOVE_ITEM: remove_item,
    ActionType.EXIT: exit_program
}

"""
we print the map and prompt the user for input. then we chekc if the input is valid.
    valid: then we cast the choice to an enum and return it
    invalid: try again
"""
def get_user_choice():

    print(f'Enter the number corresponding to your desired action: {valid_choices_map}')

    while True:
        try:
            choice = int(input())
            action = valid_choices_map.get(choice)

            if action:
                return ActionType(choice) #cast to enum
            else:
                print("That is not a valid action. Try again...")

        except ValueError:
            print("Oops! That was not a valid number. Try again...")

#this function just accesses our action map, which is a dictionary of function calls.
#this is the last step in the action process.
def decide_to_do_list_action(user_choice, to_do_list):
        action_map[user_choice](to_do_list)


def main():

    to_do_list = []

    while True:
        user_choice = get_user_choice()

        if user_choice == ActionType.EXIT:
            exit_program()
            break
        else:
            decide_to_do_list_action(user_choice, to_do_list)



if __name__ == '__main__':
    main()
