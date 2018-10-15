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

from synonym import Synonym


def main():
    # 定义同义词库的存放路径
    synonym_file_path = os.path.join('output',  'synonym.pkl')
    if not os.path.exists('output'):
        os.makedirs('output')

    # 载入/建立 同义词库
    syn = Synonym()
    if os.path.exists(synonym_file_path):
        syn.load(synonym_file_path)
        print('载入同义词库完毕。共有{}组同义词\n'.format(len(syn.word2idx)))
    else:
        syn.add_synonym(os.path.join('synonym_data', '哈工大同义词林.txt'))
        print('添加同义词表 完毕。目前共有{}组同义词'.format(len(syn.word2idx)))
        syn.save(synonym_file_path)
        print('保存同义词库完毕。\n')

    # test
    test_word = ['开心', '系统', '啥', '拜倒', '是']
    for word in test_word:
        print('{}的同义词是 {}'.format(word, syn.query_synonym(word)))

    print(syn.judge_synonym('开心', '高兴'))
    print(syn.judge_synonym('开心', '不开心'))


if __name__ == "__main__":
    main()

