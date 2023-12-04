class Review:
    # Class variable to keep track of all review instances
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

   # Method to get the rating of the review
    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews
# Method to get the customer who created the review
    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant
