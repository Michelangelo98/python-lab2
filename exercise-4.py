

def find_urgent():

    '''

    '''

    urgent = {}

    for task in tasks.keys():

        if tasks[task]['urgent'] == True:

            urgent[task] = tasks[task]


    print(urgent)





if __name__ == '__main__':

    task1 = {'todo': 'call John for AmI project organization', 'urgent': True}
    task2 = {'todo': 'buy a new mouse', 'urgent': True}
    task3 = {'todo': 'find a present for Angelina’s birthday', 'urgent': False}
    task4 = {'todo': 'organize mega party (last week of April)', 'urgent': False}
    task5 = {'todo': 'book summer holidays', 'urgent': False}
    task6 = {'todo': 'whatsapp Mary for a coffee', 'urgent': True}
    tasks = {'task1': task1,'task2': task2,'task13': task3,'task4': task4,'task5': task5,'task6': task6}


    find_urgent()