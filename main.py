print("hello world")
def get_longest_str(string1: str, string2: str) -> str:
    """Accepts two strings and returns the longest one"""
    if len(string1) > len(string2):
        the_longest_string = string1
    elif len(string1) < len(string2):
        the_longest_string = string2
    else:
        return string1
    return the_longest_string


def is_list_comprised_solely_of_numbers(the_list: list) -> bool:
    """Returns True if the list consists only of numbers and False otherwise"""
    return all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in the_list)


def output_str() -> None:
    """Outputs a string of the type "'*' * 80" to the console and returns nothing"""
    print('*' * 80)