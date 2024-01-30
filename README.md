# File Management Tool

This is an interactive command-line file management tool that allows users to inspect, create, delete, and read files in a directory. The program is designed to be cross-platform, supporting both Windows and Posix file systems.

## Usage

The user input for this program takes the following format:

### Commands

- **L**: List the contents of the specified directory.
- **Q**: Quit the program.
- **C**: Create a new file in the specified directory.
- **D**: Delete a file.
- **R**: Read the contents of a file.

### Options for 'L' command

- **-r**: Output directory content recursively.
- **-f**: Output only files, excluding directories in the results.
- **-s [SEARCH_TERM]**: Output only files that match the given file name.
- **-e [FILE_EXTENSION]**: Output only files that match the given file extension.

## Features

### Creating a New File

- To create a new file, use the 'C' command with the '-n' option:
