import os

target_dir = raw_input('Target directory: ').strip()
path, dirs, files = os.walk(target_dir).next()
file_count = len(files)
print "{} files found".format(file_count)
