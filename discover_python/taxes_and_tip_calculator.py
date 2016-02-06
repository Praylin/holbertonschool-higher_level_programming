"""Author: Praylin Diana
#Program Name: Taxes and tip calculator 
#This program is to find the total price of a meal. It gets the price of meal, the percentage of tax and the percentage of tip from user and calculates the total price"""

print "Welcome to the taxes and tip calculator!" #Print the welcome message
meal_price = float(raw_input ("What is the price before tax? ")) #Get price of meal before tax from user
taxes = float(raw_input("What are the taxes? (in %) ")) #Get the % of tax from user
tip = float(raw_input("What do you want to tip?  (in %) ")) #Get the % of tip the user wish to pay
meal_price = meal_price + (meal_price * tip/100) #Price of meal after adding tip
total_price = meal_price + (meal_price * taxes/100) #Total price after adding tax
print("The price you need to pay is: $%f." %total_price) #Print total price

