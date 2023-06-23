#  Binary search
# Time complexity = Log(n)

def binary_search(list, number_find):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_number = list[mid]
        if mid_number == number_find:
            return mid
        if mid_number < number_find:
            start = mid + 1
        if mid_number > number_find:
            end = mid - 1
    return -1


def binary_search_recursive(list, number_find, start=None, end=None):
    if start == None or end == None:
        end = len(list) - 1
        start = 0

    if end < start:
        return -1

    mid = (start + end) // 2
    if mid >= len(list) or mid < 0:
        return -1
    mid_number = list[mid]

    if mid_number == number_find:
        return mid + 1
    if mid_number < number_find:
        start = mid + 1
    if mid_number > number_find:
        end = mid - 1

    return binary_search_recursive(list, number_find, start, end)


if __name__ == '__main__':
    list = [4, 6, 8, 10, 40, 56, 66, 67, 69, 73, 78, 100, 204]
    number_find = int(input('search this number: '))


index = binary_search_recursive(list, number_find)
print('the location of the number is at ', index)


# find index of all occurences of a number from a list
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:  # this means number is in right hand side of the list
            left_index = mid_index + 1
        else:  # number to find is on left hand side of the list
            right_index = mid_index - 1

    return -1


def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >= 0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i < len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == '__main__':
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15
    indices = find_all_occurances(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")
