def cryptic_sorter(strings: list[str]) -> list[str]:
    def vowel_count(s: str) -> int:
        return sum(1 for c in s if c in "aeiou")

    def sort_key(s: str):
        return len(s), s.lower(), vowel_count(s)

    def merge(left: list[str], right: list[str]) -> list[str]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if sort_key(left[i]) < sort_key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(s: list[str]) -> list[str]:
        if len(s) <= 1:
            return s
        mid = len(s) // 2
        left = merge_sort(s[:mid])
        right = merge_sort(s[mid:])
        return merge(left, right)

    return merge_sort(strings)