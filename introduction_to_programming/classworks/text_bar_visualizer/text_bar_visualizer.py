from pathlib import Path


def main():
    file_path = Path('text.txt')
    lines = file_path.read_text().splitlines()
    new_lines = [f"{index + 1}: {'*' * int(line)}" if line.isdigit() else f"{index + 1}:" for index, line in enumerate(lines)]

    for i in new_lines:
        print(i)


if __name__ == "__main__":
    main()
