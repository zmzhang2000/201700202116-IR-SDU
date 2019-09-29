# Inverted index and Boolean Retrieval Model
## 任务
* 使用我们介绍的方法，在 tweets 数据集上构建 inverted index
* 实现 Boolean Retrieval Model ，使用 TREC 2014 test
topics 进行测试
* Boolean Retrieval Model
    * Input a query (like Ron and Weasley)
    * Output: print the qualified tweets
    * 支持 and, or ,not ；查询优化可以选做
## 注意
* 对于 tweets 与 queries 使用相同的预处理
## Deadline
2019.10.11 晚10点

---

## **实验步骤**
1. 将文本文件加载为json格式的items，方便提取text内容
2. text预处理
    * 大写转小写
    * 分词（使用nltk的word_tokenize）
    * 去除标点符号和停用词
3. 统计每个document出现的词，建立词典
    * 每个term对应一个集合，集合中的元素为包含这个term的文档编号
    * 可利用集合的交并补进行合并
4. 查询语句预处理
    * 大写转小写
    * 分词
    * 去除标点符号 **(不包括运算符)** 和停用词
    * 将" not ", "not", " - "转化为"-"
    * 将" or ", "or", " | "转化为"|"
    * 将" ", " and ", "and"转化为"&"
    * 其余词转化为dictionary['term']
    * 使用 **eval()** 将转化后的查询语句转化为python命令，得到查询结果
5. 查询交互
![](GUI.bmp)
6. 查询结果
![](query_result.bmp)
## tricks
* 使用python的字典数据结构来构建dictionary，提高查询效率
* 使用python的集合数据结构存储postings，提高交并补运算效率， **代码简洁**
## **详细代码及输出见inverted_index1.ipynb**

---
---
---

# 改进版 (inverted_index2.ipynb)
## 将postings的数据结构改为**链表**，即python中的list
## **定义有序list的 and or not 运算**
```
def union_list(l1, l2):
    result = []
    i = 0
    j = 0
    while (i < len(l1) and j < len(l2)):
        if l1[i] == l2[j]:
            result.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    for x in l1[i:]:
        result.append(x)
    for x in l2[j:]:
        result.append(x)
    return result

def intersection_list(l1, l2):
    result = []
    i = 0
    j = 0
    while (i < len(l1) and j < len(l2)):
        if l1[i] == l2[j]:
            result.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    return result

def difference_list(l1,l2):
    result = []
    i = 0
    j = 0
    while (i < len(l1) and j < len(l2)):
        if l1[i] == l2[j]:
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            j += 1
    for x in l1[i:]:
        result.append(x)
    return result
```
## 解析查询表达式，新增对于（）括号运算的支持
* 将and or not分别转化为& + -
* [中缀表达式转化为后缀表达式](https://blog.csdn.net/antineutrino/article/details/6763722)
## 输出中关键词加红强调
## 查询示例
* 已支持带括号的复杂查询
* 查询关键词进行了标红处理

![Ron AND Weasley OR ( Harry AND Potter NOT Birthday)](query_result2.png)
![hermione](query_result3.png)
![weasley or ron not ( Harry not potter )](query_result4.png)