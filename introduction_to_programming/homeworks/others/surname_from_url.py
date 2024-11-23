class InvalidInput(Exception):
    pass


def main():
    url = input("Enter the url: ").strip().lower()
    try:
        if not url.startswith("https://oigus.ut.ee/et/tootaja/"):
            raise InvalidInput("You entered invalid url!")

        username = url.split("/")[-1]
        surname = username.split("-")[-1]
        return f"Surname is {surname.capitalize()}"
    except InvalidInput as e:
        print(str(e))


if __name__ == "__main__":
    print(main())
