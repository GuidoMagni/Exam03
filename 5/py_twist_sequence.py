def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    k %= len(arr)
    return arr[-k:] + arr[:-k] if k else arr[:]


print(twist_sequence([1,2,3,4,5], 2))
