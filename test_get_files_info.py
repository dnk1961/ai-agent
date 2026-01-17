from functions.get_files_info import get_files_info

#test cases

test_cases = [".", "pkg", "/bin", "../"]

for case in test_cases:
    if case == ".":
        print("Result for current directory")
    else:
        print(f"Result for '{case}' directory:")
    print(get_files_info("calculator", case))