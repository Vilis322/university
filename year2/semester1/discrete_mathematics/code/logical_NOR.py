print(f"{'A':^3}|{'B':^3}|{'A NOR B':^9}|")
print("\n".join(f"{A:^3}|{B:^3}|{int(not (A or B)):^9}|" for A in [0, 1] for B in [0, 1]))
