def median(x):
  y=sorted(x)
  n=len(y)
  h=int(n/2)
  print 'n, h=',n,h
  if n%2==0:
    return (y[h]+y[h-1])/2.
  else:
    return y[h]
  
print median([ 7, 12, 3, 1, 6])
print 'this is a test'
