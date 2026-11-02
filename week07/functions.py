# Self Assessment Questions
# Q1: The first bug I noticed was the colon missing after sales. I found it by reading the code and noticing the for loop was not properly formatted. This tells me I can look at simple code and notice when things are not where they should be.
# Q2: apply_discount(price, tier) is a function that takes in a price and a tier (gold, silver, bronze, or none) and returns the price after applying the appropriate discount based on the tier. The function uses if-elif-else statements to determine the discount percentage based on the tier and then calculates the discounted price by multiplying the original price by (1 - discount). You input the price and the tier, and it outputs the final price after the discount has been applied. A colleague could probably use this function without reading the body.
# Q3: I used Claude to help format the code and explain the functions. I also used it to do a final check of all my code when I was done. For Exercise 5, I used Claude to help find the third bug in the code. The AI helped me understand certain parts, but I also used it to shortcut my work and make sure I was on the right track.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
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

print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")

# --- Exercise 3 ---
def calculate_tax(price, rate):
    return price * rate


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


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


# Step by step, using the two functions separately
discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")

total = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${total:.2f}")

# All in one, using final_price
result = final_price(200, "gold", 0.07)
print(f'final_price(200, "gold", 0.07) = ${result:.2f}')

# --- Exercise 4 ---
def calculate_tax(price, rate):
    return price * rate


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


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
# Fix: changed = to += so each sale gets added to the total instead of replacing it
    total += sale
print(f"Total: ${total}")

count = 0
# Fix: added a colon at the end because Python needs a colon to start a for loop
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
# Fix: changed <= to < because the list items are numbered 0 to 4, so there is no item 5
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---
# SCOPE: A variable created inside a function only exists inside that function. It's like a private notepad the function throws away when it finishes. So the x = 999 inside double_it() is a brand-new variable that happens to share the name x. It never touches the x = 100 outside.

x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here?
print(double_it()) # what prints here?
print(x)           # has x changed?