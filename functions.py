FILEPATH = "TodoList.txt"

def get_todos(filepath=FILEPATH):
    """ This is used read the txt content and write to a list """
    with open(filepath, 'r') as file_local:
        todoList_local = file_local.readlines()
    return todoList_local


def write_todos(todoList_arg, filepath=FILEPATH):
    """ Writes to-do items to file """
    with open(filepath, 'w') as file:
        file.writelines(todoList_arg)

