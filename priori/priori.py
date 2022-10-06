import argparse
import pandas as pd
import numpy as np
import random 
import pickle
from pathlib import Path
from collections import defaultdict

data = {'T1': ['C', 'D', 'E'], 'T2': ['B', 'C', 'D'], 'T3': ['A', 'C', 'D'], 'T4': ['A', 'C', 'D', 'E'], 'T5': ['A', 'B', 'C', 'D'], 'T6': ['B'], 'T7': ['D', 'E'], 'T8': ['A', 'B', 'C', 'D'], 'T9': ['A', 'B', 'D', 'E'], 'T10': ['A', 'B', 'C', 'D', 'E']}

import itertools
  
def findsubsets(s, n):
    
#   
#   Input: 
#       1. s - A python list of items
#       2. n - Size of each subset
#   Output:
#       1. subsets - A python list containing the subsets of size n.
    
    subsets = list(sorted((itertools.combinations(s,n))))
    return subsets

def items_from_frequent_itemsets(frequent_itemset):


#   to this code block
#   Input:
#       1. Frequent Itemsets
#   Output:
#       1. Sorted list of items

    items = list()
    for keys in frequent_itemset.keys():
        for item in list(keys):
            items.append(item)
    return sorted(list(set(items)))

def count_(dataset , list_items):
   c = 0
   for k,v in dataset.items():
      if all(item in v for item in list_items):
         c = c+1

   return c

def generate_frequent_itemsets(dataset, support, items, n=1, frequent_items={}):
    
#   Input:
#       1. dataset - A python dictionary containing the transactions.
#       2. support - A floating point variable representing the min_support value for the set of transactions.
#       3. items - A python list representing all the items that are part of all the transactions.
#       4. n - An integer variable representing what frequent item pairs to generate.
#       5. frequent_items - A dictionary representing k-1 frequent sets. 
#   Output:
#       1. frequent_itemsets - A dictionary representing the frequent itemsets and their corresponding support counts.
    
    len_transactions = len(dataset)
    if n == 1:
        # your code here
        l_item = []
        for key , value in dataset.items():
            l_item.extend(value)
        d_freq_item = {}
        for item in l_item :
            if item in d_freq_item:
                d_freq_item[item]=d_freq_item[item]+1
            else:
                d_freq_item[item]=1
        resul_freq_item = {k:v for k ,v in d_freq_item.items() if (v/len_transactions) >support}
        return resul_freq_item   
    else:
        sub_frequ_items = {}
        #frequent_items = generate_frequent_itemsets(dataset,support=support,items=items,n= n-1 , frequent_items = frequent_items)
        sub_items = findsubsets(items,n)
        for sub_item in sub_items:
            if all(item in frequent_items for item in sub_item):
                count_item = count_(dataset,sub_item)
                if (count_item/len_transactions) >support:
                    sub_frequ_items[sub_item] = count_item
                

        return sub_frequ_items
                
        
        