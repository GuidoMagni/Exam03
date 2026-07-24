def bracket_validator(s: str) -> bool:
    brack = {')': '(', ']': '[', '}': "{"}
    open = []

    for c in s:
        if c in "([{":
            open.append(c)
        elif c in ")]}":
            if not open or open.pop() != brack[c]:
                return False
    return not open