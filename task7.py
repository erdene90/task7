air_list = [
    {
        'id': 1012,
        'name': 'Bishkek-Osh',
        'time': '18-00',
        'price': '4500'
    },
    {
        'id': 1013,
        'name': 'Bishkek-Moskva',
        'time': '08-00',
        'price': '25000'
    },
    {
        'id': 1014,
        'name': 'Bishkek-Astana',
        'time': '12-00',
        'price': '8000'
    }
]


for i in air_list:
    print('--------------------------')
    print(f'номер рейса: {i["id"]}')
    print(f'от куда куда: {i["name"]}')
    print(f'время вылета: {i["time"]}')
    print(f'Цена: {i["price"]} сом')
    print('--------------------------')
while True:
    number = input('Выберите номер рейса: ')
    try:
        number = int(number)
    except:
        print('Выберите номер рейса правильно!!!')
        continue       
    break
name = input(str('Напишите ФИО: '))
 
cash = int(input('Оплатите: '))

air_price = 0
FullName = ''
air_time = ''
kuda = ''
for i in air_list:
    if number == i['id']:
        air_price = i['price']
        FullName = name
        air_time = i['time']
        kuda = i['name']    



def slovo():
    print(f'Заберите билет,\n ваш номер рейса {number}\n ФИО: {FullName}\n от куда куда: {kuda}\n время вылета: {air_time}')

change = cash - int(air_price)
if change == 0:
    slovo()

elif change < 0:
    print(f'У вас не хватает средств')

else:
    print(f'Сдача: {change}')
    slovo()

