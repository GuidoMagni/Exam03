def anagram(s1: str, s2: str) -> bool:
    new_s1 = [c for c in s1.replace(" ", "").lower()]
    new_s2 = [c for c in s2.replace(" ", "").lower()]
    return sorted(new_s1) == sorted(new_s2)