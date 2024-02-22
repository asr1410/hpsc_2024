def mysqrt(x):
 s=1.
 for i in range(100):
  s_ = s
  s = 0.5*(s + x/s)
  if s == s_:
   print(i)
   return s
 return s
print(mysqrt(float(input())))
