def binary_search(input_list, start, end, query):
    if start >= end:
        return False
    half = (start + end) // 2
    if query == input_list[half]:
        return True
    elif query > input_list[half]:
        start = half
        return binary_search(input_list[start:], start, len(input_list[start:]), query)
    else:
        end = half
        return binary_search(input_list[:half], start, len(input_list[:half]), query)

if __name__ == "__main__":
    import random
    size = 25
    input_list = sorted([random.randint(0,100) for i in range(size)])
    # input_list = [1, 6, 7, 16, 17, 20, 21, 22, 23, 23, 44, 45, 49, 58, 62, 63, 65, 69, 70, 72, 78, 79, 85, 86, 91]
    query = 25
    print(input_list)
    print(binary_search(input_list, 0, len(input_list), query))
