from pathlib import Path


def find_name(name_in_url):
    for line in name_in_url.splitlines():
        name = line.split("/")[-1]
        print(name.split("-")[-1])
    return


surnames_file_path = Path("url.txt")
surnames = surnames_file_path.read_text()
find_name(surnames)
