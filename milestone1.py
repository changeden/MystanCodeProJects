"""
File: Milestone1.py
Name: 
-----------------------
This file tests the milestone 1 for
our babyname.py project
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    if name in name_data:      #dictionary 條件的寫法 為  "if .... in ....: " or "if ....not in ...: "
        if year in name_data[name]: # 請注意 year 是name_data[name] value, name 是name_data value
            if int(rank) < int(name_data[name][year]):  #進來的 rank 比原本的 rank 小,要進來的rank
                name_data[name][year]=rank  #這樣只有把最小的dictionary 寫出來
        else:
            name_data[name][year] = rank

    else:
        name_data[name]={year:rank}       #這樣是加了一個大的dictionary （name) and 一個小的dictionary {year:rank},注意是:
        # name_data[name][year] = rank   -->這樣只有把最小的dictionary 寫出來

# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #
#可以直接拿test 4  試試看會比較了解bug
# def test4():
#     name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
#     add_data_for_name(name_data, '2010', '208', 'Kate')
#     add_data_for_name(name_data, '2000', '108', 'Kate')
#     add_data_for_name(name_data, '1990', '200', 'Sammy')
#     add_data_for_name(name_data, '1990', '90', 'Sammy')
#     add_data_for_name(name_data, '2000', '104', 'Kylie')

def test1():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test3():
    name_data = {'Kylie': {'2010': '57'}, 'Sammy': {'1980': '451', '1990': '200'}, 'Kate': {'2000': '100'}}
    add_data_for_name(name_data, '1990', '900', 'Sammy')
    add_data_for_name(name_data, '2010', '400', 'Kylie')
    add_data_for_name(name_data, '2000', '20', 'Kate')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
