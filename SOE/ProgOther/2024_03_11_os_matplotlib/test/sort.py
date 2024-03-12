import os
import shutil

os.chdir("test")
directory = os.getcwd()
content = os.listdir(".")
print(directory)
print(content)

extensions = []
for item in content:
    if os.path.isfile(item):
        extensions.append(item.split(".")[-1])

extensions = set(extensions)
print(extensions)

if "organized" not in content:
    os.mkdir("organized")

for extension in extensions:
    new_directory = os.path.join("organized", extension)
    print(new_directory)
    os.mkdir(new_directory)

for item in content:
    if os.path.isfile(item):
        ext = item.split(".")[-1]
        target_directory = os.path.join("organized", ext)
        shutil.copy(item,target_directory)
    