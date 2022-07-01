def number_to_palindrome(number=196, max_steps=10):
    result = [False, 0, [number]]
    if not is_palindrome(number):
        for i in range(1, max_steps + 1):
            result[2].append(reverse_and_add(result[-1][-1]))
            if is_palindrome(result[-1][-1]):
                result[0] = True
                result[1] = i
                break
            else:
                result[1] = i
    else:
        result[0] = True
    return result


def is_palindrome(number):
    number = str(number)
    number_back = number[::-1]
    if number == number_back:
        return True
    else:
        return False


def reverse_and_add(number):
    return number + int(str(number)[::-1])


print(number_to_palindrome())
