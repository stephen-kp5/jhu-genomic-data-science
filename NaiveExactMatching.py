def naive_exact_match(text: str, pattern: str) -> list[int]:
    """
    Return all starting positions in `text` where `pattern` matches exactly.
    """
    positions = []
    n, m = len(text), len(pattern)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)
        
    return positions

refrence = "ACGTACGTGAC"
read = "ACGT"
print(naive_exact_match(refrence, read))



# Example usage
reference = "ACGTACGTGAC"
read = "ACGT"
print(naive_exact_match(reference, read))
# Output: [0, 4]