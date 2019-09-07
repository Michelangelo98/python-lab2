from sys import argv


def choose_from_menu(scelta,errore):





    close=False



    while not close:

        string = input(scelta)

        if string.isdigit() :
            choose = int(string)
        else:
            choose = 0

        print("\n\n\n")

        if choose >= 1 and choose <= 5:

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

    number_of_occurrence = todo_list.count(to_remove)
    #altternativa: if to_remove in todo_list
    if number_of_occurrence == 0 :

        print("Task not found")

    else:
        #with this for i can remove all occurrences
        for n in range (0,number_of_occurrence):

            todo_list.remove(to_remove)

#I utilize a big amount of memory!
def remove_by_substring() :
    to_remove = input("Task to remove (by substring):")
    remove_list = []

    #utilizzo il for-list per evitare un "out of range"
    for action in todo_list :

        if action.count(to_remove) != 0:
            remove_list.append(action)



    if remove_list.__len__() == 0:
        print("Task not found")
    else:
        for action_to_remove in remove_list:
            todo_list.remove(action_to_remove)







if __name__ == '__main__':


    msg_scelta = """Insert the number corresponding to the action you want to perform: 

    1. insert a new task; 

    2. remove a task; 

    3. show all the tasks; 

    4. close the program.
    
    5. remove task by substring
    """

    msg_errore = "Choose between (1,4)"
    """
    with open(argv[1]) as file_in:
        todo_list = file_in.readlines()

    x="\n"
    todo_list = [x.strip() for x in todo_list]
    """
    #Im enable in using with
    #I have to control if the file was correctly open -> use try statement
    file_in = open(argv[1])

    #I can save a file in a list in a simpler way
    '''
    todo_list = file_in.readlines()

    for number in range(0,todo_list.__len__()) :
        todo_list[number] = todo_list[number].strip("\n")
        
    '''
    todo_list=file_in.read().splitlines()
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

        elif scelta == 5:
            remove_by_substring()

        scelta = choose_from_menu(msg_scelta, msg_errore)


    file_out = open(argv[1], 'w')

    for action in todo_list:
        file_out.write(action + "\n")


    file_out.close()



