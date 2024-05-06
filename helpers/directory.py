def directory_key_values_list(values):
    result = []

    for key, val in values.items():
        result.append([key, val])

    return result


def dicrectory_to_list(values):
    results = values.items()
    for i in range(len(results)):
        results[i].insert(0, i)

    return results