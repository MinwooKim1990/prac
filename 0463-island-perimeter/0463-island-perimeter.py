class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        tot=0
        for i in grid:
            tot=tot+sum(i)
        find_ind={}
        tot_minus_v=0
        tot_minus_h=0
        for i in range(len(grid)):
            temp=[]
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    temp.append(j)
                    if j >0 :
                        if j-1 in temp:
                            tot_minus_h+=1
            find_ind[i]=temp
            if i > 0:
                for k in find_ind[i-1]:
                    if k in find_ind[i]:
                        tot_minus_v+=1
        print(tot)
        print(tot_minus_v)
        print(tot_minus_h)
        return 4*tot-2*tot_minus_v-2*tot_minus_h