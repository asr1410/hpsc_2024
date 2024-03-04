def sqroot(x):
 s=1.
 from numpy import nan
 if x == 0:
  return 0
 elif x < 0:
  return nan
 for i in range(100):
  s_ = s
  s = 0.5*(s + x/s)
  if s == s_:
   print(i)
   return s
 return s
#print(f'the square root of given input is {sqroot(float(input("enter the number = ")))}')
