# 12. WAP to enter name, quantity and price of 5 products by a user. Generate and print all the details with the Product’s total amount in formatted manner.

productNames=[""]*5
productPrice=[0]*5
productQuantity=[0]*5

totalAmount=0

for i in range(5):
    productNames[i]=input("Enter Product Name :")
    productPrice[i]=int(input("Enter Product Price :"))
    productQuantity[i]=int(input("Enter Product Quantity :"))
    totalAmount+=productPrice[i]*productQuantity[i]
    print("*************************************")

for i in range(5):
    print("Name :",productNames[i],", Price :",productPrice[i],", Quantity :",productQuantity[i])

print("TOTAL AMOUNT :",totalAmount)

