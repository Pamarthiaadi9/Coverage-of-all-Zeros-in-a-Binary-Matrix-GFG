class Solution:
	def FindCoverage(self, matrix):
	    row, col = len(matrix), len(matrix[0])
	    count = 0
	    
	    for i in range(row):
	        for j in range(col):
	            if matrix[i][j]==0:
	                if -1<i-1<row and matrix[i-1][j]==1:
	                    count+=1
	                if -1<j-1<col and matrix[i][j-1]==1:
	                    count+=1
	                if -1<j+1<col and matrix[i][j+1]==1:
	                    count+=1
	                if -1<i+1<row and matrix[i+1][j]==1:
	                    count+=1
	    return count
