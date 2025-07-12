try:
    a=int(input())
    b=int(input())
    c=input()
except ValueError as e:
      print("ValueError",e)
except TypeError as e:
      print("TypeError",e)
except NameError as e:
      print("NameError",e)
finally:
    print("done")



