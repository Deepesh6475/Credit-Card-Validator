# Luhn's Algorithm
#card_number = "5610591081018250"
odd_index_sum = 0
even_index_sum = 0
doubled_list = []
double_string = ""

card_number = list(card_number)

for (index, value) in enumerate(card_number):
    if index % 2 != 0:
        odd_index_sum += int(value)
    else:
        doubled_value = int(value) * 2
        doubled_list.append(doubled_value)

# converting list into string
for i in doubled_list:
    double_string += str(i)
# converting string back to list
doubled_list = list(double_string)
for i in doubled_list:
    even_index_sum += int(i)

total = odd_index_sum + even_index_sum
if total % 10 == 0:
    print("Valid Credit Card Number")
else:
    print("Invalid Credit Card Number")
