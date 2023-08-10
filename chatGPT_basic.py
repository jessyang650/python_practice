def return_sum(num1, num2):
    return num1 + num2

def return_largest_num1(list1):
    largest_num = list1[0]
    for i in list1:
        if i > largest_num:
            largest_num = i
    return largest_num

def return_largest_num2(list1):
    return max(list1)

def reverse_string1(string1):
    reversed_string = ""
    for i in range(len(string1)-1, -1, -1):
        reversed_string += string1[i]
    return reversed_string

def reverse_string2(string1):
    return string1[::-1]

def return_more_than_5(list_of_words):
    new_list_of_words = []
    for i in list_of_words:
        if len(i) > 5:
            new_list_of_words.append(i)
    return new_list_of_words

def return_list_of_even_nums(list_of_nums):
    list_of_even_nums = []
    for i in list_of_nums:
        if (i % 2 == 0):
            list_of_even_nums.append(i)
    return list_of_even_nums

def return_sum_of_elements(list_of_nums):
    total_sum = 0
    for i in list_of_nums:
        total_sum += i
    return total_sum

def return_mean_of_elements(list_of_nums):
    total_sum = 0
    for i in list_of_nums:
        total_sum += i
    return total_sum / len(list_of_nums)

def return_reversed_list(list_of_nums):
    reversed_list = []
    for i in range(len(list_of_nums) - 1, -1, -1):
        reversed_list.append(list_of_nums[i])
    return reversed_list
