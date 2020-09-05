x = int(input("Enter the value of the altitude: "))
print(x)

if x <= 1000:
    print("Safe to Land")
elif x <= 5000:
    print("Bring down to 1000")
else:
    print("Turn Around")

