class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        col0 = 1

        # Step 1: mark rows & columns
        for i in range(r):
            if matrix[i][0] == 0:
                col0 = 0
            
            for j in range(1, c):
                if matrix[i][j] == 0:   
                    matrix[0][j] = 0
        
        # Step 2: update inner matrix
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 3: first row
        if matrix[0][0] == 0:
            for j in range(c):
                matrix[0][j] = 0
        
        # Step 4: first column
        if col0 == 0:
            for i in range(r):
                matrix[i][0] = 0