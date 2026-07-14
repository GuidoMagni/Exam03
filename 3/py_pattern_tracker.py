def pattern_tracker(text: str) -> int:
    count = 0
    prev = "9"
    for a in text:
        if a.isdigit():
            if a > prev:
                count += 1
            prev = a
        else:
            prev = "9"
    return count


print(pattern_tracker("112233"))
