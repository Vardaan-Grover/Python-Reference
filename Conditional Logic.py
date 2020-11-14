price=input('How much did you pay in pesos: ')
price=float(price)
if price<1:
    tax=0
    print('Your tax rate is '+ str(tax)+' %')
else:
    print('Your tax rate is 1 %')

