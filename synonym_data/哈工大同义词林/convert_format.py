# -*- coding: utf-8 -*-
"""
@author: weijiawei
@date: 2018/10/15
"""
import os
import re
from collections import Counter
import numpy as np
import pandas as pd

if __name__ == "__main__":
    input_path = os.path.join('哈工大信息检索研究中心同义词词林扩展版.txt')
    output_path = os.path.join('..', '哈工大同义词林.txt')

    # 不同的语料，建立的方式应该不一样
    word_cnt = Counter()
    # 载入哈工大同义词林(gbk格式）
    with open(input_path, 'r', encoding='GBK') as fin, open(output_path, 'w', encoding='utf8') as fout:
        for line in fin:  # 读取一行
            # 取出符号（=, @, #）
            match_obj = re.match(r'[\w]+([=@#]) (.*)', line)
            token = match_obj.group(1)  # 符号
            line = match_obj.group(2)  # 同义词组
            # print(line)
            if token != '=':
                continue

            # 区分出主词 和 其他词
            words = line.split()
            main_word = words[0]  # 同义词统一映射为该词
            words = words[1:]  # 其他同义词
            # 临时统计词频
            # for word in words:
            #     word_cnt[word] += 1

            # 保存至输出文件
            fout.write('{} {}\n'.format(main_word, ' '.join(words)))
    # 临时查看词频大于1d的词
    # for k, v in word_cnt.items():
    #     if v > 1:
    #         print((k, v))
