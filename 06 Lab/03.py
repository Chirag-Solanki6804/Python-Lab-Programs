# 3. WAP to take a list of any six product names split the list into two and append the first part to the end of the list.

products=["p1","p2","p3","p4","p5","p6"];

if len(products)==6:
    mid=len(products)//2

    part1=products[:mid]
    part2=products[mid:]

    products.extend(part1)

print(products)
