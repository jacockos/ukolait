def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(n):
    return n % 2 == 0

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return " ".join(word.capitalize() for word in s.split())

def max_of_list(lst):
    return max(lst)

def min_of_list(lst):
    return min(lst)

def average(lst):
    return sum(lst) / len(lst)
