import re
from collections import deque

def is_palindrome():
    d = deque()
    user_input = input("Enter a string to check if it's a palindrome: ")

    cleaned = re.sub(r'[^a-zA-Z0-9]', '', user_input).lower()

    for char in cleaned:
            if char.isalnum():
                d.append(char)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return "It's not a palindrome."
    return "It's a palindrome."

def main():
    result = is_palindrome()
    print(result)


if __name__ == "__main__":
    main()

# Strings to test the function:
#     "A man a plan a canal Panama",
#     "racecar",
#     "Python",
#     "Madam In Eden I'm Adam",
#     "Was it a car or a cat I saw?",
#     "No lemon no melon"
