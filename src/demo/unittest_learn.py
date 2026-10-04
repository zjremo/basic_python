import unittest
from unittest.mock import patch
import requests

class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
    def get_interest_rate(self):
        url = "https://api.interest-rate.com/interest-rate"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("rate")
        else:
            raise Exception("Failed to get interest rate")

    def __str__(self):
        return f"BankAccount(balance={self.balance})"

class TestBankAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
    
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self):
        self.account = BankAccount(100)
    
    def tearDown(self) -> None:
        print("tearDown")
    
    def test_create_account(self):
        self.assertIsInstance(self.account, BankAccount)

        with self.assertRaises(ValueError):
            BankAccount(-100)
    
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150, msg="Balance should be 150")

        with self.assertRaises(ValueError):
            self.account.deposit(-50)
    
    def test_get_interest_rate(self):
        # 使用patch.object来模拟requests.get
        with patch.object(requests, "get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {"rate": 0.05}
            self.assertEqual(self.account.get_interest_rate(), 0.05)

if __name__ == "__main__":
    unittest.main()