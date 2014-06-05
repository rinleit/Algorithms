def process_regex(regex):
    return regex.group().split()


def convert_to_int_list(string_list):
    return list(map(int, string_list))