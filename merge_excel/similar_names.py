from difflib import SequenceMatcher
from functools import partial, reduce
from typing import List

import pypinyin


def get_similarity(s1: str, s2: str, isjunk=None) -> float:
    """
    返回两个字符串的相似程度
    """
    return SequenceMatcher(isjunk, s1, s2).quick_ratio()


# 带声调的(默认)
def get_pinyin(word: str) -> List[str]:
    """
    汉字转换成拼音

    可能有多音字,所以输出为list
    诗书继世长 -> ['shīshūjìshìzhǎng', 'shīshūjìshìcháng']
    """
    return reduce(lambda x, y: [i+j for i in x for j in y], pypinyin.pinyin(word, heteronym=True), [''])


def get_name_similarity(name1: str, name2: str) -> float:
    """
    返回两个名字的最大相似度， 根据名字和读音两者判断取较大值
    """
    name_similarity = get_similarity(name1, name2)
    pinyin_similarity = max([get_similarity(i, j) for i in get_pinyin(name1) for j in get_pinyin(name2)])
    return name_similarity if name_similarity > pinyin_similarity else pinyin_similarity


def get_pinyin_similarity(name1: str, name2: str) -> float:
    return max([get_similarity(i, j) for i in get_pinyin(name1) for j in get_pinyin(name2)])


if __name__ == "__main__":
    print(get_pinyin("诗书继世长"))
    print(get_pinyin_similarity("我的", "我德"))
    print(get_pinyin("我的"))
    print(get_pinyin("我德"))
