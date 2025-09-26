from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


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

# -- write file tests

print('\nwrite_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):')
print("Result for lorem.txt:")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print('\nwrite_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):')
print("Result for pkg/morelorem.txt:")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print('\nwrite_file("calculator", "/tmp/temp.txt", "this should not be allowed"):')
print("Result for /tmp/temp.txt (should be blocked):")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

# -- run python file tests

print('\nrun_python_file("calculator", "main.py"):')
print("Result for main.py (should print calculator usage instructions):")
print(run_python_file("calculator", "main.py"))

print('\nrun_python_file("calculator", "main.py", ["3 + 5"]):')
print(
    "Result for main.py with args (should run calculator with nasty rendered result):"
)
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print('\nrun_python_file("calculator", "tests.py"):')
print("Result for tests.py:")
print(run_python_file("calculator", "tests.py"))

print('\nrun_python_file("calculator", "../main.py"):')
print("Result for ../main.py (should return an error):")
print(run_python_file("calculator", "../main.py"))

print('\nrun_python_file("calculator", "nonexistent.py"):')
print("Result for nonexistent.py (should return an error):")
print(run_python_file("calculator", "nonexistent.py"))
