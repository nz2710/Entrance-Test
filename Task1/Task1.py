def task1(strings):
    if not strings:
        return []
    length_freq = {}
    for s in strings:
        length = len(s)
        if length in length_freq:
            length_freq[length] += 1
        else:
            length_freq[length] = 1
    
    max_freq = 0
    most_common_length = 0
    for length, freq in length_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_common_length = length

    return [s for s in strings if len(s) == most_common_length]

def test():
    test_cases = [
        (["a", "ab", "abc", "cd", "def", "gh"], ["ab", "cd", "gh"]),
        (["a", "b", "c", "de"], ["a", "b", "c"]),
        (["hello", "world", "python", "code"], ["hello", "world"]),
    ]
    
    for i, (input_strings, expected_output) in enumerate(test_cases):
        result = task1(input_strings)
        print(f"\nTest case {i + 1}:")
        print(f"Input: {input_strings}")
        print(f"Output: {result}")
        assert result == expected_output, f"Test case {i + 1} failed: expected {expected_output}, got {result}"
        print(f"Test case {i + 1} passed")

# Chạy kiểm tra
if __name__ == "__main__":
    test()
    print("All test cases passed!")