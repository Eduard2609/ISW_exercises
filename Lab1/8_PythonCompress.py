from itertools import groupby
for key, group in groupby(input("Enter string of numbers: ")):
   print('({}, {})'.format(len(list(group)), key), end=" ")