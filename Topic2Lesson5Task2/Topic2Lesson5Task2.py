word = input('Введите слово из строчныч латинских букв: ');
c = ""
vowel = 0
consonant = 0
x1 = True
for a in word:
    if a not in c:
        if a in 'aeoiu':
            print(f"{a}: {word.count(a)}", 'глассная' )
            c += a
for d in word:
    if d in 'aeuio':
        vowel += 1
    else:
        consonant += 1
        x1 = False
if x1 == False:
    print('Какой то из букв условия нет в слове', x1)
print('Гласных ', vowel)
print('Согласных ', consonant)
