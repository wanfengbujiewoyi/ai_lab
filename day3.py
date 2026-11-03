name=input("whats your name")
weight=input("whats your weight")
height=input("whats your height")
weight_one=float(weight)
height_one=float(height)
bmi=weight_one/height_one**2
print(f"hello {name},your bmi is{bmi:.2f}")