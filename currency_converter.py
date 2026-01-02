amount = int(input("Enter the amount "))
source = input("Enter the source currency: (USD/INR/GBP)").lower()
target = input("Enter the target currency (USD/INR/GBP)").lower()

if source == "usd" and target == "inr":
    value = (amount * 90.9)
    print(value)

elif source == "inr" and target == "usd":
    value = (amount/90.9)
    print(value)
    
elif source == "gbp" and target == "inr":
    value = (amount * 121.26)
    print(value)

elif source == "inr" and target == "gbp":
    value = (amount/121.26)
    print(value)

elif source == "gbp" and target == "usd":
    value = (amount * 1.35)
    print(value)
    
elif source == "usd" and target == "gbp":
    value = (amount/1.25)
    print(value)
    
else:
    print("Enter valid input")

