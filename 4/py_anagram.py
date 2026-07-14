def anagram(s1: str, s2: str) -> bool:
    new_s1 = s1.lower().replace(" ", "")
    new_s2 = s2.lower().replace(" ", "")
    return sorted(new_s1) == sorted(new_s2)


print(anagram("abc", "abcc"))

# Alternatuve
# def anagram(s1: str, s2: str) -> bool:
#     new_s1 = s1.lower().replace(" ", "")
#     new_s2 = s2.lower().replace(" ", "")
#     if len(new_s1) != len(new_s2):
#         return False
#     for c in new_s1:
#         if new_s1.count(c) != new_s2.count(c):
#             return False
#     return True