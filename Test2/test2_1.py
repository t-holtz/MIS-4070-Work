# Student: Tanner Holtz
# Semester: Fall 2024
# Test 2
# Question 1
purchase = float(input("Enter amount of purchase: "))
if purchase >= 1000:
    discount = purchase *.1
    purchase = purchase - discount
elif purchase >= 250:
    discount = purchase *.5
    purchase = purchase - discount
print(f"Discount Applied: {discount}")
print(f"Final Purchase: {purchase}")