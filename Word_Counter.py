def word_counter(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"File: {filepath} has {word_count} words\n")

    except FileNotFoundError:
        print(f"Error: The file {filepath} could not be found.\n")
    except PermissionError:
        print(f"Error: You do not have the permission to read The file {filepath}.\n")
    except Exception as e:
        print(f"Error: {e}\n")

filename = input(f"Enter the filename (eg: algebra.txt): ").strip()
word_counter(filename)