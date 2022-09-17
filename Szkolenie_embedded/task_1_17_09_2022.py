import types
import os


def generate_files_by_walk(path, file_extension: str = '.py') -> types.GeneratorType:
    enum = 0
    enum_failed = 0
    for dir_name, subdirs, filenames in os.walk(path):
        for e, filename in enumerate(filenames):
            enum += 1
            if filename.upper() == 'Failed'.upper():
                enum_failed += 1
            yield '{} = {}, {}, {}'.format(enum, enum_failed, type(filename), filename)


def main():
    for file in generate_files_by_walk(r'C:\Users\pmacyszyn_adm\Desktop\Task'):
        print(file)


if __name__ == '__main__':
    main()
