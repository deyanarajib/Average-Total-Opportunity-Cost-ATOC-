import numpy as np
from Setup import Transportation

class AverageTotalOpportunityCost:

    def __init__(self, trans):

        self.trans = trans
        self.table = trans.table.copy()
        self.alloc = []

    def allocation(self, x, y):
        
        mins = min([self.table[x, -1], self.table[-1, y]])
        self.alloc.append([self.table[x, 0], self.table[0, y], mins])
        
        if self.table[x, -1] < self.table[-1, y]:
            #delete row and supply x then change value of demand y
            self.table = np.delete(self.table, x, 0)
            self.table[-1, y] -= mins
            
        elif self.table[x, -1] > self.table[-1, y]:
            #delete column and demand y then change value of supply x
            self.table = np.delete(self.table, y, 1)
            self.table[x, -1] -= mins
            
        else:
            #delete row and supply x, column and demand y
            self.table = np.delete(self.table, x, 0)
            self.table = np.delete(self.table, y, 1)

    def solve(self, show_iter=False):

        cost = self.table[1:-1, 1:-1].copy()
        cost1 = cost - np.min(cost, 1).reshape(-1, 1)
        cost2 = cost - np.min(cost, 0)
        self.table[1:-1, 1:-1] = cost1 + cost2

        if show_iter:
            self.trans.print_frame(self.table)

        while self.table.shape != (2, 2):

            ratoc = np.average(self.table[1:-1, 1:-1], 1)
            catoc = np.average(self.table[1:-1, 1:-1], 0)

            if max(ratoc) > max(catoc):
                x = np.argmax(ratoc)
                y = np.argmin(self.table[x + 1, 1:-1])
            else:
                y = np.argmax(catoc)
                x = np.argmin(self.table[1:-1, y + 1])

            self.allocation(x + 1, y + 1)

            if show_iter:
                self.trans.print_frame(self.table)
            
        return np.array(self.alloc, dtype=object)


if __name__ == "__main__":

    #example 1 balance problem
    cost = np.array([[9, 8, 5, 7],
                    [4, 6, 8, 7],
                    [5, 8, 9, 5]])

    supply = np.array([12, 14, 16])
    demand = np.array([8, 18, 13, 3])

    #example 2 unbalance problem
    cost = np.array([[ 4,  8,  8],
                    [16, 24, 16],
                    [8, 16, 24]])
    supply = np.array([76, 82, 77])
    demand = np.array([72, 102, 41])

    #initialize transportation problem
    trans = Transportation(cost, supply, demand)

    #setup transportation table.
    #minimize=True for minimization problem, change to False for maximization, default=True.
    #ignore this if problem is minimization and already balance
    trans.setup_table(minimize=True)

    #initialize ATOC method with table that has been prepared before.
    ATOC = AverageTotalOpportunityCost(trans)

    #solve problem and return allocation lists which consist n of (Ri, Cj, v)
    #Ri and Cj is table index where cost is allocated and v it's allocated value.
    #(R0, C1, 3) means 3 cost is allocated at Row 0 and Column 1.
    #show_iter=True will showing table changes per iteration, default=False.
    allocation = ATOC.solve(show_iter=False)

    #print out allocation table in the form of pandas DataFrame.
    #(doesn't work well if problem has large dimension).
    trans.print_table(allocation)

#Result from example problem above
'''
example 1 balance problem
          C0     C1     C2    C3 Supply
R0         9      8  5(12)     7     12
R1         4  6(13)   8(1)     7     14
R2      5(8)   8(5)      9  5(3)     16
Demand     8     18     13     3     42

TOTAL COST: 241

example 2 unbalance problem
            C0      C1      C2  Dummy Supply
R0           4   8(76)       8      0     76
R1      16(21)      24  16(41)  0(20)     82
R2       8(51)  16(26)      24      0     77
Demand      72     102      41     20    235

TOTAL COST: 2424
'''
