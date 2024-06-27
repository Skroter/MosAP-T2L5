summInvestments = 1000
cashIvan = int(input('Сколько денег у Ивана: '))
cashMike = int(input('Сколько денег у Майла: '))

if cashIvan >= summInvestments <= cashMike:
    print(2)
elif cashMike < summInvestments <= cashIvan:
    print('Ivan')
elif cashIvan < summInvestments <= cashMike:
    print('Mike')
if cashIvan < summInvestments > cashMike:
    if cashIvan+cashMike >= summInvestments:
        print('1')
if cashIvan+cashMike < summInvestments:
    print('0')
