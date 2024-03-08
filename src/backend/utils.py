def is_list_of_strings(lst):
    return (bool(lst) and not isinstance(lst, str) and all(isinstance(elem, str) for elem in lst)) or lst == []
    