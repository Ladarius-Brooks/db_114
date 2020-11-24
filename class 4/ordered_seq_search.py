def seq_search(array, element):
    position = 0
    found = False
    stopped = False
    while position < len(array) and not found:
        print(array[position])
        if array[position] == element:
            found = True
        else:
            if array[position] > element:
                stopped = True
            position += 1
        return found