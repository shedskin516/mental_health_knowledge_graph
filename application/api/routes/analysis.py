from flask import Blueprint, current_app, request, jsonify

from api.dao.therapist import TherapistDAO
from api.data import issues
# from api.data import user
from api.data import noUseKey

import numpy as np
from math import floor
 
def jaro_distance(s1, s2):
    if (s1 == s2):
        return 1.0
    len1 = len(s1)
    len2 = len(s2)
    max_dist = floor(max(len1, len2) / 2) - 1
    match = 0
    hash_s1 = [0] * len(s1)
    hash_s2 = [0] * len(s2)
    for i in range(len1):
        for j in range(max(0, i - max_dist),
                       min(len2, i + max_dist + 1)):
            if (s1[i] == s2[j] and hash_s2[j] == 0):
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break
 
    if (match == 0):
        return 0.0

    t = 0
    point = 0
    for i in range(len1):
        if (hash_s1[i]):
            while (hash_s2[point] == 0):
                point += 1
            if (s1[i] != s2[point]):
                t += 1
            point += 1
    t = t//2
 
    return (match/ len1 + match / len2 +
            (match - t) / match)/ 3.0

analysis_routes = Blueprint("analysis", __name__, url_prefix="/api/analysis")


def process_trouble(trouble):
    trouble = trouble.replace('.',' ').replace(',',' ')
    trouble = trouble.split(' ')
    user_dict = {}
    for w in trouble:
        if w != '' and w not in noUseKey:
            if w in user_dict.keys():
                user_dict[w] = user_dict[w]+1
            else:
                user_dict[w] = 1
    return user_dict


def getIssue(trouble):
    user = process_trouble(trouble)
    list = []
    for issue in issues:
        issueBoW = issues[issue]
        sum = 0
        for word in issueBoW:
            for word_user in user:
                c = jaro_distance(word_user, word)
                if c > 0.9:
                    sum += issueBoW[word]
        stat = [sum, issue]
        list.append(stat)

    list = np.array(list)
    list = np.flip(list[list[:,0].argsort()])
    res = []
    for index, item in enumerate(list):
        res.append(item[0])
        if index >= 2:
            break
    return res


# get disease detail by disease name
@analysis_routes.route('/', methods = ['POST', 'GET'])
def get_therapist():
    data = request.get_json()
    print(data)
    if data['trouble'] == '': return

    issues = getIssue(data['trouble'])

    dao = TherapistDAO(current_app.driver)
    output = dao.recommendTherapist(issues)

    return jsonify(output)

