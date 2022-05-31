import os


files_to_process = [
    r"023-code expansion\S01-L014__exec_task_file\math_sin_square.py",
    r"023-code expansion\S01-L014__exec_task_file\math_square_root.py"
    ]


basename = os.path.basename(files_to_process[0]) # math_sin_square.py


for num, file_path in enumerate(files_to_process):

    with open(file_path, 'r') as f:
        print("{} - Flie: {}".format(num + 1, os.path.basename(file_path)))
        print("Result:")
        source = f.read()
        exec(source)
        print()


