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
