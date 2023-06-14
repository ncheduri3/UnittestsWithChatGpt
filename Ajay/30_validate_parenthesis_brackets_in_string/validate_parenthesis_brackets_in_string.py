def validate_parenthesis_brackets_in_string(string):
    stack = []

    for char in string:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False

            top = stack.pop()
            if (top == "(" and char != ")") or (top == "[" and char != "]") or (top == "{" and char != "}"):
                return False

    return len(stack) == 0
