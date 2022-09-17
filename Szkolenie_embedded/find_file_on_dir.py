import os

def find_files(search_path, filename):
   result = []

# Wlaking top-down from the root
   for e, (root, dir, files) in enumerate(os.walk(search_path)):
        print(e, root, files)
        if filename in files:
            result.append(os.path.join(root, filename))
   return result

print(find_files("C:\\",'chrome.exe'))