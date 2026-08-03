def build_bad_character_table(pattern: str) -> dict[str, int]:
    """Return the last-occurrence table for the bad character rule."""
    table = {}
    for index, char in enumerate(pattern):
        table[char] = index
    return table


def build_good_suffix_table(pattern: str) -> list[int]:
    """Return the shift table for the good suffix rule."""
    m = len(pattern)
    shift = [0] * (m + 1)
    border_pos = [0] * (m + 1)

    i = m
    j = m + 1
    border_pos[i] = j

    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = border_pos[j]
        i -= 1
        j -= 1
        border_pos[i] = j

    j = border_pos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = border_pos[j]

    return shift


def boyer_moore_match(text: str, pattern: str) -> list[int]:
    """Return all starting positions in `text` where `pattern` matches exactly."""
    positions = []
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))

    bad_char = build_bad_character_table(pattern)
    good_suffix = build_good_suffix_table(pattern)

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            positions.append(s)
            s += good_suffix[0]
        else:
            bad_char_shift = j - bad_char.get(text[s + j], -1)
            good_suffix_shift = good_suffix[j + 1]
            s += max(1, bad_char_shift, good_suffix_shift)

    return positions


if __name__ == "__main__":
    reference = "ACGTACGTGAC"
    read = "ACGT"
    print("Reference:", reference)
    print("Pattern:", read)
    print("Matches:", boyer_moore_match(reference, read))
