temp = float(input("ENTER A TEMPERATURE: "))

#TELL YOUR USE TO CHOOSE SCALE
print("CHOOSE CONVERSION")
print("1. CELSIUS TO FAREINHEIT")
print("2. FAREINHEIT TO CELSIUS")
choice = input("ENTER CHOICE (1/2): ")

#PERFORM CONVERSION 
if choice == "1":
    result = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {result}°F:")
elif choice == "2":
    result = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {result}°C")
else:
    print("INVALID CHOICE")
 # Step 4: Ask if user wants another conversion
again = input("Do you want to convert again (yes/no):").lower()
if again != "yes":
    print("GOODBYE")
    


