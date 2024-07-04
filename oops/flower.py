class Flower:
    """Flower class"""

    def __init__(self, name: str, petals: int, price: float):
        self._name = name
        self._petals = petals
        self._price = price
    
    def get_price(self):
        return self._price
    
    def get_number_of_petals(self):
        return self._petals
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if price <= 0:
            raise ValueError("Price should be greater than zero.")
        
        self._price = price
        return True
    
    def set_petals(self, petals):
        if petals <= 0:
            raise ValueError("Petals should be greater than zero.")
        
        self._petals = petals
        return True
    
    def change_name(self, name):
        self._name = name
        return True
    
