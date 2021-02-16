#to-do list
#by ryan langstone
import time
todo_list = []
def number_input(phrase, option):
    digit = ""
    while digit == "":
        try: 
            digit = int(input(phrase))
            if digit not in option:
                print ("has to be of one of the options provided")
                digit = ""
        except:
            print("needs to be a number of one of the provided options")
    return  digit

def menu():
    otions = [1,2,3]
    print("chose a mode by entering a number:")
    print("1: add a item to list")
    print("2: view your list")
    print("3: exit")
    return  number_input("", otions)

def add_item():
    item = "start"
    while item != "0" and item != "exit":
        item = input("Enter a taskk to add to your list or type 0 or exit to return to menue\n")
        if item != "0" and item != "exit":
            todo_list.append(item)

def print_list():
    print("Here is your to-do list:")
    for i in todo_list:
        print(i)

value = 0
while value != 3:
    value = menu()
    if value == 1:
        add_item()
    elif value == 2:
        print_list()
    else:
        print("hope you use this tool again some time")
        time.sleep(1)
        print("see ya")