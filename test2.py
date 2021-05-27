result = 1
try:
   print('Enter Hours:')
   x = float(input())
   print('Enter Rate:')
   y = float(input())
except:
   print('Hanya terima angka bang')
   result = 0

if result == 1:
   z = (x * y) + (5 * 15)
   print('Pay: ' + str(z)) 