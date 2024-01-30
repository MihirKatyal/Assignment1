

def list_directory(path, options):
    files = []
    for root, dirs, filenames in os.walk(path):
        if '-f' in options:
            # Output only files
            files.extend([os.path.join(root, filename) for filename in filenames])
        else:
            # Output files and directories
            files.extend([os.path.join(root, filename) for filename in filenames])
            if '-r' not in options:
                break  # If not recursive, only list the current directory

    if '-s' in options:
        # Filter by file name
        files = [file for file in files if options['-s'] in os.path.basename(file)]

    if '-e' in options:
        # Filter by file extension
        files = [file for file in files if file.endswith(options['-e'])]

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
