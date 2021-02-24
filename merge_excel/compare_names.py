from typing import Tuple, List, TypeVar

from merge_excel.similar_names import get_pinyin_similarity, get_similarity

L = List[Tuple[str, str]]


def get_compare_result(names_1: list, names_2: list) -> List[L]:
    tmp_names_1 = names_1[:]
    tmp_names_2 = names_2[:]
    same_names: L = []  # 名字相同
    same_pinyin: L = []  # 读音相同
    similar_names_6: L = []  # 相似的名字 0.66
    similar_pinyin_6: L = []  # 相似的读音 0.66
    similar_names_5: L = []  # 相似的名字 0.5
    similar_pinyin_5: L = []  # 相似的读音 0.5

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
        for j in tmp_names_2[:]:
            if get_similarity(i, j) > 0.6:
                similar_names_6.append((i, j))
                tmp_names_1.remove(i)
                tmp_names_2.remove(j)

    for i in tmp_names_1[:]:
        for j in tmp_names_2[:]:
            if get_similarity(i, j) == 1:
                similar_names_6.append((i, j))
                tmp_names_1.remove(i)
                tmp_names_2.remove(j)



    return [same_names, same_pinyin,,, tmp_names_1, tmp_names_2]


    if __name__ == '__main__':
        a = ["23", '24', '233', '435', 't43g', 'r3f', '我得', '我的啊']
        b = ["23", '24', '23', '435', 't3g', 'r3f', '我德', '我德分']
        result = get_compare_result(a, b)
        print(result)
        # for i in [0]:
        #     print(i)
