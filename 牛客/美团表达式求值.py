

a=input()
try:
    print("true"if eval(a.replace("t","T").replace("f","F")) else"false")
except:
    print("error")