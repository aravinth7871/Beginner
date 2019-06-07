Numb = int(input("Please Enter any Numb: "))
Count = 0
while(Numb > 0):
    Numb = Numb // 10
    Count = Count + 1
print("\n Numb of Digits in a Given Numb = %d" %Count)
