def is_palindrome(n: int) -> bool:
    # Initialize reversed number 'x' with 0 and 'y' with input number
    x, y = 0, n
    while y > 0:
        # Try to reverse input number by taking the remainder of the number
        # divided by 10, added by previous value of 'x' that multiplied
        # by 10, also divide previous value of 'y' by 10, throw away
        # the decimal part
        x, y = (y % 10) + (x * 10), y // 10
    # Returns True if reversed number equals to input number, otherwise False
    return n == x
