def task2(numbers):
    if len(numbers) < 2:
        return ("Can it nhat 2 so")
    
    max1 = max2 = float('-inf')
    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    return max1 + max2

def test():
    """
    Unit test function for sum_top_two_integers.
    """
    test_cases = [
        ([1, 4, 2, 3, 5], 9),
        ([5, 5, 5, 5], 10),
        ([-1, -2, -3, -4, -5], -3),
        ([1.5, 2.5, 3.5, 4.5], 8),  
    ]
    
    for i, (input_list, expected_output) in enumerate(test_cases):
        try:
            result = task2(input_list)
            print(f"Output: {result}")
            assert result == expected_output, f"Test case {i+1} failed: expected {expected_output}, got {result}"
            print(f"Test case {i+1} passed")
        except Exception as e:
            print(f"Test case {i+1} failed: {str(e)}")

if __name__ == "__main__":
    test()