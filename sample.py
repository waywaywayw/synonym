# -*- coding: utf-8 -*-
"""
@author: weijiawei
@date: 2018/10/12
"""

import os
import re
import numpy as np
import pandas as pd
import pickle

from synonym import synonym_DB


def main():
    synonym_DB_name = 'synonym.pkl'
    synonym_DB_path = os.path.join('output', synonym_DB_name)
    syn = synonym_DB()

    # 载入/建立 同义词库
    if os.path.exists(synonym_DB_path):
        print('载入 同义词库完毕..')
        syn.load_DB(synonym_DB_path)
    else:
        syn.build_DB(os.path.join('synonym_data', '哈工大信息检索研究中心同义词词林扩展版.txt'))
        syn.save_DB(synonym_DB_path)
        print('建立并保存 同义词库完毕..')

    # test
    test_word = ['开心', '人才', '啥', '拜倒']
    for word in test_word:
        print('{}的同义词是 {}'.format(word, syn.query_synonym(word)))

    print(syn.judge_synonym('开心', '高兴'))
    print(syn.judge_synonym('开心', '不开心'))


if __name__ == "__main__":
    main()

