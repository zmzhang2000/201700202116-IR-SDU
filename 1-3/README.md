# IR Evaluation
## 任务
实现以下指标评价，并对Homework1.2检索结果进行评价
* Mean Average Precision (MAP)
* Mean Reciprocal Rank (MRR)
* Normalized Discounted Cumulative Gain (NDCG)
## Deadline
2019.11.8 晚10点

---

## 数据文件
* tweets.txt (数据集，包含tweet内容和id)
* topic.desc.MB171-225.txt (测试查询关键词)
* qrels2014.txt (测试查询的ground truth，包括每个文档的gain)
## 输出文件
* result.txt (用于测试代码是否可以正常运行的输出)
* best_result.txt (根据ground truth的gain排序后的结果)
* my_result_[SMART notation].txt (根据homework1.2产生的检索结果)
## MRR metric实现
* 对于每个query
    * 查找结果中第一个相关文档的位置k
    * query的RR为1/k
* 取所有query的RR的均值为MRR
```python
def MRR_eval(qrels_dict, test_dict, k=100):
    RR_result = []
    for query in qrels_dict:
        true_list = sorted(list(qrels_dict[query].items()), key=lambda x: x[1], reverse=True)
        true_list = [x[0] for x in true_list]
        test_result = test_dict[query]
        length_use = min(k, len(test_result))
        if length_use <= 0:
            print('query ', query, ' not found test list')
            return []
        else:
            k_rank = 0
            for idx, doc_id in enumerate(test_result[:length_use]):
                if doc_id in true_list:
                    k_rank = idx + 1
                    break
            if k_rank > 0:
                RR_result.append(1 / k_rank)
            else:
                RR_result.append(0)
        # print('query', query, ', RR: ', RR_result[-1]) # 打印每个样本的分数
    return np.mean(RR_result)
```
## 评测结果
```
result test:
MAP = 0.6148422817122279
MRR = 0.79737012987013
NDCG = 0.756819929645465

best result test:
MAP = 0.7480226976538059
MRR = 1.0
NDCG = 1.0

my result (lnc.ltn) :
MAP = 0.5421879440165703
MRR = 0.990909090909091
NDCG = 0.7178485955905279

my result (bpc.ltn) :
MAP = 0.529056839925935
MRR = 0.9541125541125542
NDCG = 0.7016120137074677

my result (lnn.lnn) :
MAP = 0.4914672030273702
MRR = 0.9530303030303031
NDCG = 0.6935234146946007
```