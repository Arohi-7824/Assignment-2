#Program to calculate sum and avergae 

def total_sum(**args):
    total=0
    for i in args:
        total=total+args[i]
    return total

def average(**args):
    return total_sum(**args)/len(args)

def max_num(**args):
    max_value=float('-inf') #Initialize max_value to negative infinity
    for i in args:
        if args[i] > max_value: #Update max_value if a larger value is found
            max_value = args[i]
    return max_value

def min_num(**args):
    min_value=float('inf') #Initialize min_value to positive infinity
    for i in args:
        if args[i] < min_value: #Update min_value if a smaller value is found
            min_value = args[i]
    return min_value    

try:
    n=int(input("Enter the number of values: ")) #Input number of values to be calculated
    if n <= 0:
        print("Please enter a valid number of values (greater than zero).")
    else:
        values = {}
        for i in range(n):
            value = int(input(f"Enter value {i+1}: ")) #Input values from the user
            values[f"value_{i+1}"] = value #Store values in a dictionary with keys like value_1, value_2, etc.
        
        print(f"Sum: {total_sum(**values)}") #Function call for total sum using dictionary unpacking
        print(f"Average: {average(**values)}")#Function call for average value
        print(f"Maximum: {max_num(**values)}")#Function call for maximum value
        print(f"Minimum: {min_num(**values)}") #Function call for minimum value
except ValueError:
    print("Please enter valid integers for the values.")