def merge_sort(input_list):
    # Divide the list half by half
    if len(input_list) > 1:
        middle = len(input_list) // 2
        left = input_list[middle:]
        right = input_list[:middle]
        print('*'*50)
        print(f'preleft: {left}, preright: {right}')
        # Recursive call to the function until
        # the list cannot be further divided
        merge_sort(left)
        merge_sort(right)
        # Iterators to traverse the sublists
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        # Iterate both lists
        while i < len(left) and j < len(right) and k <= len(input_list):
            if left[i] < right[j]:
                # Change positions
                input_list[k] = left[i]
                i += 1
            else:
                # Keep the order
                input_list[k] = right[j]
                j += 1
            k += 1
        # If the lists cannot be compared simultaneously,
        # copy their sorted contents
        # left
        while i < len(left):
            input_list[k] = left[i]
            i += 1
            k += 1
        # right
        while j < len(right):
            input_list[k] = right[j]
            j += 1
            k += 1
        print(f'left: {left}, right: {right}')
        print(f'list: {input_list}')
        print('*'*50)
    return input_list

if __name__ == "__main__":
    import random
    list_length = 10
    input_list = [random.randint(i,100) for i in range(list_length)]
    print(input_list)
    res = merge_sort(input_list)
    print(res) 