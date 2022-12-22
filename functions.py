def get_todos(filepath="todos.txt"):
    """Read a text file and returns a to-do list"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath="todos.txt"):
    """Overwrites the previous text file and add a new
    todos in the text file
    """
    file = open(filepath, "w")
    file.writelines(todos_arg)
    file.close()


if __name__ == "__main__":
    print("Hello from functions")

