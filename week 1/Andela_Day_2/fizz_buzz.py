enter_number = int(input("enter a number that is a multiple of  3 or 5: "))


def fizzBuzz(enter_number):
    if (enter_number <= 0):
        return "Number must be greater than zero"

    elif (enter_number % 5 == 0):
        return 'Buzz'

    elif (enter_number % 3 == 0):
        return 'Fizz'

    elif (enter_number % 3 == 0 & enter_number % 5 == 0):
        return 'FizzBuzz'

    else:
        return str(enter_number) + (" This number is not a multiple of 3 or 5")


print(fizzBuzz(enter_number))

