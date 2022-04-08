"""Classes for melon orders."""
from random import choice
import datetime

class AbstractMelonOrder:
    """Super class of Melon orders"""

    shipped = False

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax 
        # self.country_code = country_code 
        # self.shipped = False

    # @staticmethod
    def get_base_price(self):
        """Calculate splurge base pricing"""

        base_price = choice(range(5,10)) 
        # time = datetime.time()
        # now = datetime.datetime.now()

        # # Is it rush hour?
        # if now.hour >= 8 and now.hour <= 11 and now.weekday() < 5:
        #     base_price += 4

    
        order_time = datetime.datetime.now()
        day_of_week = datetime.datetime.weekday(order_time)

        if (day_of_week < 5) and (order_time.hour >= 8 and order_time.hour <= 11): 
                base_price += 4

        return base_price 

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        # total = (1 + self.tax) * self.qty * base_price
        
        if self.species == 'Christmas melon':
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'International' and self.qty < 10:
            total += 3
            
        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08
    


    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

    #     super().__init__(species, qty, "domestic", 0.08)


class GovernmentMelonOrder(AbstractMelonOrder): 
    """Ubermelon has struck a deal with the US Government."""

    # tax = 0.00 
    passed_inspection = False 
    
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        # self.passed_inspection = False
        super().__init__(species, qty, order_type='Government', tax=0.00)
 
    def mark_inspection(self, passed):
        # if passed == bool('True'): 
            self.passed_inspection = passed



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    # order_type = "international"
    # tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        self.country_code = country_code
        super().__init__(species, qty, order_type='International', tax=0.17)
        #  self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


