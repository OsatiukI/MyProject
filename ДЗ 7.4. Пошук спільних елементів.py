def common_elements():
    first_list =  set(range(0, 99, 3))
    second_list = set(range(0, 99, 5))
    result = first_list.intersection(second_list)
    print(result)
    return result


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
