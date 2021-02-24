from typing import Tuple, List

import xlrd
import xlsxwriter

from merge_excel.similar_names import get_pinyin_similarity, get_name_similarity

L = List[Tuple[str, str]]


def get_compare_result(names_1: list, names_2: list) -> List[L]:
    tmp_names_1 = names_1[:]
    tmp_names_2 = names_2[:]
    same_names: L = []  # 名字相同
    same_pinyin: L = []  # 读音相同
    similar_names: L = []  # 相似的名字

    for i in tmp_names_1[:]:
        if i in tmp_names_2:
            same_names.append((i, i))
            tmp_names_1.remove(i)
            tmp_names_2.remove(i)

    for i in tmp_names_1[:]:
        for j in tmp_names_2[:]:
            if get_pinyin_similarity(i, j) == 1:
                same_pinyin.append((i, j))
                tmp_names_1.remove(i)
                tmp_names_2.remove(j)

    for i in tmp_names_1[:]:
        level = 0
        tmp_container = tuple()
        for j in tmp_names_2[:]:
            similarity = get_name_similarity(i, j)
            if similarity > level and similarity > 0.4:
                level = similarity
                tmp_container = (i, j)
        if tmp_container:
            similar_names.append(tmp_container)
            tmp_names_1.remove(tmp_container[0])
            tmp_names_2.remove(tmp_container[1])

    return [
        sorted(same_names),
        sorted(same_pinyin),
        sorted(similar_names),
        sorted(tmp_names_1),
        sorted(tmp_names_2),
    ]


def open_excel(path):
    data = xlrd.open_workbook('tmp.xlsx')
    # 查看工作表

    table = data.sheet_by_index(0)
    # 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1
    # table = data.sheet_by_index(0)

    # 获取行数和列数
    # 行数：table.nrows
    # 列数：table.ncols
    print("总行数：" + str(table.nrows))
    print("总列数：" + str(table.ncols))

    # 获取整行的值 和整列的值，返回的结果为数组
    # 整行值：table.row_values(start,end)
    # 整列值：table.col_values(start,end)
    # 参数 start 为从第几个开始打印，
    # end为打印到那个位置结束，默认为none
    # print("整行值：" + str(table.row_values(0)))
    # print("整列值：" + str(table.col_values(0)))
    # print("整列值：" + str(table.col_values(1)))
    column_1 = table.col_values(0)
    column_2 = table.col_values(1)
    print('第一列', column_1)
    print('第二列', column_2)
    return column_1, column_2


def write_excel(results):
    workbook = xlsxwriter.Workbook('compare_result.xlsx')  # 创建一个excel文件
    worksheet = workbook.add_worksheet('sheet1')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1

    # worksheet.set_column('A:A', 20)  # 设置第一列宽度为20像素
    # bold = workbook.add_format({'bold': True})  # 设置一个加粗的格式对象

    xx = ['一样', '读音一样', '相似']
    row = 0
    for result_index in range(len(results) - 2):
        result = results[result_index]
        worksheet.write(row, 2, xx[result_index])
        for i in result:
            worksheet.write(row, 0, i[0])
            worksheet.write(row, 1, i[1])
            row += 1

    worksheet.write(row, 2, '其他')
    _row = row
    for i in results[-2]:
        worksheet.write(_row, 0, i)
        _row += 1

    for i in results[-1]:
        worksheet.write(row, 1, i)
        row += 1


    workbook.close()


if __name__ == '__main__':
    a = ["23", '24', '233', '435', 't43g', 'r3f', '我得', '我的啊', '今天', '和']
    b = ["23", '24', '23', '435', 't3g', 'r3f', '我德', '我德分', '果然', '很']
    result = get_compare_result(a, b)
    # print(result)
    # for i in [0]:
    #     print(i)

    # result = get_compare_result(*open_excel(1))
    print(result)
    write_excel(result)

    # print(result)
