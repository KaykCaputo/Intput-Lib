from typing import Optional

def intput(msg: str, error_msg: str = "Invalid input! Please enter an integer.") -> int:
    """
    Read an integer from user input with a message prompt.

    Parameters:
        msg (str): The prompt message to display.
        error_msg (str, optional): Custom error message if input is invalid.

    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(error_msg)

def intput_range(msg: str, min_val: int, max_val: int,
                 error_msg: Optional[str] = None) -> int:
    """
    Read an integer from user input within a specified range.

    Parameters:
        msg (str): The prompt message to display.
        min_val (int): Minimum acceptable value (inclusive).
        max_val (int): Maximum acceptable value (inclusive).
        error_msg (str, optional): Custom error message if input is invalid or out of range.

    Returns:
        int: The integer entered by the user within the range.
    """
    default_error = f"Invalid input! Please enter an integer between {min_val} and {max_val}."
    if error_msg is None:
        error_msg = default_error

    while True:
        try:
            value = int(input(msg))
            if min_val <= value <= max_val:
                return value
            else:
                print(error_msg)
        except ValueError:
            print(error_msg)

def floatput(msg: str, error_msg: str = "Invalid input! Please enter an float.") -> float:
    """
    Read an float from user input with a message prompt.

    Parameters:
        msg (str): The prompt message to display.
        error_msg (str, optional): Custom error message if input is invalid.

    Returns:
        float: The float entered by the user.
    """
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(error_msg)


