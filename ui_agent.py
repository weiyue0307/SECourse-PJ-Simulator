__author__ = 'weiyue'
#  -*- coding:utf-8 -*-

import random
from ui_strategy import Strategy

class Agent:
    def __init__(self):
        self.strategies = []
        self.credit = 0
        self.record = []


    def add_strategy(self, strategy):
        self.strategies.append(strategy)


    def next_decision(self, previous_series):
        best_index = self.get_best_strategy()
        return self.strategies[best_index].next_decision(previous_series)

    def get_best_strategy(self):
        self.strategies.sort(key = lambda x: x.get_score(), reverse = True)
        score = self.strategies[0].get_score()
        for i in range (len(self.strategies)):
            if self.strategies[i].get_score() != score:
                break
            i += 1
        return random.randint(0, i-1)


    def update_strategy(self, previous_series, minority_choice):
        if self.next_decision(previous_series) == minority_choice:
            self.credit += 1
        self.record.append(self.credit)
        for strategy in self.strategies:
            strategy.update(previous_series, minority_choice)




