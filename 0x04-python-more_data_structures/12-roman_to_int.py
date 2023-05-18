#!/usr/bin/python3
def to_sub_max(list_num):
    to_subtract = 0
    max_val = max(list_num)

    for j in list_num:
        if max_val > j:
            to_subtract += j

    return (max_val - to_subtract)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_num.keys())

    no = 0
    prev_rom = 0
    list_num = [0]

    for i in roman_string:
        for roman_num in list_keys:
            if roman_num == i:
                if rom_num.get(i) <= prev_rom:
                    no += to_sub_max(list_num)
                    list_num = [rom_num.get(i)]
                else:
                    list_num.append(rom_num.get(i))

                prev_rom = rom_num.get(i)

    no += to_sub_max(list_num)

    return (no)
