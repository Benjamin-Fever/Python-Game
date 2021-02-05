def sort_draw_hierarchy(array):
    while True:
        count = 0
        for i in range(0, len(array) - 1):
            if array[i].depth > array[i + 1].depth:
                num1 = array[i]
                num2 = array[i + 1]
                array[i] = num2
                array[i + 1] = num1
            else:
                count += 1
        if count >= len(array) - 1:
            break
    return array

