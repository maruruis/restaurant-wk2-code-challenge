from review import Review

class Restaurant:
    all_restaurants = [] # Class variable to keep track of all restaurant instances


    def __init__(self, name):
        self.name = name
        Restaurant.all_restaurants.append(self) # Add the current restaurant instance to the list of all restaurants

# Method to get the name of the restaurant
    def name(self):
        return self.name

    # Class method to get all restaurant instances
    @classmethod
    def all(cls):
        return cls.all_restaurants

     # Method to get a list of reviews for the current restaurant
    def reviews(self):
        return [review for review in Review.all() if review.restaurant == self]

    def customers(self):
        return list(set([review.customer for review in self.reviews()]))
     
    def average_star_rating(self):
        if not self.reviews():
            return 0.0

        total_rating = 0.0
        for review in self.reviews():
            total_rating += review.rating # Sum up the ratings of all reviews for the restaurant

        return total_rating / len(self.reviews())
