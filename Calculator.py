import string
print("This program will calculate the ROI for any given stock")
purchPrice = float(input("Initial Purchase Price: $"))
quantity = float(input("How many shares did you purchase? "))
sellPrice = float(input("Today's Price (or price when sold): $"))

gain_loss = (sellPrice - purchPrice) * quantity
gain_loss_percent = (sellPrice - purchPrice) / purchPrice

if gain_loss > 0:
    print(f"You made a profit of ${gain_loss}")
elif gain_loss < 0:
    print(f"You have a loss of ${-gain_loss}")
else:
    print("You have neither made profit nor loss.")
