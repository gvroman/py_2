# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_correct = False

while not ip_correct:
    ip_address = input("введите ip-адрес: ")
    octets = ip_address.split('.')
    for oct in octets:
            if not oct.isdigit() or len(octets) != 4 or not 0 <= int(oct) <= 255:
                print('Неправильный IP-адрес')
                break
    else:
        ip_correct = True
        if ip_address == "255.255.255.255":
            print("local broadcast")
        elif ip_address == "0.0.0.0":
            print("unassigned")
        elif 1 <= int(octets[0]) <= 223:
            print("unicast")
        elif 224 <=int(octets[0]) <= 239:
            print("multicast")
        else:
            print("unused")
