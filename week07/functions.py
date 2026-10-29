
# Self-Assessment Questions:

# 1. The first mistake that I found in the code was that there
# was a missing colon for the for loop. I also saw it by 
# seeing the error message, which help me find the errors.

# 2. The apply_discount takes a price and tier, and it applies it
# to the correct discount and returns the discounted price.

# 3. I used ChatGPT to help me understand the
# material if I made a mistake, to help identify errors after I tried,
# and gave me more clarification when I needed


#Exercise 1: calculate_tax

def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


#Exercise 2: apply_discount

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")


#Exercise 3: Compose them

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


#Exercise 4: Loops + function

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


#Exercise 5: Debug first, then ask

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    # I changed the = to += in order to add all of the sales together.
    total += sale
print(f"Total: ${total}")

count = 0
# I added the missing colon to the for loop.
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
# I changed the <= to < to avoid moving past the list.
while i < len(sales):
    print(sales[i])
    i += 1


#Exercise 6: Scope experiment

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# The local x doesn't change the global x
