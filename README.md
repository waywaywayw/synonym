# 同义词库

## 简介
提供查询同义词、判断同义词的简单接口。  


## 目前词库
- 哈工大同义词词林扩展版。

## 添加新的同义词表的操作顺序
**样例方法详见sample.py**  
同义词库路径：output/synonym.pkl

没有同义词库的情况：  
 - 先add新同义词表, 最后save。（save后，生成的同义词库会保存在同义词库路径。

已有同义词库的情况：  
 - 直接load即可。然后再query_synonym。  