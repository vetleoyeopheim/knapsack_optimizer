"""
Author: Vetle �ye Opheim
"""

import numpy as np
from numba import njit
import itertools


class Knapsack:
    """
    Class for solving 0-1 knapsack problems
    """

    def __init__(self, values, prices, item_num, budget):

        self.item_num = item_num
        self.values = values
        self.prices = prices
        self.budget = budget

        

    def all_quantities(self):
        """
        Return an array of all possible sets of quantities
        Used for brute force solutions for 
        """
        quantities = list(itertools.product([0,1], repeat = self.item_num))
        quantities = np.array(quantities)

        return quantities

    def calc_scores(self, quantities):
        scores = np.dot(quantities, self.values)
        return scores

    def calc_costs(self, quantities):
        costs = np.dot(quantities, self.prices)
        return costs

    def brute_force(self):

        quantities = self.all_quantities()
        scores = self.calc_scores(quantities)

        #Get the set of admissible quantities, those combinations where budget is smaller than or equal to cost. When cost > budget scores are set to 0
        admissible = np.where(cost <= self.budget, scores, 0)

        return (np.max(admissible), np.argmax(admissible), admissible)




    
        




