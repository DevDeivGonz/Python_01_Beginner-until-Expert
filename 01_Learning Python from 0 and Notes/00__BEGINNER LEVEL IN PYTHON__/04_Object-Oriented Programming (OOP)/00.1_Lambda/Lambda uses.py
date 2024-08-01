x = lambda a, b: a * b
print(x(5, 6))

# //////////////////////////////////////

y = lambda x, y: x + y
print(y(10, 3))

# ////////////////////77
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))