print(f"{'A':^3}|{'B':^3}|{'A NAND B':^10}|")
print("\n".join(f"{A:^3}|{B:^3}|{int(not (A and B)):^10}|" for A in [0, 1] for B in [0, 1]))
