def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not isinstance(number, str) or not isinstance(from_base, int) or not isinstance(to_base, int):
        return "ERROR"
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"
    if number == "":
        return "ERROR"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    negative = False
    num = number.upper()
    if num.startswith("-"):
        negative = True
        num = num[1:]
    if num == "":
        return "ERROR"

    value = 0
    for ch in num:
        if ch not in digits[:from_base]:
            return "ERROR"
        value = value * from_base + digits.index(ch)

    if value == 0:
        return "0"

    result = ""
    while value > 0:
        value, rem = divmod(value, to_base)
        result = digits[rem] + result

    if negative:
        result = "-" + result

    return result


print(number_base_converter("G", 16, 10))
