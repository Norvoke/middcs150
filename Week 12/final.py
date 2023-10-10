def keep_val(a_list, val):
    while len(a_list) != 0:
        if a_list[0] != val:
            del a_list[0]
            keep_val(a_list, val)
        if a_list[0] == val:
            return keep_val(a_list, val)
    return []