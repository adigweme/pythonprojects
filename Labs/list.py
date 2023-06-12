def sum_of_list(list):
    """
    Find the sum of all values in a given list.
    :param list: a list passed from a prior function
    :return: return the sum of all values in param list
    """
    sum = 0.0
    for i in list:
        sum = sum + i
    return sum