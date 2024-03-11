import pandas


def grab_input():
    """Prompts the user to input data and returns it.

    This function waits for the user's input, captures it, and then
    returns the input as a string.

    Returns:
        str: The input provided by the user.
    """
    user_input = input("Please enter something: ")
    return user_input


def read_from_file(path):
    """Reads content from a specified file.

    Opens the file located at 'path', reads its contents, and then
    returns the content as a string.

    Args:
        path (str): The path to the file to be read.

    Returns:
        str: The content of the file.
    """
    with open(path, 'r') as file:
        return file.read()


def read_from_csv_file_with_pandas(path):
    """Reads a file using pandas and returns its content as a DataFrame.

    Utilizes pandas to read a file (typically a CSV or Excel file) specified by
    'path' and returns a pandas DataFrame containing the file's content.

    Args:
        path (str): The path to the file to be read, supported by pandas.

    Returns:
        DataFrame: A DataFrame containing the data read from the file.
    """
    return pandas.read_csv(path)
