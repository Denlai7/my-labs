       
aaa = input("введіть дію ділення")
try:
    exec(aaa)
except ZeroDivisionError:
    print("it is not dividingguu bestie")
except:
    print("Something happened...")
else:
    print(aaa)
    