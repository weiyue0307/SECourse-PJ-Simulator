__author__ = 'weiyue'
#  -*- coding:utf-8 -*-

from ui_strategy import Strategy, StrategyTable
from ui_agent import Agent
from random import randint
import pylab
import sys

class Game:
    def __init__(self, T, n, m, s):
        self.T = T  # T: total steps
        self.n = n  # n: the number of agents
        self.m = m  # m: the length of memory
        self.s = s  # s: the number of sample strategies

        self.agents = [Agent() for _ in range(n)]
        self.user = Agent()
        self.choice = -1
        self.strategytable = StrategyTable(self.m)
        self.decisions = []
        self.minority_decisions = []
        self.previous_index = randint( 0, 2**m -1)

        for agent in self.agents:
            for i in range(s):
                strategy = Strategy(self.strategytable.score_init())
                agent.add_strategy(strategy)
                #print(strategy.decision_map)

        for i in range(s):
            strategy = Strategy(self.strategytable.score_init())
            self.user.add_strategy(strategy)

    def collect_decisions(self):
        # When everyone has chosen, the system begin to collect the results
        choices = [0, 0, 0]
        choices[self.choice] += 1
        for agent in self.agents:
            choices[agent.next_decision(self.previous_index)] += 1
        self.decisions.append((choices[-1], choices[1], choices[0]))
        #print(self.decisions)

    def record_current_conditions(self):
        self.minority_decisions.append(self.get_minority_decision())
        return self.minority_decisions[-1]

    def next_step(self):
        self.collect_decisions()
        winning_decision = self.record_current_conditions()
        if self.choice != 0:
            if winning_decision == self.choice:
                print("Good Choice!")
            else:
                print("Bad Choice!")
        # update the score of the agents & strategies
        self.update_agents(winning_decision)
        self.update_previous_series(winning_decision)

    def get_minority_decision(self):
        # Get the real minority decision of this step
        if self.decisions[-1][0] > self.decisions[-1][1]:
            return 1 # illustrate the people of going to the bar win the game
        else:
            return -1

    def update_agents(self, winning_decision):
        for agent in self.agents:
            agent.update_strategy(self.previous_index, winning_decision)
        return winning_decision

    def update_previous_series(self, winning_decision):
        # leave out the oldest record of the memory, add the new decision at the last position
        self.previous_index = self.previous_index << 1
        self.previous_index &= ~(1 << self.m)
        if winning_decision == 1:
            self.previous_index |= 1
        else:
            self.previous_index |= 0

    def run(self):
        for i in range(self.T):
            print("Please make your choice: Go: Please input 1; Not Go: Please input -1")
            print("If you want to pause the game and see some details, please input 0")
            print("If you want yo exit, please input 'quit'")
            self.choice = input()
            if self.choice == "quit":
                sys.exit()
            while True:
                #if self.choice.isdigit():
                self.choice = int(self.choice)
                if self.choice in {0, 1, -1}:
                    break
                print("The number is illegal, please input int number again")
                print("If you want yo exit, please input 'quit'")
                self.choice = input()

            if self.choice == 0:
                flag = 0
                self.plot(i)
                print("The past Good choices are: ", self.minority_decisions)
                print("If you want to check one agent's strategies and credit, please input his number(from 1 to", n, "), else input -2 to return to the game")
                print("If you want yo exit, please input 'quit'")
                number = input()
                if number == "quit":
                    sys.exit()
                if number == "-2":
                    flag = 1
                #else:
                while (flag == 0 and not number.isdigit()):
                    if number == "quit":
                        sys.exit()
                    if number == "-2":
                        break
                    print("The number is illegal, please input int number again")
                    print("If you want yo exit, please input 'quit'")
                    number = input()
                number = int(number)-1
                while(flag == 0 and number>0):
                    print("This agent's credit is",self.agents[number].credit)
                    self.agents[number].strategies.sort(key = lambda x: x.get_score(), reverse = True)
                    score = [self.agents[number].strategies[i].get_score() for i in range(s)]
                    print("This agent's strategies' credit is", score)
                    print("If you want to continue to check, please input the agent's number(from 1 to", n, "), else input -2 to return to the game")
                    print("If you want yo exit, please input 'quit'")
                    number = input()
                    if number == "quit":
                        sys.exit()
                    if number == "-2":
                        break
                    while (not number.isdigit()):
                        if number == "quit":
                            sys.exit()
                        if number == "-2":
                            break
                        print("The number is illegal, please input agent's number(int) again")
                        print("If you want yo exit, please input 'quit'")
                        number = input()
                    number = int(number) - 1

            self.next_step()

    def print_result(self):
        total = 0.0
        half_n = self.n / 2.0
        for result in self.decisions:
            total += (half_n - result[0]) ** 2 + (half_n - result[1]) ** 2
        total /= 2 * self.T
        total = total ** 0.5
        print("var=", total)

    def plot(self, t):
        # plot the relation of The number of people in the Bar and the Steps
        y = [result[1] for result in self.decisions]
        x = [i for i in range(t)]
        #pylab.xlim(1,n)
        pylab.figure()
        pylab.xlabel('Steps(Total is 20)')
        pylab.ylabel('The number of people in the Bar(Total is 20)')
        pylab.plot(x,y)
        pylab.show()
        # plot the relation of Everyone's credits and Steps
        namelist = ['User'+ str(i+1) for i in range(n)]
        plotlist = []
        for agent in self.agents:
            plot1,=pylab.plot(x, agent.record)
            plotlist.append(plot1)
        pylab.legend(plotlist, namelist, loc = 'upper right', shadow = True)
        pylab.show()


if __name__ == '__main__':
    # In this project, we choose to let the user input the value of 'T, n, m, s'
    #T = 20
    #n = 10
    #m = 3
    #s = 4
    print("please input the number(int) of 'T': Total steps, (1<T<=10000)")
    print("If you want yo exit, please input 'quit'")
    T = input()
    while( not T.isdigit() or int(T)>10000 or int(T)<2):
        if T == "quit":
            sys.exit()
        print("The number is illegal, please input again, (1<T<=10000)")
        print("If you want yo exit, please input 'quit'")
        T = input()
    T = int(T)

    print("please input the number(int) of 'n': The number of agents, (1<n<=100)")
    print("If you want yo exit, please input 'quit'")
    n = input()
    while(not n.isdigit() or int(n) > 100 or int(n) < 2):
        if n == "quit":
            sys.exit()
        print("The number is illegal, please input again, (1<n<=100)")
        print("If you want yo exit, please input 'quit'")
        n = input()
    n = int(n)

    print("please input the number(int) of 'm': The length of the memory, (1<m<=10)")
    print("If you want yo exit, please input 'quit'")
    m = input()
    while(not m.isdigit() or int(m) > 10 or int(m) < 2):
        if m == "quit":
            sys.exit()
        print("The number is illegal, please input again, (1<m<=10)")
        print("If you want yo exit, please input 'quit'")
        m = input()
    m = int(m)

    print("please input the number(int) of 's': The number of sample strategies, (1<s<=",2**m, ")")
    print("If you want yo exit, please input 'quit'")
    s = input()
    while(not s.isdigit() or int(s) > 2**m or int(s) < 2):
        if s == "quit":
            sys.exit()
        print("The number is illegal, please input again, (1<s<=",2**m, ")")
        print("If you want yo exit, please input 'quit'")
        s = input()
    s = int(s)

    mg = Game(T, n, m, s)
    mg.run()
    #mg.plot()


