from enum import Enum

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

action_map = {
    ActionType.SHOW_LIST: show_list,
    ActionType.ADD_ITEM: add_item,
    ActionType.REMOVE_ITEM: remove_item,
    ActionType.EXIT: exit_program
}


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
