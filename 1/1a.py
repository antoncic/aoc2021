import pytest

def get_data(data_file_path):
    data = []
    with open(data_file_path, 'rb') as file:
        data = [int(line) for line in file]
    return data

def number_of_increasing_depth(data_file_path):
    data = get_data(data_file_path)
    number_of_increasing = 0
    for i in range(len(data)-1):
        a = data[i]
        b = data[i+1]
        if (a < b):
            number_of_increasing += 1
    return number_of_increasing

print(number_of_increasing_depth("input.txt"))

##### Tests ####

def test_get_data():
    data = get_data("test-input.txt")
    sum = 0
    for element in data:
        sum = sum + element
    assert sum == 2256

def test_number_of_increasing():
    assert number_of_increasing_depth("test-input.txt") == 7
