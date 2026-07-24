def string_sculptor(text: str) -> str:
    i = 0
    result = []
    for c in text:
        if c == ' ':
            i = 0
            result.append(c)
        elif c.isalpha():
            if i % 2:
                result.append(c.upper())
            else:
                result.append(c.lower())
            i += 1
        else:
            result.append(c)
    return "".join(result)