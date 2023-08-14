# #Uyga vazifalar:
# 2) A, B va C sonlarini kiriting va A ni qiymati B ga, B ni qiymati C ga
# va C ni qiymati A ga almashtirilsin. A, B va C ning yangi qiymatlarini
# chiqaring.
# A, B, C = map(int, input().split())
# A, B, C = C, A, B
# #================ 2-usul QO'shimcha o'zgaruvchi orqali
# # temp = B
# # B = A
# # temp2 = C
# # C = temp
# # A = temp2
# print(f'A = {A}, B = {B}, C = {C}')

# 3) A, B va C sonlarini kiriting va A ni qiymati C ga, C ni qiymati B ga
# va B ni qiymati A ga almashtirilsin. A, B va C ning yangi qiymatlarini
# # chiqaring.
# A, B, C = map(int, input().split())
# A, B, C = B, C, A


# 4) Ikki xonali sonni kiriting va ushbu sonni o’nliklar va birliklar
# xonasidagi raqamlarini va ularning yi’g’indisini chiqaring.
# number = int(input('2 xonali son kiriting: '))
# onlar, birlar = number//10, number%10
# print(f'O`nlar = {onlar}, Birlar = {birlar} Yig`indisi = {onlar+birlar}')


# 5) Ikki xonali sonni kiriting va ushbu sonni teskari tartibda o’ziga
# joylashtiring. Sonning o’zgargan qiymatini chiqaring.
# number = int(input('2 xonali son: '))
# number = number%10*10 + number//10
# print(f'Sonning teskarisi {number}')


# 6) Uch xonali sonni kiriting va ushbu sonni o’nliklar va birliklar
# xonasidagi raqamlarini va ularning yi’g’indisini chiqaring.
# number = int(input('3 xonali son: '))  # 158
# onlar,birlar = number%100//10, number%10
# print(f"O'nlar = {onlar}, Birlar = {birlar} Yig'indisi = {onlar+birlar}")

# 7) To’rt xonali sonni kiriting va ushbu sonni teskari tartibda o’ziga
# joylashtiring. Sonning o’zgargan qiymatini chiqaring.
# number = int(input('4 xonali son kiriting: '))
# number = number % 10 * 1000 + number % 100 // 10 * 100 + number % 1000 // 100 * 10 + number // 1000
# print('teskarisi ',number)
# 8) Kun boshidan boshlab N sekund vaqt o’tdi (N ni input orqali
# kiriting). Kun boshidan boshlab nechi soat, minut va sekund
# o’tganligini aniqlang va natijani chiqaring
N = int(input('Necha sekund o\'tdi? '))
soat = N // 3600
minut = N % 3600 // 60
sekund = N % 60
print(f'{soat:0>2}:{minut:0>2}:{sekund:0>2}')
# 1 soat : 60 min => 1 min => 60 sek