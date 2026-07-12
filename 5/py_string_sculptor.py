def string_sculptor(text: str) -> str:
    result = []
    index = 0
    for char in text:
        if char == " ":
            index = 0
            result.append(char)
        elif char.isalpha():
            result.append(char.upper() if index % 2 else char.lower())
            index += 1
        else:
            result.append(char)
    return "".join(result)

print(string_sculptor("Hello World"))