print("Enter 6 temperatures in Celsius (e.g., 36C/36c):")

celsius = []
while len(celsius) < 6:
    temp = input('')
    if temp.endswith("c") or temp.endswith("C"):
        try:
            celsius.append(float(temp[:-1]))
        except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("Please enter the temperature in the correct format. ")
    
if celsius: 
    min1 = min(celsius)
    max1 = max(celsius)
    mean = sum(celsius) / len(celsius)
    print(f'The minimum is {min1}, the maximum is {max1}, and the mean is {mean:.2f}.')
else:
    print("No temperatures were entered.")
