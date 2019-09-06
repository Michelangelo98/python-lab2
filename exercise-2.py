from sys import argv

def choose_from_menu(scelta,errore):





    close=False



    while not close:

        choose = int(input(scelta))

        print("\n\n\n")

        if choose >= 1 and choose <= 4:

            close = True

        else:

            print(errore)





    return choose

def insert_a_new_task():



    todo_list.append(input("New task:"))

def show_all_task() :

    print(sorted(todo_list))

def remove_task() :



    to_remove = input("Task to remove (by exactly):")



    if todo_list.count(to_remove) == 0 :

        print("Task not found")

    else:

        todo_list.remove(to_remove)



if __name__ == '__main__':


    msg_scelta = """Insert the number corresponding to the action you want to perform: 

    1. insert a new task; 

    2. remove a task; 

    3. show all the tasks; 

    4. close the program."""

    msg_errore = "Choose between (1,4)"
    """
    with open(argv[1]) as file_in:
        todo_list = file_in.readlines()

    x="\n"
    todo_list = [x.strip() for x in todo_list]
    """

    file_in = open(argv[1])
    todo_list = file_in.readlines()

    for number in range(0,todo_list.__len__()) :
        todo_list[number] = todo_list[number].strip("\n")
    file_in.close()

    file_out = open(argv[1],'w')


    scelta = choose_from_menu(msg_scelta, msg_errore)

    while scelta != 4:



        if scelta == 1:

            insert_a_new_task()

        elif scelta == 2:

            remove_task()

        elif scelta == 3:

            show_all_task()

        scelta = choose_from_menu(msg_scelta, msg_errore)


    file_out = open(argv[1], 'w')

    for action in todo_list:
        file_out.write(action + "\n")


    file_out.close()
