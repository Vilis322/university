from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass(frozen=True)
class Confirmation:
    account_number: int
    transaction_code: str
    transaction_id: int
    time_utc: str
    time: str


class BankAccount:
    interest_rate: float = 0.005
    _tx_counter: int = 0

    @classmethod
    def _next_tx_id(cls) -> int:
        cls._tx_counter += 1
        return cls._tx_counter

    @staticmethod
    def _utc_timestamp() -> str:
        return datetime.utcnow().strftime("%Y%m%d%H%M%S")

    def _make_code(self, type_code: str, tx_id: int) -> str:
        ts = self._utc_timestamp()
        return f"{type_code}-{self.account_number}-{ts}-{tx_id:03d}"

    def __init__(self, account_number: int, first_name: str, last_name: str, preferred_time_zone_offset: int):
        self.account_number: int = account_number
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.preferred_time_zone_offset: int = preferred_time_zone_offset
        self._balance: float = 0.0

    def get_balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> str:
        tx_id = self._next_tx_id()
        if amount > 0:
            self._balance += amount
            return self._make_code("D", tx_id)
        return self._make_code("X", tx_id)

    def withdraw(self, amount: float) -> str:
        tx_id = self._next_tx_id()
        if 0 < amount <= self._balance:
            self._balance -= amount
            return self._make_code("W", tx_id)
        return self._make_code("X", tx_id)

    def apply_interest(self) -> str | float:
        tx_id = self._next_tx_id()
        interest = self._balance * BankAccount.interest_rate
        self._balance += interest
        return self._make_code("I", tx_id)

    @staticmethod
    def parse_confirmation(confirmation_code: str, timezone_offset: int) -> Confirmation:
        """"""
        type_code, acc_num, ts_str, tx_id = confirmation_code.split("-")

        dt_utc = datetime.strptime(ts_str, "%Y%m%d%H%M%S")
        dt_local = dt_utc + timedelta(hours=timezone_offset)

        return Confirmation(
            account_number=int(acc_num),
            transaction_code=type_code,
            transaction_id=int(tx_id),
            time_utc=dt_utc.strftime("%Y-%m-%dT%H:%M:%S"),
            time=dt_local.strftime("%Y-%m-%d %H:%M:%S"),
        )

code = "D-140568-20250315145900-124"
result = BankAccount.parse_confirmation(code, -7)
print(result.account_number)      # 140568
print(result.time_utc)            # 2019-03-15 14:59:00
print(result.time)                # 2019-03-15 07:59:00 (MST)