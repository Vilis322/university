import pytest
from bank_account import BankAccount, Confirmation


@pytest.fixture
def account():
    return BankAccount(140568, "John", "Doe", -7)


# =============================================================================
# 1. Initialization
# =============================================================================
class TestInitialization:

    def test_initial_balance_is_zero(self, account):
        assert account.get_balance() == 0.0

    def test_account_number(self, account):
        assert account.account_number == 140568

    def test_first_name(self, account):
        assert account.first_name == "John"

    def test_last_name(self, account):
        assert account.last_name == "Doe"

    def test_timezone_offset(self, account):
        assert account.preferred_time_zone_offset == -7


# =============================================================================
# 2. Deposit
# =============================================================================
class TestDeposit:

    def test_deposit_positive_amount(self, account):
        code = account.deposit(500.0)
        assert account.get_balance() == 500.0
        assert code.startswith("D-140568-")

    def test_deposit_multiple_times(self, account):
        account.deposit(100.0)
        account.deposit(250.0)
        assert account.get_balance() == 350.0

    def test_deposit_zero_returns_rejected_code(self, account):
        code = account.deposit(0)
        assert account.get_balance() == 0.0
        assert code.startswith("X-140568-")

    def test_deposit_negative_returns_rejected_code(self, account):
        code = account.deposit(-100.0)
        assert account.get_balance() == 0.0
        assert code.startswith("X-140568-")

    def test_deposit_small_amount(self, account):
        account.deposit(0.01)
        assert account.get_balance() == pytest.approx(0.01)


# =============================================================================
# 3. Withdraw
# =============================================================================
class TestWithdraw:

    def test_withdraw_valid_amount(self, account):
        account.deposit(500.0)
        code = account.withdraw(200.0)
        assert account.get_balance() == 300.0
        assert code.startswith("W-140568-")

    def test_withdraw_entire_balance(self, account):
        account.deposit(500.0)
        code = account.withdraw(500.0)
        assert account.get_balance() == 0.0
        assert code.startswith("W-140568-")

    def test_withdraw_more_than_balance_rejected(self, account):
        account.deposit(100.0)
        code = account.withdraw(200.0)
        assert account.get_balance() == 100.0
        assert code.startswith("X-140568-")

    def test_withdraw_zero_rejected(self, account):
        account.deposit(100.0)
        code = account.withdraw(0)
        assert account.get_balance() == 100.0
        assert code.startswith("X-140568-")

    def test_withdraw_negative_rejected(self, account):
        account.deposit(100.0)
        code = account.withdraw(-50.0)
        assert account.get_balance() == 100.0
        assert code.startswith("X-140568-")

    def test_withdraw_from_zero_balance_rejected(self, account):
        code = account.withdraw(10.0)
        assert account.get_balance() == 0.0
        assert code.startswith("X-140568-")


# =============================================================================
# 4. Interest
# =============================================================================
class TestInterest:

    def test_apply_interest(self, account):
        account.deposit(1000.0)
        code = account.apply_interest()
        assert account.get_balance() == pytest.approx(1005.0)
        assert code.startswith("I-140568-")

    def test_interest_on_zero_balance(self, account):
        account.apply_interest()
        assert account.get_balance() == 0.0

    def test_interest_compounds(self, account):
        account.deposit(1000.0)
        account.apply_interest()
        account.apply_interest()
        expected = 1000.0 * (1 + 0.005) * (1 + 0.005)
        assert account.get_balance() == pytest.approx(expected)


# =============================================================================
# 5. Transaction codes
# =============================================================================
class TestTransactionCodes:

    def test_deposit_code_format(self, account):
        code = account.deposit(100.0)
        parts = code.split("-")
        assert len(parts) == 4
        assert parts[0] == "D"
        assert parts[1] == "140568"

    def test_rejected_deposit_code(self, account):
        code = account.deposit(-1)
        assert code.split("-")[0] == "X"

    def test_withdraw_code_format(self, account):
        account.deposit(500.0)
        code = account.withdraw(100.0)
        assert code.split("-")[0] == "W"

    def test_rejected_withdraw_code(self, account):
        code = account.withdraw(100.0)
        assert code.split("-")[0] == "X"

    def test_interest_code_format(self, account):
        account.deposit(100.0)
        code = account.apply_interest()
        assert code.split("-")[0] == "I"

    def test_transaction_ids_increment(self, account):
        code1 = account.deposit(100.0)
        code2 = account.deposit(200.0)
        id1 = int(code1.split("-")[3])
        id2 = int(code2.split("-")[3])
        assert id2 == id1 + 1


# =============================================================================
# 6. Parse confirmation
# =============================================================================
class TestParseConfirmation:

    def test_parse_deposit_confirmation(self):
        code = "D-140568-20250315145900-124"
        result = BankAccount.parse_confirmation(code, -7)
        assert result.account_number == 140568
        assert result.transaction_code == "D"
        assert result.transaction_id == 124
        assert result.time_utc == "2025-03-15T14:59:00"
        assert result.time == "2025-03-15 07:59:00"

    def test_parse_withdrawal_confirmation(self):
        code = "W-999-20260101120000-001"
        result = BankAccount.parse_confirmation(code, 0)
        assert result.account_number == 999
        assert result.transaction_code == "W"
        assert result.transaction_id == 1
        assert result.time_utc == "2026-01-01T12:00:00"
        assert result.time == "2026-01-01 12:00:00"

    def test_parse_with_positive_timezone(self):
        code = "I-555-20260601080000-010"
        result = BankAccount.parse_confirmation(code, 3)
        assert result.time_utc == "2026-06-01T08:00:00"
        assert result.time == "2026-06-01 11:00:00"

    def test_parse_rejected_transaction(self):
        code = "X-123-20260315100000-005"
        result = BankAccount.parse_confirmation(code, -5)
        assert result.transaction_code == "X"
        assert result.time == "2026-03-15 05:00:00"

    def test_confirmation_is_frozen(self):
        code = "D-140568-20250315145900-124"
        result = BankAccount.parse_confirmation(code, 0)
        with pytest.raises(AttributeError):
            result.account_number = 999

    def test_parse_invalid_format_raises(self):
        with pytest.raises(ValueError):
            BankAccount.parse_confirmation("invalid", 0)


# =============================================================================
# 7. Edge cases
# =============================================================================
class TestEdgeCases:

    def test_deposit_then_withdraw_then_deposit(self, account):
        account.deposit(1000.0)
        account.withdraw(400.0)
        account.deposit(200.0)
        assert account.get_balance() == 800.0

    def test_interest_after_withdrawal(self, account):
        account.deposit(1000.0)
        account.withdraw(500.0)
        account.apply_interest()
        assert account.get_balance() == pytest.approx(500.0 * 1.005)

    def test_large_deposit(self, account):
        account.deposit(1_000_000.0)
        assert account.get_balance() == 1_000_000.0

    def test_very_small_deposit(self, account):
        account.deposit(0.001)
        assert account.get_balance() == pytest.approx(0.001)
