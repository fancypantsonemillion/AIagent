from functions.get_files_info import get_files_info

def run_tests():
    # Test 1: Current Directory
    print("get_files_info(\"calculator\", \".\"):")
    print(f"Result for current directory:\n{get_files_info('calculator', '.')}\n")

    # Test 2: Subdirectory
    print("get_files_info(\"calculator\", \"pkg\"):")
    print(f"Result for 'pkg' directory:\n{get_files_info('calculator', 'pkg')}\n")

    # Test 3: Absolute Path Violation
    print("get_files_info(\"calculator\", \"/bin\"):")
    print(f"Result for '/bin' directory: {get_files_info('calculator', '/bin')}\n")

    # Test 4: Traversal Violation
    print("get_files_info(\"calculator\", \"../\"):")
    print(f"Result for '../' directory: {get_files_info('calculator', '../')}\n")

if __name__ == "__main__":
    run_tests()