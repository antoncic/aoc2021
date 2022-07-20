import pytest

def get_data(data_file_path):
    data = []
    with open(data_file_path, 'rb') as file:
        data = [int(line) for line in file]
    return data

def number_of_increasing_windows(data_file_path):
    data = get_data(data_file_path)
    number_of_increasing = 0
    for i in range(len(data)-3):
        current_window = data[i] + data[i+1] + data[i+2]
        next_window = data[i+1] + data[i+2] + data[i+3]
        if (current_window < next_window):
            number_of_increasing += 1
    return number_of_increasing



print(number_of_increasing_windows("input.txt"))

##### Tests ####

def test_get_data():
    data = get_data("test-input.txt")
    sum = 0
    for element in data:
        sum = sum + element
    assert sum == 2256

def test_number_of_increasing_windows():
    assert number_of_increasing_windows("test-input.txt") == 5
