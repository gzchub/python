#!/usr/bin/python

l = [1,5,2,9,3,6]
i = 0
n = len(l)

while i < n - 1:
    j = 0
    while j < n - i - 1:
      if l[j] > l[j + 1]:
          l[j],l[j + 1] = l[j + 1],l[j]

      j += 1
    i += 1
print l
