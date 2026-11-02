# Self Assessment Questions
# Q1: The most surprising thing was that a slice stops right before the end number, so inventory[:3] gives me three items and not four. I also didn't expect .sort() to change the original list instead of giving me back a new sorted one. Negative indexes were a nice surprise too, because inventory[-1] always gets the last item no matter how long the list is.
# Q2: At my restaurant job, tracking sales for each shift in Excel would mean typing every number in and then going down the column by hand to find the busy days. With a Python list, I could put all the shift sales in one list and use a loop to pull out every shift over a target, then get the count and average with len() and sum(). It would take a few lines of code instead of sorting and highlighting cells every week.

# --- Exercise 1 ---
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# --- Exercise 2 ---
print(inventory[0])    # first item, positive index
print(inventory[-1])   # last item, negative index

# Middle position comes from the length, so it still works if the list changes
middle = len(inventory) // 2
print(inventory[middle])

# --- Exercise 3 ---
print(inventory[:3])   # first three items
print(inventory[-2:])  # last two items
print(inventory[::2])  # every other item

# --- Exercise 4 ---
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# --- Exercise 5 ---
coords = (40.7128, -74.0060)   # NYC

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples can't be changed, which is good for coordinates because a location should never get changed by accident.")

print(coords)

# --- Exercise 6 ---
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

# --- Exercise 7 ---
prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))

print(f"Original:   {prices}")
print(f"Discounted: {discounted}")

# --- Exercise 8 ---
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")
