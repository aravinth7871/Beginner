numb1 = 1
numb2 = 1
numb3 = -4
if (numb1 >= numb2) and (numb1 >= numb3):
   largest = numb1
elif (numb2 >= numb1) and (numb2 >= numb3):
   largest = numb2
else:
   largest = numb3

print("The largest number between",numb1,",",numb2,"and",numb3,"is",largest)

