import os

f_types = input(
    "Add the file extensions to find and count (example: .txt .docx .pptx):"
)

f_types = f_types.split(" ")

# Get partitions and periferals


path = r"c:" + os.environ["HOMEPATH"] + r"\\Desktop"

print("Scanning the desktop and it's sub-folders to find specified file types.")

count = 0
for d_path, d_names, f_names in os.walk(path):
    for name in f_names:
        _, extension = os.path.splitext(d_path + name)
        if extension in f_types:
            count += 1
            print(name)

print()
print(f"Done scanning. Found {count} files")

input()
