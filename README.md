# 同义词库

## 简介
目标是将单词分组，并且每组里的单词基本同义。每组单词的同义词都映射为该组单词里的主词。  
提供查询同义词、判断同义词的简单接口。  

## 目前的词库
- 哈工大同义词词林扩展版。

## 建立同义词库的逻辑
#### 主词的定义：
同组的同义词被查询时，都映射为该词。
#### 建立同义词库时:
- 建立一个映射表，将每个单词都映射为 所处同义词组中的主词。
- 新增一组同义词时，如果 主词 已在同义词库中：  
    那么取消之前建立的该主词的映射关系，重新设置映射关系。
- 新增一组同义词时，如果 主词之外的词 已在同义词库中：  
    那么不处理，依然保持之前的映射关系。
##### 例子：
    1. 这个 这 此 斯 是 之 者 夫 其一 以此
    2. 正确 对 是 然 不错 无误 对头 得法 科学 不利 不易 无可非议 无可指责
    3. 是 为 乃 系 则 属  
##### 说明：  
以上有三组同义词，针对“是”这个字的情况：  
如果只有第一组同义词存在，那么“是”将映射为“这个”；  
如果第一组和第二组同义词同时存在，那么“是”将映射为“这个”；  
如果三组同义词都存在，那么“是”将映射为“是”。（作为主词）

## 使用步骤
**使用方法demo详见sample.py**  

没有同义词库的情况：  
 - 先add新同义词表, 然后save。（save后，生成的同义词库会保存在output/synonym.pkl）

已有同义词库的情况：  
 - 直接load即可。
 
 ## 可能存在的问题
 单词的词性不同，意义可能不同。（没有找到case, 不过可能有这个问题。而且这块暂时不好解决）