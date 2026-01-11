class Solution:
    def rotateMatrix(self, matrix):
        # code here
        n=len(matrix)
        # new_s=[[0]*n for _ in range(n)]
        
        # for i in range(n):
        #     for j in range(n):
        #         new_s[i][j]=matrix[j][n-i-1]
                
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] =new_s[i][j]  
        
        for i in range(n):
            for j in range(i+1,n):
                matrix[j][i], matrix[i][j]= matrix[i][j],matrix[j][i]
        for j in range(n):
            top, bottom = 0, n-1
            while top < bottom:
                matrix[top][j], matrix[bottom][j] = matrix[bottom][j], matrix[top][j]
                top += 1
                bottom -= 1
