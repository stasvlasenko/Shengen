countries =[
    {'name': 'Thailand', 'sea': True, 'shengen': True,'echange': 2.2},
    {'name': 'Hungray', 'sea': False, 'shengen': True,'echange': 4.3},
    {'name': 'Japan', 'sea': True, 'shengen': False, 'echange': 1.1}
    ]

countries_dict={
    'Italy':    {'sea': True,
                'hot': 23,
                'shengen': True,
                'amount': 2.2,
                'cost': 10000},
    'Hungray':  {'sea': True,
                'hot': 20,
                'shengen': True,
                'amount': 4.3,
                'cost': 5000},
    'Japan':    {'sea': True,
                'hot': 22,
                'shengen': False,
                'amount': 1.1,
                'cost': 50000},
    'Russia':   {'sea': True,
                 'hot': 25,
                 'shengen': False,
                 'amount': 1,
                 'cost': 30000},
    'USA':      {'sea': True,
                 'hot': 25,
                 'shengen': False,
                 'amount': 65,
                 'cost': 10000},
    'Austria':  {'sea': False,
                 'hot': 23,
                 'shengen': True,
                 'amount': 75,
                 'cost': 20000},
    'Germany':  {'sea': True,
                 'hot': 25,
                 'shengen': True,
                 'amount': 75,
                 'cost': 15000},
    'China':    {'sea': True,
                 'hot': 33,
                 'shengen': False,
                 'amount': 5,
                 'cost': 5000}
}

my_money = 50000

#1 Search country here sea and hot
#2 Search country here shengen
#3 And select country first or two here mony it is OK

#1
Sea_and_hot = []
for country in countries_dict.keys():
    if countries_dict[country]['sea'] == True and countries_dict[country]['hot'] >= 23:
        Sea_and_hot.append(country)
print(Sea_and_hot)

#2
Shengen = []
for country in countries_dict.keys():
    if countries_dict[country]['shengen'] == True:
        Shengen.append(country)
print(Shengen)

#3 Страны где нам хватает денег прожить там месяц
full_money = []
cost_mount = 0
for country in countries_dict.keys():
    cost_mount = countries_dict[country]['amount'] * countries_dict[country]['cost']
    if cost_mount <= my_money:
        full_money.append(country)

#4
one_two = set(Sea_and_hot + Shengen)
three = set(full_money)
print('Либо есть шенген, либо море и тепло:', one_two)
print('Хватает денег:', three)

print('Хватает денег и соответсвует нашим требованиям',one_two.intersection(three))

shengen_counties = set()
sea_countries = set()


for country in countries:
    if country['shengen']:
        shengen_counties.add(country['name'])
    if country['sea']:
        sea_countries.add(country['name'])

#print(shengen_counties)
#print(type(sea_countries))
#print('Страны в шенгене с морем:', shengen_counties & sea_countries)


count = 0
#print(countries[0])
for test in countries:
    print('В валюте - У нас %0.2f денег' % (my_money/test['echange']))


