import os
import psutil

f_types = input("Add the file extensions to find and count (example: .txt .docx .pptx):")
f_types = f_types.split(" ")

# Get partitions and periferals
partitions = []
for partition in psutil.disk_partitions():
    partitions.append(partition.__getattribute__('mountpoint'))
# print(partitions)

for mount in partitions:
    path = mount[:-1] + os.environ["HOMEPATH"] + r"\Desktop" if mount == 'C:\\' else mount

    count = 0
    for d_path, d_names, f_names in os.walk(path):
        for name in f_names:
            _, extension = os.path.splitext(d_path + name)
            if extension in f_types:
                count += 1
                print(d_path + '\\' + name)

print()
print(f"Done scanning. Found {count} files")
