# -*- coding: utf-8 -*-

'''
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   dialogue_predict.py
 
@Time    :   2019-11-06 14:25
 
@Desc    :
 
'''

import pathlib
import os
import tensorflow as tf

from Chatbot_Retrieval_model.QA.FAQ import FAQ
from Chatbot_Retrieval_model.Bert_sim.run_similarity import BertSim   # Bert语义相似度
from Chatbot_Retrieval_model.Domain.Domain_predict import Bert_Class

from Chatbot_Retrieval_model.util.logutil import Logger


baseDir = str(pathlib.Path(os.path.abspath(__file__)).parent.parent.parent)

loginfo = Logger('FAQ_log', 'info')

data = baseDir + '/data/FAQ/FAQ.txt'

bs = BertSim()
bs.set_mode(tf.estimator.ModeKeys.PREDICT)

bc = Bert_Class()

def get_anwser(msg):

    robot = FAQ(data, usedVec=False)

    anwser = robot.answer(msg, 'simple_pos')

    sen2 = '我想买保险'
    predict = bs.predict(msg, sen2)
    result = predict[0][1]

    bc_result = bc.predict_on_pb(msg)
    print(result, bc_result)

    return anwser

def estimate_answer(candidate, answer):
    '''
    评估答案，暂时不用
    :param candidate:
    :param answer:
    :return:
    '''
    candidate = candidate.strip().lower()
    answer = answer.strip().lower()
    if candidate == answer:
        return True

    if not answer.isdigit() and candidate.isdigit():
        candidate_temp = "{:.5E}".format(int(candidate))
        if candidate_temp == answer:
            return True
        candidate_temp == "{:.4E}".format(int(candidate))
        if candidate_temp == answer:
            return True

    return False




# msg = '预算14万内买什么车好呢？'
# get_anwser(msg)

if __name__ == '__main__':
    sentence1 = '你多大了？'
    sentence2 = '你今年几岁'
    predict = bs.predict(sentence1, sentence2)
    print(predict[0][1])