shengen_window = 180
residents = 90

def wellcome():
    print('Это шенгенский калькулятор, он считает дни пребывания в шенгене. Чтобы выполнять нужные функции, нажимайте нужные кнопки')
    print_list_visits(visits)
def print_list_visits(visits):
    if len(visits) == 0:
        non_visit = 'В списке нет визитов'
        print(non_visit)
        return non_visit
    else:
        yes_visit = 'Даты визитов в списке: %s' % visits
        print(yes_visit)
        return yes_visit
def print_command_for_input(command):
    for key in command:
        print('%s - %s' % (key, command[key]))
def del_visit(visits):
    #Проверить, есть ли в принципе визиты
    if len(visits) == 0:
        return 0
    #Вывести список визитов
    print('Введите номер визита для удаления:')
    count = 0
    for element in visits:
        count += 1
        print('%s визит - %s ' % (count, element))

    var_del = (int(input())-1)
    del visits[var_del]
def cross_date_new_input_value(visits, one_data):
    non_conflict = 0

    if len(visits) > 0:
        for visit in visits:
            if visit[0] <= one_data[0] and visit[1] <= one_data[0]:
                non_conflict += 0
            elif visit[0] >= one_data[1]:
                non_conflict += 0
            else:
                non_conflict += 1

    if non_conflict == 0:
        return True
    else:
        return False
def add_date_visit(visits):
    true_data = False
    while true_data == False:
        print('Введите дату въезда:')
        data_in = int(input())
        print('Введите дату выезда:')
        data_out = int(input())
        if data_in <= data_out:
            list_date = [data_in, data_out]
            true_data_step_one = True
        else:
            print('Дата выезда не может быть раньше даты въезда, введите верные значения')

        check_90 = True
        duration = data_out - data_in
        if duration <= 90:
            check_90 = True
        else:
            check_90 = False

        if check_90 == False:
            print('Добавляемый визит длится %s дней. Визит не добавлен.' % (list_date[1] - list_date[0]))


        peresechenie = cross_date_new_input_value(visits, list_date)
        if peresechenie == False:
            print('Даты поездок не должны пересекаться, введите верное значение')

        if peresechenie == True and true_data_step_one == True and check_90 == True:
            true_data = True

    if true_data == True:
        #Добавляем дату к списку, ищем предыдущий визит и добавляем после него. если он первый, сразу добавим
        if len(visits) > 0:
            resist=[]
            for visit in visits:
                resist.append(list_date[0] - visit[1])

            find_index = 0
            for find in resist:
                if find >= 0:
                   find_index += 1
                else:
                    break

            #Нашли ячейку в основном спике, где разница между новым въездом и последним выездом минимальная. В следующую за енй ячейку можно ставить новую поездку
            visits.insert(find_index, list_date)

        else:
            visits.append(list_date)
def duration_every_visit(visits):
    list_time_visits = []
    count_visit = 0
    #print('Даты поездок:', visits)
    for time_one_visit in visits:
        count_visit += 1
        time_visit = 0
        time_visit = time_one_visit[1] - time_one_visit[0] + 1
        list_time_visits.append(time_visit) #Создали список с продолжительностью каждой поездки
        #print('Визит №',count_visit, '=', time_visit, 'дней')
    return list_time_visits
def check_visits_day_90(list_time_visits):
    count_visit = 0
    for check_time in list_time_visits:
        erorr_residents = False
        count_visit += 1
        if check_time > residents:
            erorr_residents = True

    if erorr_residents == False:
        return True
    else:
        return False
def limits_visits(visits):
    check = check_visits_day_90(duration_every_visit(visits))
    if check == False:
        return
    erorr_window = False
    count_visit = 0
    for done_window in visits:
        count_visit += 1
        start_window = done_window[1] - shengen_window #Нашли дату начала окна

        list_days_in_window = []
        all_time_in_window  = 0

        for in_window in visits: #Находим поездки в окне и их длительность

            if start_window <= in_window[0] and in_window[1] <= done_window[1]:
                var_days_in_window = in_window[1] - in_window[0] + 1
                list_days_in_window.append(var_days_in_window)

        all_time_in_window = sum(list_days_in_window) #Складываем длительность поездок

        if all_time_in_window <= residents:
            #print('Время пребывания не нарушено, вы можете пробыть в этом окне ещё', residents - all_time_in_window, 'дней')
            print('Визит:', count_visit, '— Ок')
        else:
            print('Визит:', count_visit, '— Время пребывания в окне:', all_time_in_window, 'дней')
            corect_start = 0
            if start_window < 0:
                corect_start = 0
            else:
                corect_start = start_window
            print('Сократите время прибывания в интервале дат:', corect_start, '—', done_window[1])
            print('Минимальное время сокращения:', all_time_in_window - residents, 'дней.')
            erorr_window = True

    if erorr_window == False:
        all_ok = 'Все визиты укаладываются в %s дней, за последние %s дней' %(residents, shengen_window)
        print (all_ok)
        return all_ok

#открытьфайл
#Прочитать первую строку
#Создать массив с двумя значениями
#Положить массив в основной массив
#Прочитать вторую строку
#Создать массив
#Положить массив в основной массив

visits = []
#Открыли файл
with open('date_visits', 'r') as file:
    #считали его построчно
    for line in file:
        #Строку разбили на элементы и создали список
        line_visits = line.split()
        #Преобразовываем элементы из строки в инты
        list_int_line_visits = []
        for int_line_visits in line_visits:
            list_int_line_visits.append(int(int_line_visits))
        #Заполянем список визитов списками интов построчно
        visits.append(list_int_line_visits)


#visits = [[17, 20], [21, 51], [90, 120], [200, 250], [310, 399]]
command = { 'p': 'Печатать список визитов',
            'v': 'Добавить визит',
            'y': 'Удалить визит',
            'e': 'Выход'
           }
wellcome()
loop = True
while loop == True:
    limits_visits(visits)
    print('Введите нужную команду:')
    print_command_for_input(command)
    job = input()
    if job == 'v':
        add_date_visit(visits)
    if job == 'p':
        print_list_visits(visits)
        duration_visit = duration_every_visit(visits)
        over_90 = check_visits_day_90(duration_visit)
    if job == 'e':
        print('Работа программы завершена, результаты записаны в файл')
        break
    if job == 'y':
        del_visit(visits)

#Закрыть файл и записать туда всю информацию.
duration_visit = duration_every_visit(visits)
with open('date_visits', 'a') as file:
    file.write('\n\n --------- \n Результат работы программы:\n')
    list = print_list_visits(visits)
    file.write(str(list))
    file.write('\n Продолжительность каждого визита:')
    file.write(str(duration_visit))
    file.write('\n')
    file.write(str(limits_visits(visits)))