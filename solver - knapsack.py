#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])
def solve_it(input_data):
    # Modify this code to run your optimization algorithm
    # parse the input
    lines = input_data.split('\n')
    firstline = lines[0].split()
    item_count = int(firstline[0])
    capacity = int(firstline[1])
    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
        vt = []
        wt = []
        
        vt.append(items[i][1])
        wt.append(items[i][2])
        
    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    
        w = capacity + 1
        h = len(vt)
        table = [[0 for x in range(w)]for y in range range(h)]

        for index in range(len(vts)):
            for weight in range(w):
                if wt[i] > capacity:
                    table[index][weight] =  table[index-1][weight]
                    continue
                if wt[i] <= capacity:
                    if (vts[i] + table[index-1][weight-wt[index]]) > table[index-1][weight]:
                        table[index][weight] = max(table[index-1][weight],vts[i] + table[index-1][weight-wt[index]])
                        
                    else:
                        table[index][weight] = table[index-1][weight]

    # prepare the solution in the specified output format
                    output_data = str(max(table[index][weight])) 
                    return output_data

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
