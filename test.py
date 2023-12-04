#Import necessary classes from respective files
from customer import Customer
from restaurant import Restaurant

#Example usage:
customer1 = Customer("Ian", "Kimani")
customer2 = Customer("Doja", "Cat")
customer3 = Customer("Ian", "Duncan")
restaurant1 = Restaurant("Taco 'Bout It")
restaurant2 = Restaurant("Lettuce Entertain You")

customer1.add_review(restaurant1, 5)
customer2.add_review(restaurant1, 5)
customer3.add_review(restaurant2, 4)
customer1.add_review(restaurant2, 5)
customer3.add_review(restaurant2, 3)

print("Average Star Rating for Taco 'Bout It:", restaurant1.average_star_rating())
print("Restaurants reviewed by Ian Kimani:", [restaurant.name for restaurant in customer1.restaurants()])
print("Customer found by name :", Customer.find_by_name("Ian Kimani").full_name())
print("All customers with given name 'Ian':", [customer.full_name() for customer in Customer.find_all_by_given_name("Ian")])