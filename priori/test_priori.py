import unittest

from priori import generate_frequent_itemsets  

class TestX(unittest.TestCase):
    def setUp(self):
        self.min_support = 0.5
        self.items = ['A', 'B', 'C', 'D', 'E']
        self.dataset = dict()
        self.dataset["T1"] = ['A', 'B', 'D']
        self.dataset["T2"] = ['A', 'B', 'E']
        self.dataset["T3"] = ['B', 'C', 'D']
        self.dataset["T4"] = ['B', 'D', 'E']        
        self.dataset["T5"] = ['A', 'B', 'C', 'D']
        
    def test0(self):
        frequent_1_itemsets = generate_frequent_itemsets(self.dataset, self.min_support, self.items)
        print (frequent_1_itemsets)
        frequent_1_itemsets_solution = dict()
        frequent_1_itemsets_solution['A'] = 3
        frequent_1_itemsets_solution['B'] = 5
        frequent_1_itemsets_solution['D'] = 4

        print ("Test 1: frequent 1 itemsets")
        assert frequent_1_itemsets == frequent_1_itemsets_solution

        frequent_2_itemsets = generate_frequent_itemsets(self.dataset, self.min_support, self.items, 2, frequent_1_itemsets)
        print (frequent_2_itemsets)
        frequent_2_itemsets_solution = dict()
        frequent_2_itemsets_solution[('A', 'B')] = 3
        frequent_2_itemsets_solution[('B', 'D')] = 4
        
        print ("Test 1: frequent 2 itemsets")
        assert frequent_2_itemsets == frequent_2_itemsets_solution

        frequent_3_itemsets = generate_frequent_itemsets(self.dataset, self.min_support, self.items, 3, frequent_2_itemsets)
        print (frequent_3_itemsets)
        frequent_3_itemsets_solution = dict()

        print ("Test 1: frequent 3 itemsets")
        assert frequent_3_itemsets == frequent_3_itemsets_solution         
   
tests = TestX()
tests_to_run = unittest.TestLoader().loadTestsFromModule(tests)
unittest.TextTestRunner().run(tests_to_run) 