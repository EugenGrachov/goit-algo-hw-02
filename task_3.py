def is_balanced(expression):
    stack = []
    opening = "({["
    closing = ")}]"
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack

if __name__ == "__main__":
    test_cases = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }",
        "{[()]}",
        "[(])"
    ]

    for expr in test_cases:
        result = is_balanced(expr)
        print(f"{expr}: {'Симетрично' if result else 'Несиметрично'}")
