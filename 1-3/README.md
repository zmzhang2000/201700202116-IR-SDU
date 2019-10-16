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
* 对已经实现的**所有SMART notation**进行组合并检索，分别选取**MAP, MRR, NDCG最高**的SMART notation，得到如下结果
```
MAP最高的SMART notation为：ann.npn
MAP = 0.5450475431272652
MRR = 0.9698701298701299
NDCG = 0.7246718992202057

MRR最高的SMART notation为：lnc.ntn
MAP = 0.5421879440165703
MRR = 0.990909090909091
NDCG = 0.7178485955905279

NDCG最高的SMART notation为：ann.ntn
MAP = 0.5444353423293059
MRR = 0.9698701298701299
NDCG = 0.7246718992202057
```
* 其他SMART notation评测示例(**全部评测结果见get_query_result.ipynb**)
```
nnn.nnn: 
MAP = 0.462935118027406
MRR = 0.9312801484230055
NDCG = 0.6591187301857276
nnn.nnc: 
MAP = 0.462935118027406
MRR = 0.9312801484230055
NDCG = 0.6591187301857276
nnn.ntn: 
MAP = 0.5193173906812537
MRR = 0.956060606060606
NDCG = 0.7035308065001947
nnn.ntc: 
MAP = 0.5193173906812537
MRR = 0.956060606060606
NDCG = 0.7035308065001947
nnn.npn: 
MAP = 0.5202911054581345
MRR = 0.956060606060606
NDCG = 0.7043657469797785
nnn.npc: 
MAP = 0.5202911054581345
MRR = 0.956060606060606
NDCG = 0.7043657469797785
nnn.lnn: 
MAP = 0.462935118027406
MRR = 0.9312801484230055
NDCG = 0.6591187301857276
nnn.lnc: 
MAP = 0.462935118027406
MRR = 0.9312801484230055
NDCG = 0.6591187301857276
nnn.ltn: 
MAP = 0.5193173906812537
MRR = 0.956060606060606
NDCG = 0.7035308065001947
nnn.ltc: 
MAP = 0.5193173906812537
MRR = 0.956060606060606
NDCG = 0.7035308065001947
nnn.lpn: 
MAP = 0.5202911054581345
MRR = 0.956060606060606
NDCG = 0.7043657469797785
nnn.lpc: 
MAP = 0.5202911054581345
MRR = 0.956060606060606
NDCG = 0.7043657469797785
nnn.ann: 
MAP = 0.462935118027406
MRR = 0.9312801484230055
NDCG = 0.6591187301857276
nnn.anc: 
MAP = 0.462935118027406
MRR = 0.9312801484230055
NDCG = 0.6591187301857276
nnn.atn: 
MAP = 0.5193173906812537
MRR = 0.956060606060606
NDCG = 0.7035308065001947
nnn.atc: 
MAP = 0.5193173906812537
MRR = 0.956060606060606
NDCG = 0.7035308065001947
nnn.apn: 
MAP = 0.5202911054581345
MRR = 0.956060606060606
NDCG = 0.7043657469797785
nnn.apc: 
MAP = 0.5202911054581345
MRR = 0.956060606060606
NDCG = 0.7043657469797785
nnn.bnn: 
MAP = 0.462935118027406
MRR = 0.9312801484230055
NDCG = 0.6591187301857276
```