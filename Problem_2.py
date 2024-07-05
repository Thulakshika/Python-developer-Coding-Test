## Printing the square of the even numbers
def square_evens(numbers: list):
    evens = [number * number for number in numbers if number % 2 == 0]
    return evens

print(square_evens([1, 2, 3, 4, 5]))
