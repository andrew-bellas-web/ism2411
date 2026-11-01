
# Reflection 1:
# The most surprising thing about Python lists is how easy it is to
# add and remove items without having to create new lists 
#every time. I expected it to be a lot more difficult when
#seeing it for the first time.

# Reflection 2:
# In my accounting class, I have worked with sales data using Excel.
# Using python lists could have saved me a lot of time by being able 
# to calculate total sales, averages, and finding the highest and 
# lowest sales automatically.


# Exercise 1 - Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# Exercise 2 - Index practice
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# Exercise 3 - Slicing
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4 - Modify
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5 - Tuple comparison
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed after they are created.")
    print("This is useful for coordinates because the values stay the same.")

print(coords)


# Exercise 6 - Average of a list of sales
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7 - Accumulator pattern
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original:", prices)
print("Discounted:", discounted)


# Exercise 8 - Filter above threshold
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))
