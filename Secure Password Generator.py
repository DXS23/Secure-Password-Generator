import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

counter = int(input('Какое количество паролей для генерации необходимо? '))
length = int(input('Какая длина пароля? '))
ques1 = input('Включать ли цифры 0123456789? (да или нет) ')
ques2 = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да или нет) ')
ques3 = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да или нет) ')
ques4 = input('Включать ли символы !#$%&*+-=?@^_? (да или нет) ')
ques5 = input('Исключать ли неоднозначные символы il1Lo0O? (да или нет) ')

def generate_password(length, chars):
    return random.sample(chars, length)

if ques1.lower() == 'да' or ques1.lower() == 'yes':
    chars += digits
if ques2.lower() == 'да' or ques2.lower() == 'yes':
    chars += uppercase_letters
if ques3.lower() == 'да' or ques3.lower() == 'yes':
    chars += lowercase_letters
if ques4.lower() == 'да' or ques4.lower() == 'yes':
    chars += punctuation
if ques3.lower() == 'да' or ques3.lower() == 'yes':
    for i in 'il1Lo0O':
        chars.replace(i, '')
print('Ваши пароли:')
for j in range(counter):
    print(*generate_password(length, chars), sep='')
