""" 
        abstraction referes to breaking down a complex problem into fundamentals.
        class is the primary means of abstraction in oop.
        class will have data members(attributes) and member function(methods).

    """
from datetime import datetime, timedelta

class CreditCard:
    EXPIRE_WINDOW = 365
    
    def __init__(self, customer, bank, account, limit):
        """Create a new credit card instance

        Initial balance is set zero

        customer -> the name of the customer
        bank -> the name of the bank
        account -> the account number
        limit -> credit limit (measured in rupeer)
        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._credit_used = 0
        self._last_updated = datetime.date()
        self._transaction_history = []
        self._last_renewed_on = datetime.date()
    
    def get_customer(self):
        """Returns the name of the custmer"""
        return self._customer
    
    def get_bank(self):
        """Return the bank assosciated with the credit card"""
        return self._bank
    
    def get_account(self):
        """Return the account assosciated with the credit card"""
        return self._account
    
    def get_limit(self):
        """Return the limit for the credit card"""
        return self._limit
    
    def get_used_credit(self):
        """Return the credit used"""
        return self._credit_used

    def pay(self, amount, merchant):
        """Make payment using credit card
        
        Total credit used should not exceed the limit.
        Generate a transaction history

        returns
        Bool -> status of payment.

        """

        if (self._credit_used + amount) > self._limit:
            return False
        
        self._credit_used += amount
        self._transaction_history.append(
            self._generate_transaction_log(amount, merchant)
        )
        return True

    
    def update_limit(self, new_limit):
        """Update the existing limit
        
        Credit card can be updated only once in 60 days

        returns 
        Bool -> Status of update
        """
        current_date = datetime.date()
        if current_date - self._last_updated <= timedelta(days=60):
            return False

        self._limit = new_limit
        self._last_updated = current_date
        return True
    
    def _generate_transaction_log(amount, merchant):
        return {
            "date": datetime.date(),
            "time": datetime.time(),
            "credit_used": amount,
            "merchant": merchant
        }
    


class HDFCPremiumCreditCard(CreditCard):
    BANK_NAME = "HDFC BANK"
    LIMIT = 200000
    def __int__(self, customer, account):
        super().__init__(customer, BANK_NAME, account, LIMIT)