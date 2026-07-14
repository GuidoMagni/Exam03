def cryptic_sorter(strings: list[str]) -> list[str]:
    def vowel_count(s: str) -> int:
        return sum(1 for c in s if c.lower() in "aeiou")

    def sort_key(s: str):
        # (length, case-insensitive value, vowel count)
        return (len(s), s.lower(), vowel_count(s))

    def merge(left: list[str], right: list[str]) -> list[str]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            # "<=" (not "<") is what keeps the sort stable:
            # on a tie, the element from `left` (which came first
            # in the original order) is taken first.
            if sort_key(left[i]) <= sort_key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(arr: list[str]) -> list[str]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    return merge_sort(strings)


print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
