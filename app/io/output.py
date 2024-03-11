def print_to_console(message):
    """Prints a given message to the console.

    Takes a string 'message' and prints it to the standard output (console).

    Args:
        message (str): The message to be printed to the console.
    """
    print(message)


def write_to_file(path, content):
    """Writes the given content to a file specified by 'path'.

    Opens or creates a file at the path specified by 'path' and writes
    the 'content' to it. If the file already exists, its content will be
    overwritten.

    Args:
        path (str): The path to the file where the content will be written.
        content (str): The content to write to the file.
    """
    with open(path, 'w') as file:
        file.write(content)
