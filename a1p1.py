from pathlib import Path

def list_directory(path, options):
    files = []
    for file_path in Path(path).rglob("*"):
        if file_path.is_file():
            files.append(file_path)


    files.sort(key=lambda x: (os.path.isdir(x), x))  # Sort files first, then directories

    for file in files:
        print(file)

def main():
    while True:
        user_input = input("Enter command: ")
        args = user_input.split()
        command = args[0]

        if command == 'Q':
            print("Quitting the program.")
            break
        elif command == 'L':
            if len(args) < 2:
                print("Please provide a directory path.")
                continue

            directory_path = args[1]
            options = {arg: args[i + 1] for i, arg in enumerate(args[2:]) if arg.startswith('-')}

            list_directory(directory_path, options)
        else:
            print("Invalid command. Please use 'L' to list or 'Q' to quit.")

if __name__ == "__main__":
    main()
