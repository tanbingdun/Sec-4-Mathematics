import statistics
from math import floor
from math import log10

print("This is the Mean and Standard Deviation Calculator for Discrete Data by Mr Tan!\n")

data_input = input("Enter your data set separated by space: ")
data_list = data_input.split()
#data_list.sort()
data_float = [float(num) for num in data_list]

# Total frequency of data
n = len(data_float)
print(f"\nTotal frequency of data = {n}\n")

# For computing mean
mean = statistics.mean(data_float)

# For computing spread
pstdev = statistics.pstdev(data_float)

def round_to_3_sf(number):
    num_str = str(number).replace('.', '')  # Remove decimal point if present
    sf_count = sum(c.isdigit() for c in num_str)

    if sf_count == 3:
        return number
    else:
        rounded_number = round(number, -int(floor(log10(abs(number)))) + 2)
        return rounded_number

mean_3sf = round_to_3_sf(mean)
pstdev_3sf = round_to_3_sf(pstdev)

print(f"Mean of data= {mean_3sf}\n")
print(f"Standard Deviation = {pstdev_3sf}\n")
