a=int(input("a=",))
if (a%3==0 and a%2==0):
     print("it is divisible by 3 and it is an even number",a)
elif(a%3==0 and a%2==1):
    print ("it is divisible by 3 and it is a odd number",a)
elif(a%2==0):
    print("it is not divisible by 3 and it is a even number",a)
else:
    print("it is not divisible by 3 and it is a odd number",a)