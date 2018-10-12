# -*- coding: utf-8 -*-
"""
@author: weijiawei
@date: 2018/10/12
"""
import os
import re
import copy
import numpy as np
import pandas as pd
import pickle
from collections import Counter


class synonym_DB(object):
    """
    使用并查集建立同义词库
    """
    def __init__(self):
        self._union_find = []    # 定义并查集
        self._word2idx = {}     # 单词形式 -> id形式
        self._idx2word = {}     # id形式 -> 单词形式
        pass

    def build_DB(self, input_path, encoding='GBK'):
        """
        建立同义词库。
        :param input_path: 同义词语料地址
        :return:
        """
        # 不同的语料，建立的方式应该不一样
        word_cnt = Counter()
        # 载入哈工大同义词林(gbk格式）
        with open(input_path, 'r', encoding=encoding) as fin:
            for line in fin:    # 读取一行
                # 取出符号（=, @, #）
                match_obj = re.match(r'[\w]+([=@#]) (.*)', line)
                token = match_obj.group(1)  # 符号
                line = match_obj.group(2)   # 同义词组
                # print(line)
                if token !='=': continue
                # 区分出主词 和 其他词
                words = line.split()
                # 临时统计词频
                # for word in words:
                #     word_cnt[word] += 1
                main_word = words[0]    # 同义词统一映射为该词
                words = words[1:]   # 其他同义词

                # 添加进字典和并查集
                # 先添加主词
                if main_word not in self._word2idx.keys():  # main_word还不在字典中的情况
                    current_id = len(self._union_find)
                    self._word2idx[main_word] = current_id  # 添加进字典
                    main_id = current_id
                    self._union_find.append(main_id)    # main_word在并查集中的id为main_id
                else:
                    main_id = self._word2idx[main_word] # 如果main_word已经在词典中，直接取出对应id
                # 再添加其他词
                for word in words:
                    if word not in self._word2idx.keys():
                        current_id = len(self._union_find)
                        self._word2idx[word] = current_id  # 添加进字典
                        self._union_find.append(main_id)  # 其他同义词在并查集中的id为main_id
                    else:
                        pass    # 已经存在了。就不管了。。
        # 计算idx2word
        for word, idx in self._word2idx.items():
            self._idx2word[idx] = word
        # 临时显示词频
        # for k, v in word_cnt.items():
        #     if v > 1:
        #         print((k, v))

    def load_DB(self, input_path):
        """载入同义词库"""
        with open(input_path, 'rb') as fin:
            obj = pickle.load(fin)
            self._union_find = obj._union_find
            self._word2idx = obj._word2idx
            self._idx2word = obj._idx2word

    def save_DB(self, save_path):
        """保存同义词库"""
        with open(save_path, 'wb') as fout:
            pickle.dump(self, fout)

    def query_synonym(self, word):
        """
        查询给定单词的同义词。（同组的单词，返回的同义词保证相同）
        :param word: 查询单词
        :return: 查询成功，返回单词的同义词；查询失败，返回None
        """
        wid = self._word2idx.get(word, None)  # 找到查询单词的id
        if wid == None:  # 不存在同义词库中
            return None
        else:
            main_id = self._union_find[wid]  # 找到该单词 在同义词组中的主词的id
            ret_word = self._idx2word[main_id]  # 找到主词id对应的词
            return ret_word

    def judge_synonym(self, word1, word2):
        """
        判断两个单词是否为同义词。
        :return: True or False
        """
        w1id = self._word2idx.get(word1, None)
        w2id = self._word2idx.get(word2, None)
        if w1id == None or w2id ==None:  # 不存在同义词库中
            return False
        else:
            main1_id = self._union_find[w1id]
            main2_id = self._union_find[w2id]
            if main1_id==main2_id:
                return True
            else:
                return False

