def kaprekize(number):
    """ Repeatedly performs the operation needed to get to Kaprekar's constant.

        This only works on a 4-digit number with at least 2 distinct digits.

        Args:
            number: The number to start the process with

        Returns:
            6174, Kaprekar's constant
    """
    if number != 6174:
        # splitting the digits into an array
        digits = split_digits(number)

        # adding 0 at the front if number is 3 digits
        if number < 1000:
            digits.insert(0, 0)

        # putting digits in descending order
        digits.sort()
        digits.reverse()

        # getting the digits in ascending order
        reversed = digits.copy()
        reversed.reverse()

        # converting back to integers
        digits = join_digits(digits)
        reversed = join_digits(reversed)

        # getting the next number
        result = digits - reversed

        # displaying the operation
        display(digits, reversed, result)

        # repeating process
        return kaprekize(result)
    else:
        # we hit kaprekar's constant
        return 6174

def display(top, bottom, result):
    """ Displays the results of one subtraction/operation.

        Args:
            top: The number in descending order
            bottom: The number in ascending order
            result: The result of the operation
    """
    # checking if the bottom is a 3 digit number
    pad = "0" if bottom < 1000 else ""
    # creating output string
    output = "\n  " + str(top) + "\n- " + pad + str(bottom) + "\n ------\n  " + str(result) + "\n"
    # printing to console
    print(output)

def repeats(number):
    """ Checks if a 4-digit number has at least 2 distinct digits.

        Args:
            number: The number to check

        Returns:
            True if it only has repeating digits,
            False if it has at least 2 distinct digits
    """
    digits = split_digits(number)
    return [digit1 != digit2 for digit1 in digits for digit2 in digits].count(True) < 2

def split_digits(number):
    """ Splits an integer into an array of single digits.

        Args:
            number: The number to split

        Returns:
            An array of integers that are the digits in number
    """
    return [int(digit) for digit in list(str(number))]

def join_digits(digits):
    """ Joins an array of digits into a single integer

        Args:
            digits: The array to join together

        Returns:
            An integer that is the digits joined together
    """
    return int("".join([str(digit) for digit in digits]))

def main():
    """ Quick implementation that grabs a number from the user and starts the process
        of getting Kaprekar's constant.
    """
    num = int(input("\nPlease enter a number to kaprekize: "))

    if repeats(num):
        print("\nError: number must have at least two distinct digits.\n")
    else:
        kaprekize(num)

        print("\nDone!\n")
    
if __name__ == "__main__":
    main()
