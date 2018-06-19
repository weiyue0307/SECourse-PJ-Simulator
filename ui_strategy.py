__author__ = 'weiyue'
#  -*- coding:utf-8 -*-

from itertools import product
from random import randint

class StrategyTable:
    def __init__(self, m):
        self.m = m
        # create strategy table
        self.generator = self.generator()

    def generator(self):
        return [list(i) for i in product([0,1], repeat = self.m)]

    # create score for strategies
    def score_init(self):
        total_bits = 2**self.m
        scores_choices = [-1,1]
        return [scores_choices[randint(0,1)] for _ in range(total_bits)]


class Strategy:
    def __init__(self, decision_map):
        self.score = 0
        self.decision_map = decision_map
        #self.previous_series_index = randint(0, 2 ** m - 1)

    def get_score(self):
        return self.score

    def next_decision(self, previous_series):
        return self.decision_map[previous_series]

    def update(self, previous_series, minority_decison):
        if self.next_decision(previous_series) == minority_decison:
            self.score +=1
        else:
            self.score -=1


if __name__ == '__main__':
    m=3
    ST = StrategyTable( m )
    test = [0, 1, 0]
    mygenerator = ST.generator
    print(mygenerator)
    print (ST.score_init())





