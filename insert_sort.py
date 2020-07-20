def insert_sort(input_list):
    for i in range(len(input_list)):
        current_value = input_list[i]
        current_position = int(i)
        while current_position > 0 and input_list[current_position - 1] > current_value:
            # Aqui sobre-escribimos nuestro elemento actual
            input_list[current_position] = input_list[current_position - 1]
            current_position -= 1
            print(input_list)
        # Aca ponemos el elemento actual en la posicion anterior
        input_list[current_position] = current_value
    return input_list

if __name__ == "__main__":
    import random
    input_list = [random.randint(i,100) for i in range(10)]
    print(input_list)
    res = insert_sort(input_list)
    print(res)