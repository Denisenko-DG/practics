n=int(input("Введите число"))
seven, five ='0', '0'
if (n% 7 ==0)and(n%5==0):   print('11')
if (n% 7!=0)and(n%5==0):   print('01')
if (n% 7 ==0)and(n%5!=0): print('10')
if (n% 7!=0)and(n%5!=0):print('00')