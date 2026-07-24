def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    try:
        value = int(number, from_base)
    except (ValueError, TypeError):
        return "ERROR"
    if value == 0:
        return "0"
    while value > 0:
        rem = value % to_base
        value = value // to_base
        result = digits[rem] + result
    return result
