def reverse_end_and_concatenate(numbers1, numbers2):
    if len(numbers2) > 2:   
        numbers2.reverse()
    return numbers1 + numbers2

def split_list(numbers, position):
    return (numbers[:position], numbers[position:])

def exchange_numbers(numbers, position):
    lhs_position = position-1
    lhs_value = numbers[lhs_position]
    i = len(numbers)
    potential = None 
    while(lhs_position < i):
        i -= 1
        if numbers[i] > lhs_value:
            if potential is None:
                potential = i
            else:
                if numbers[i] < numbers[potential]:
                    potential = i
    numbers[lhs_position] = numbers[potential]
    numbers[potential] = lhs_value
    return numbers

def find_less_than(numbers):
    position = len(numbers)-1
    while(position > 0):
        if numbers[position-1] < numbers[position]:
            return position
        position -= 1
    return position


def set_up_list(n):
    list_of_numbers = []
    count = 1
    for i in range(n):
       list_of_numbers.append(count) 
       count += 1
    return list_of_numbers

def algorithm_one(n):
    count = 1
    numbers = set_up_list(n)
    print(count, numbers) #We need to print our starting list before we start organizing
    position = None
    while(True):
        position = find_less_than(numbers)
        if position == 0:
            return
        numbers = exchange_numbers(numbers, position)
        numbers1, numbers2 = split_list(numbers, position)
        numbers = reverse_end_and_concatenate(numbers1, numbers2)
        count += 1
        print(count, numbers)

def main():
    valid_value = False
    while(valid_value == False):
        value = input("Enter your n (in range 1-9): ")
        value = int(value)
        if 0 < value and value < 10:
            valid_value = True
    algorithm_one(value)
    

main()
