a = 1042000
b = 702648265

for num in range(a, b + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print("The first armstrong number is",num)
       break
