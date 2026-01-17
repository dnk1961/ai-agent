from functions.write_to_file import write_to_file

#test cases

test_cases = [("lorem.txt", "wait, this isn't lorem ipsum"),("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),("/tmp/temp.txt", "this should not be allowed")]

for path,content in test_cases:
    print(write_to_file("calculator", path, content))