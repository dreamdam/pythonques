num=int(input("Enter the number to be reversed: "))
reversed_num=0
while num>0:
    digit = num%10
    reversed_num = reversed_num*10 + digit
    num=num//10
print(f"Reversed number: {reversed_num}")
print("Program by Arnav Kharbanda, 0221BCA050")