from functions.get_file_content import get_file_content


# -- file content tests

print('get_file_content("calculator", "lorem.txt"):')
print("Result for lorem.txt (should truncate):")
result = get_file_content("calculator", "lorem.txt")
print(f"Length: {len(result)}")
print(result)

print('\nget_file_content("calculator", "main.py"):')
print("Result for main.py:")
print(get_file_content("calculator", "main.py"))

print('\nget_file_content("calculator", "pkg/calculator.py"):')
print("Result for pkg/calculator.py:")
print(get_file_content("calculator", "pkg/calculator.py"))

print('\nget_file_content("calculator", "/bin/cat"):')
print("Result for /bin/cat (should return an error string):")
print(get_file_content("calculator", "/bin/cat"))

print('\nget_file_content("calculator", "pkg/does_not_exist.py"):')
print("Result for pkg/does_not_exist.py:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
