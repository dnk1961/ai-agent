from functions.get_file_content import get_file_content

#test cases

test_cases = ["lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

for case in test_cases:
    print(get_file_content("calculator", case))