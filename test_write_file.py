from functions.write_file import write_file

def run_tests():
    # Test 1: Overwriting an existing file
    print("Testing overwrite of lorem.txt:")
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result: {result1}\n")

    # Test 2: Writing to a new file in a subdirectory (requires makedirs)
    print("Testing write to a new subdirectory file:")
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result: {result2}\n")

    # Test 3: Security Violation (outside the sandbox)
    print("Testing restricted path:")
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result: {result3}\n")

if __name__ == "__main__":
    run_tests()
