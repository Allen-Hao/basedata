#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Allen time：2019/11/10

"""
1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及【其他】的个数
3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
"""

# homework one
import os


def modify_file(file_name, old_content, new_content):
    with open(file_name, mode='rt', encoding='utf-8') as read_f, \
            open('%s.swap' % file_name, mode='wt', encoding='utf-8') as write_f:
        for line in read_f:
            if old_content in line:
                line = line.replace(old_content, new_content)

            write_f.write(line)

    os.remove(file_name)
    os.rename('%s.swap' % file_name, file_name)


def calculate_count(data_str):
    dict_count = {'number': 0, 'alpha': 0, 'space': 0, 'other': 0}
    for i in data_str:
        if i.isdigit():
            dict_count['number'] += 1
        elif i.isalpha():
            dict_count['alpha'] += 1
        elif i is ' ':
            dict_count['space'] += 1
        else:
            dict_count['other'] += 1
    return dict_count


def judge_length(data):
    if len(data) > 5:
        return True
    else:
        return False


def check_up_list(data_list):
    if len(data_list) > 2:
        return data_list[:2]


def get_odd_list(data):
    odd_list = []
    for i in data:
        if data.index(i) % 2:
            odd_list.append(i)
    return odd_list


def check_up_dict(data_dict):
    for key, value in data_dict.items():
        if len(value) > 2:
            data_dict[key] = value[:2]
    return data_dict


if __name__ == '__main__':
    # modify_file('db.txt', 'zsh', 'zsh[yjn]')
    # res = calculate_count('132498  7a  fdshk   dca!@#$%$^')
    # print(res)
    # res1 = judge_length('dddddddd')
    # res2 = judge_length('        ')
    # res3 = judge_length((1, 1, 1, 1, 1, 1, 1, ))
    # print(res1, res2, res3)
    # res = check_up_list([1,2,3])
    # res1 = check_up_list((1,2,3))
    # res2 = check_up_list([1])
    # print(res, res1, res2)
    # print(get_odd_list([1,2,3,4,]))
    # print(get_odd_list(['a','a','a']))
    dict1 = {'k1': 'va',
            'k2': [11, 22, 33, 44],
            }
    # dict1 = {"k1": "v1v1", "k2": [11, 22, 33, 44], 'k3': (9, 8, 7, 65, 4)}

    print(check_up_dict(dict1))

