from pathlib import Path


class MyError(Exception):
    def __init__(self, text):
        super().__init__(text)


def user_input(input_message):
    return input(input_message).strip().lower()


def get_numbered_lines(file):
    text = Path(file).read_text()
    i = 1

    for line in text.splitlines():
        print(f".".join([str(i), line]))
        i += 1


def main():
    file_name = user_input(input_message="Enter file name: ")
    try:
        if not file_name.endswith("names.txt"):
            raise MyError("You entered in an invalid file name!")

        get_numbered_lines(file_name)
    except MyError as e:
        print(str(e))


if __name__ == "__main__":
    main()
