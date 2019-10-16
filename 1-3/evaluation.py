import math
import numpy as np


def generate_tweetid_gain(file_name):
    qrels_dict = {}
    with open(file_name, 'r', errors='ignore') as f:
        for line in f:
            ele = line.strip().split(' ')
            if ele[0] not in qrels_dict:
                qrels_dict[ele[0]] = {}
            # here we want the gain of doc_id in qrels_dict > 0,
            # so it's sorted values can be IDCG groundtruth
            if int(ele[3]) > 0:
                qrels_dict[ele[0]][ele[2]] = int(ele[3])
    return qrels_dict


def read_tweetid_test(file_name):
    # input file format
    # query_id doc_id
    # query_id doc_id
    # query_id doc_id
    # ...
    test_dict = {}
    with open(file_name, 'r', errors='ignore') as f:
        for line in f:
            ele = line.strip().split(' ')
            if ele[0] not in test_dict:
                test_dict[ele[0]] = []
            test_dict[ele[0]].append(ele[1])
    return test_dict


def MAP_eval(qrels_dict, test_dict, k=100):
    AP_result = []
    for query in qrels_dict:
        test_result = test_dict[query]
        true_list = set(qrels_dict[query].keys())
        # print(len(true_list))
        # length_use = min(k, len(test_result), len(true_list))
        length_use = min(k, len(test_result))
        if length_use <= 0:
            print('query ', query, ' not found test list')
            return []
        P_result = []
        i = 0
        i_retrieval_true = 0
        for doc_id in test_result[0: length_use]:
            i += 1
            if doc_id in true_list:
                i_retrieval_true += 1
                P_result.append(i_retrieval_true / i)
                # print(i_retrieval_true / i)
        if P_result:
            AP = np.sum(P_result) / len(true_list)
            # print('query:', query, ',AP:', AP) # 打印每个样本的分数
            AP_result.append(AP)
        else:
            # print('query:', query, ' not found a true value') # 打印每个样本的分数
            AP_result.append(0)
    return np.mean(AP_result)


def NDCG_eval(qrels_dict, test_dict, k=100):
    NDCG_result = []
    for query in qrels_dict:
        test_result = test_dict[query]
        # calculate DCG just need to know the gains of groundtruth
        # that is [2,2,2,1,1,1]
        true_list = list(qrels_dict[query].values())
        true_list = sorted(true_list, reverse=True)
        i = 1
        DCG = 0.0
        IDCG = 0.0
        # maybe k is bigger than arr length
        length_use = min(k, len(test_result), len(true_list))
        if length_use <= 0:
            print('query ', query, ' not found test list')
            return []
        for doc_id in test_result[0: length_use]:
            i += 1
            rel = qrels_dict[query].get(doc_id, 0)
            DCG += (pow(2, rel) - 1) / math.log(i, 2)
            IDCG += (pow(2, true_list[i - 2]) - 1) / math.log(i, 2)
        NDCG = DCG / IDCG
        # print('query', query, ', NDCG: ', NDCG) # 打印每个样本的分数
        NDCG_result.append(NDCG)
    return np.mean(NDCG_result)


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


def evaluation():
    k = 100
    # query relevance file
    file_qrels_path = 'data/qrels.txt'
    # qrels_dict = {query_id:{doc_id:gain, doc_id:gain, ...}, ...}
    qrels_dict = generate_tweetid_gain(file_qrels_path)
    # ur result, format is in function read_tweetid_test, or u can write by ur own

    # 测试示例
    file_test_path = 'result/result.txt'
    # test_dict = {query_id:[doc_id, doc_id, ...], ...}
    test_dict = read_tweetid_test(file_test_path)
    print("result test:")
    MAP = MAP_eval(qrels_dict, test_dict, k)
    print('MAP', ' = ', MAP, sep='')
    MRR = MRR_eval(qrels_dict, test_dict, k)
    print('MRR', ' = ', MRR, sep='')
    NDCG = NDCG_eval(qrels_dict, test_dict, k)
    print('NDCG', ' = ', NDCG, sep='')
    print('\n')

    # 测试最佳结果
    file_test_path = 'result/best_result.txt'
    # test_dict = {query_id:[doc_id, doc_id, ...], ...}
    test_dict = read_tweetid_test(file_test_path)
    print("best result test:")
    MAP = MAP_eval(qrels_dict, test_dict, k)
    print('MAP', ' = ', MAP, sep='')
    MRR = MRR_eval(qrels_dict, test_dict, k)
    print('MRR', ' = ', MRR, sep='')
    NDCG = NDCG_eval(qrels_dict, test_dict, k)
    print('NDCG', ' = ', NDCG, sep='')
    print('\n')

    # 测试我的输出
    my_result_path = 'result/my_result_lnc.ltn.txt'
    test_dict = read_tweetid_test(my_result_path)
    print("my result (lnc.ltn) :")
    MAP = MAP_eval(qrels_dict, test_dict, k)
    print('MAP', ' = ', MAP, sep='')
    MRR = MRR_eval(qrels_dict, test_dict, k)
    print('MRR', ' = ', MRR, sep='')
    NDCG = NDCG_eval(qrels_dict, test_dict, k)
    print('NDCG', ' = ', NDCG, sep='')
    print('\n')

    # 测试我的输出
    my_result_path = 'result/my_result_bpc.ltn.txt'
    test_dict = read_tweetid_test(my_result_path)
    print("my result (bpc.ltn) :")
    MAP = MAP_eval(qrels_dict, test_dict, k)
    print('MAP', ' = ', MAP, sep='')
    MRR = MRR_eval(qrels_dict, test_dict, k)
    print('MRR', ' = ', MRR, sep='')
    NDCG = NDCG_eval(qrels_dict, test_dict, k)
    print('NDCG', ' = ', NDCG, sep='')
    print('\n')

    # 测试我的输出
    my_result_path = 'result/my_result_lnn.lnn.txt'
    test_dict = read_tweetid_test(my_result_path)
    print("my result (lnn.lnn) :")
    MAP = MAP_eval(qrels_dict, test_dict, k)
    print('MAP', ' = ', MAP, sep='')
    MRR = MRR_eval(qrels_dict, test_dict, k)
    print('MRR', ' = ', MRR, sep='')
    NDCG = NDCG_eval(qrels_dict, test_dict, k)
    print('NDCG', ' = ', NDCG, sep='')
    print('\n')

if __name__ == '__main__':
    evaluation()
