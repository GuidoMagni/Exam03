def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    result = []
    result.extend(list1)
    result.extend(list2)
    result.sort()
    return result