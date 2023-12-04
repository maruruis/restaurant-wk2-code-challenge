from review import Review

class Customer:
    # Class variable to keep track of all customer instances
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        # Class method to get all customer instances
        return cls.all_customers

    def restaurants(self):
        # Method to get a list of unique restaurants reviewed by the current customer
        return list(set([review.restaurant for review in Review.all() if review.customer == self]))

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)

    def num_reviews(self):
        return len([review for review in Review.all() if review.customer == self])

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all():
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
         # Class method to find all customers with a given given name
        return [customer for customer in cls.all() if customer.given_name == name]
