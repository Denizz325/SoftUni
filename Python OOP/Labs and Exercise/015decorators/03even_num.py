def even_numbers(function):
    def wrapper(numbers):
        result = function([num for num in numbers if num % 2 == 0])
        return result

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
