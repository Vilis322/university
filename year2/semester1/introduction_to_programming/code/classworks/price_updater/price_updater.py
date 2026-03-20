from pathlib import Path


def main():
    file_data = Path("prices.txt").read_text().splitlines()
    new_file = Path("new_prices.txt")

    new_file.write_text("")

    with new_file.open('a') as new_data_file:
        for product_line, price_line in zip(file_data[::2], file_data[1::2]):
            if price_line.isdigit():
                new_price = float(price_line) - 0.01
                new_data_file.write(f"{product_line}\n{new_price:.2f}\n")
                print(f"{product_line} OK!")
            else:
                print(f"Could not convert the price of '{product_line}'.")


if __name__ == "__main__":
    main()
