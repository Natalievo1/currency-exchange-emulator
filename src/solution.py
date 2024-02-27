class Currency:
    currencies = {
        'CHF': 0.930023,  # Swiss Franc
        'CAD': 1.264553,  # Canadian Dollar
        'GBP': 0.737414,  # British Pound
        'JPY': 111.019919,  # Japanese Yen
        'EUR': 0.862361,  # Euro
        'USD': 1.0  # US Dollar
    }

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f"{round(self.value,2)} {self.unit}"
    
    def __str__(self):
        return f"{round(self.value,2)} {self.unit}"

    def __add__(self, other):
        if isinstance(other, (int, float)):  # Directly treat other as USD value
            other_value_in_self_unit = other * self.currencies[self.unit]
            return Currency(self.value + other_value_in_self_unit, self.unit)
        elif isinstance(other, Currency):
            other_value_in_self_unit = (other.value / self.currencies[other.unit] * self.currencies[self.unit])
            return Currency(self.value + other_value_in_self_unit, self.unit)
        else:
            raise TypeError("Unsupported type for addition")

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            # Convert the Currency object to USD before addition
            value_in_usd = self.value / self.currencies[self.unit] * self.currencies["USD"]
            # Perform addition in USD
            result_in_usd = other + value_in_usd
            # Return a new Currency object with the result in USD
            return Currency(result_in_usd, "USD")
        else:
            raise TypeError("Unsupported type for addition")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other_value_in_self_unit = other * self.currencies[self.unit]
            return Currency(self.value - other_value_in_self_unit, self.unit)
        elif isinstance(other, Currency):
            other_value_in_self_unit = (other.value / self.currencies[other.unit] * self.currencies[self.unit])
            return Currency(self.value - other_value_in_self_unit, self.unit)
        else:
            raise TypeError("Unsupported type for subtraction")

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            # Convert the Currency object to USD before addition
            value_in_usd = self.value / self.currencies[self.unit] * self.currencies["USD"]
            # Perform addition in USD
            result_in_usd = other - value_in_usd
            # Return a new Currency object with the result in USD
            return Currency(result_in_usd, "USD")
        else:
            raise TypeError("Unsupported type for subtraction")

    def __iadd__(self, other):
        return Currency.__add__(self, other)

    def __isub__(self, other):
        return Currency.__sub__(self, other)
        
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 
