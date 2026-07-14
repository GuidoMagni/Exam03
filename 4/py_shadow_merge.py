def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    result = []
    for a in list1:
        result.append(a)
    for b in list2:
        result.append(b)
    result.sort()
    return result


print(shadow_merge([1,1,2], [1,3,3]))
