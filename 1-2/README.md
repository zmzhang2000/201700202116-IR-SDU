# Ranked Retrieval Model
## 任务
* 在 Homework 1.1 的基础上实现最基本的 Ranked Retrieval Model
    * Input: a query (like Ron Weasley birthday)
    * Output: Return the top K (e.g., K = 10) relevant tweets
* Use SMART notation: lnc.ltc
    * Document : logarithmic tf (l as first character), no idf and cosine normalization
    * Query: logarithmic tf (l in leftmost column), idf (t in second column), no normalization
* 改进 Inverted index
    * 在 Dictionary 中存储每个 term 的 DF
    * 在 posting list 中存储 term 在每个 doc 中的 TF with pairs (docID , tf)
* 选做
    * 支持所有的SMART Notations
## Deadline
2019.10.25 晚10点

---

## 已完成修改（Homeword1.1基础上）
1. posting增加tf信息
2. posting list 按tf由大到小排序

    ![posting list](posting_list.png)
3. postings融合时使用集合运算
4. query的分词由split()改为nltk.word_tokenize()
5. 预先计算每个文档的tf向量的L2范数
```
tokens = [preprocess(x) for x in tweets] # 每个doc的分词
length = [nltk.FreqDist(x) for x in tokens] # 每个doc的词频统计信息
length = [list(x.values()) for x in length] # 每个doc的tf向量
length = [math.sqrt(sum([tf*tf for tf in x])) for x in length] # 每个doc的tf向量的L2范数
```
6. 解析查询语句时直接分词，无需考虑and、or、not
7. 
