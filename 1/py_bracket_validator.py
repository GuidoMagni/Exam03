def bracket_validator(s: str) -> bool:
    brackets = {')': '(', ']': '[', '}': '{'}
    open = []
    for c in s:
        if c in '([{':
            open.append(c)
        elif c in ')]}':
            if not open or open.pop() != brackets[c]:
                return False
    return not open


print(bracket_validator("([)]"))
