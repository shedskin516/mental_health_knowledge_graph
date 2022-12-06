import math

def get_DCG(groundtruth, pred_rank_list, k):
    dcg = 0
    groundtruth = list(map(lambda x: x.lower(), groundtruth))
    pred_rank_list = list(map(lambda x: x.lower(), pred_rank_list))

    for index, pred in enumerate(pred_rank_list):
        if index >= k:
            break
        if pred in groundtruth:
            dcg += (1) / math.log(index + 1 + 1, 2)

    idcg = 0
    num_item = int(min(k, len(groundtruth)))
    for i in range(num_item):
        idcg += (1) / math.log(i + 1 + 1, 2)
    ndcg = dcg / idcg

    return ndcg 


def get_recall(groundtruth, pred_rank_list, k):
    recall = 0
    groundtruth = list(map(lambda x: x.lower(), groundtruth))
    pred_rank_list = list(map(lambda x: x.lower(), pred_rank_list))

    for index, pred in enumerate(pred_rank_list):
        if index >= k:
            break
        if pred in groundtruth:
            recall += 1
    
    num_item = min(k, len(groundtruth))
    recall = float(recall) / num_item

    return recall


def evaluationWithK(gt, pred, k):
    recall = get_recall(gt, pred, k)
    dcg = get_DCG(gt, pred, k)

    print("recall@" + str(k) + ": " + str(recall))
    print("dcg@" + str(k) + ": " + str(dcg))
    return recall, dcg


def evaluation(gt, pred):
    recall3, dcg3 = evaluationWithK(gt, pred, 3)
    recall5, dcg5 = evaluationWithK(gt, pred, 5)
    recall10, dcg10 = evaluationWithK(gt, pred, 10)
    return recall3, dcg3, recall5, dcg5, recall10, dcg10


gt = ['school issues', 'impulse control disorders', 'anger management']
pred = ['anger management', 'stress', 'grief', 'parenting', 'school issues', 'impulse control disorders', 'emotional disturbance', 'anger management', 'depression', 'school issues']
evaluation(gt, pred)
