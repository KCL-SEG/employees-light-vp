"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly, contract_hrs, rate, commission_Contract , commission_perContract, commission_bonus, total_pay = 0):
        self.name = name
        self.monthly = monthly
        self.contract_hrs = contract_hrs
        self.rate = rate
        self.commission_Contract = commission_Contract
        self.commission_perContract = commission_perContract
        self.commission_bonus = commission_bonus
        self.total_pay = total_pay
    def get_pay(self):
        self.total_pay = self.monthly + (self.contract_hrs * self.rate) + (self.commission_Contract* self.commission_perContract) + self.commission_bonus
        return self.total_pay
    def __str__(self):
        if self.monthly:
            self.name = f'{self.name} works on a monthly salary of {self.monthly}'
        if self.contract_hrs:
            self.name = f'{self.name} works on a contract of {self.contract_hrs} hours at {self.rate}/hour'
        if self.commission_Contract:
            self.name = self.name + f' and receives a commission for {self.commission_Contract} contract(s) at {self.commission_perContract}/contract'
        if self.commission_bonus:
            self.name = self.name + f' and receives a bonus commission of {self.commission_bonus}'
        self.name = self.name +  f'.  Their total pay is {self.total_pay}.'
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 100, 25, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000, 0, 0, 4, 200, 0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 150, 25, 3, 220, 0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 0, 0, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 120, 30, 0, 0, 600)
