number = 5432
thousands =number//1000
hundreds =(number%1000)//100
tens =(number%100)//10
ones =number%10
sum_of_digits = thousands + hundreds + tens + ones
print(sum_of_digits)