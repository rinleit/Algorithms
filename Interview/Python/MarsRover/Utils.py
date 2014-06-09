def process_regex(regex):
    """
    Return a list of the individual matched fields from a successful regular expression match
    :param regex: Matched regular expression
    :return: List of matched regular expression fields
    """
    return regex.group().split()


def convert_to_int_list(string_list):
    """
    Return a list of integers
    :param string_list: List of Ints as Strings
    :return: List of Ints
    """
    return list(map(int, string_list))