'''Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value.'''


print("Enter temperatures in Celsius (e.g., 36C/36c).\nPress Enter to finish:")

celsius = []
while True:
    temp = input('')
    if temp == '': 
        break
    try:
        if temp.endswith('c') or temp.endswith("C"):
            celsius.append(int(temp[:-1]))
        else:
            print("Please enter in correct format.")       
    except ValueError:
        print("Please enter a value.")
        
if celsius:  
    min1 = min(celsius)
    max1 = max(celsius)
    mean = sum(celsius) / len(celsius)
    print(f'The minimum is {min1}, the maximum is {max1}, and the mean is {mean:.2f}.')
else:
    print("No temperatures were entered.")
