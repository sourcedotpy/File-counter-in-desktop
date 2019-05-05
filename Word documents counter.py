import os

count = 0

path = r"c:" + os.environ["HOMEPATH"] + r"\\Desktop"

print("Scanning the desktop and it's sub-folders to find word documents.")
print("Scanning: ")

for d_path, d_names, f_names in os.walk(path):
    for name in f_names:
        _, extension = os.path.splitext(d_path + name)
        if extension == ".docx" or extension == ".doc" or extension == ".odt":
            count += 1
            print(name)

print()
print(f"Done scanning. Found {count} documents")

input()
