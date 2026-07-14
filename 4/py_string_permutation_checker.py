def string_permutation_checker(s1: str, s2: str) -> bool:
    new_s1 = s1.replace(" ", "")
    new_s2 = s2.replace(" ", "")
    return sorted(new_s1) == sorted(new_s2)


print(string_permutation_checker("a gentleman","elegant man"))
