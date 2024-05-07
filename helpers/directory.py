def directory_key_values_list(values, custom_keys = []):
    result = []
    i = 0

    for key, val in values.items():
        if len(custom_keys) > 0: 
            result.append([custom_keys[i], val])
            i += 1
        else: result.append([key, val])
        

    return result


def dicrectory_to_list(values):
    value = values.values()
    result = []

    for i in value:
        result.append(i)

    return result


def directory_list_to_list(values, add_number = False):
    result = []
    for i in range(len(values)):
        result.append(dicrectory_to_list(values[i]))
        if add_number:
            result[i].insert(0, i + 1)
    
    return result