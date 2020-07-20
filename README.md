# Average-Total-Opportunity-Cost-ATOC
 A method for solving Transportation Problem

Algorithm for TOCT
Step 1: Subtract the smallest entry from each of the elements of every row of the TT and place them on the right-top of corresponding elements.
Step 2: Apply the same operation on each of the columns and place them on the right-bottom of the corresponding elements.
Step 3: Form the TOCT whose entries are the summation of right-top and right-bottom elements of Steps 1 and 2.

Algorithm for Allocation
Step 1: Place the average of total opportunity costs of cells along each row identified as Row Average Total Opportunity Cost (RATOC) and the average of total opportunity costs of cells along each column identified as Column Average Total Opportunity Cost (CATOC) just after and below the supply and demand amount respectively within first brackets.
Step 2: Identify the highest element among the RATOCs and CATOCs, if there are two or more highest elements; choose the highest element along which the smallest cost element is present. If there are two or more smallest elements, choose any one of them arbitrarily.
Step 3: Allocate Xij = min(ai, bj) on the left top of the smallest entry in the (i, j) th of the TT.
Step 4:
a). If ai < bj, leave the i-th row and readjust bj as bj = bj - ai.
b). If ai > bj, leave the j-th column and readjust ai as ai = ai - bj.
c). If ai = bj, leave either ith row or j-th column but not both.
Step 5: Repeat Steps 1 to 4 until the rim requirement satisfied.
Step 6: Calculate sum i=1 to m sum j=1 to n of cij xij, z being the minimum transportation cost and cij are the cost elements of the TT.

Source: S.M. Abul Kalam Azad, Md. Bellel Hossain, and Md. Mizanur Rahman, "An Algorithmic Approach to Solve Transportation Problems with The ", International Journal of Scientific and Research Publications, Volume 7, Issue 2, February 2017.
