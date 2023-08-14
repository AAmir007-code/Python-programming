number_1 = input('biror son kiriting: ')
number_2 = input('yana bir son kiriting: ')

for _ in ('+','-','*','**','/','//','%'):
    print(f'{number_1} {_} {number_2} = {eval(number_1+_+number_2)}')


