# Extract the thousands place by performing integer division by 1000
# Extract the hundreds place by first performing integer division by 100, then using modulus to get the last digit
# Extract the tens place by first performing integer division by 10, then using modulus to get the last digit
# Extract the ones place by performing modulus 10 on the number
# Calculate the sum of all the digits
# Print the sum of the digits


number = 5432
thousands =number//1000
hundreds =(number%1000)//100
tens =(number%100)//10
ones =number%10
sum_of_digits = thousands + hundreds + tens + ones
print(sum_of_digits)
