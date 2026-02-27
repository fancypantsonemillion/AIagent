from functions.get_file_content import get_file_content

def run_tests():
    # Test 1: Truncation Check (lorem.txt should be > 10k chars)
    print("Testing lorem.txt truncation:")
    result = get_file_content("calculator", "lorem.txt")
    print(f"Content length: {len(result)}")
    print(f"Ends with truncation message: {'truncated' in result}\n")

    # Test 2: Standard File
    print("get_file_content('calculator', 'main.py'):")
    print(f"{get_file_content('calculator', 'main.py')[:100]}...\n")

    # Test 3: Subdirectory File
    print("get_file_content('calculator', 'pkg/calculator.py'):")
    print(f"{get_file_content('calculator', 'pkg/calculator.py')[:100]}...\n")

    # Test 4: Security Violation
    print("get_file_content('calculator', '/bin/cat'):")
    print(f"{get_file_content('calculator', '/bin/cat')}\n")

    # Test 5: Missing File
    print("get_file_content('calculator', 'pkg/does_not_exist.py'):")
    print(f"{get_file_content('calculator', 'pkg/does_not_exist.py')}\n")

if __name__ == "__main__":
    run_tests()
