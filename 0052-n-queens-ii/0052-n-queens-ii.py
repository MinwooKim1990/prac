class Solution:
    def totalNQueens(self, n: int) -> int:    
        #preset
        cols=set()
        dia=set()
        antidia=set()
        res=set()
        def track(r):
            if r==n:  # switch   
                return 1      
            count=0
            for queen in range(n):
                if not(queen in cols or (r-queen) in dia or (r+queen) in antidia):
                    cols.add(queen) # Add if it is not in
                    dia.add(r-queen)
                    antidia.add(r+queen)        
                    print('addcol',cols)
                    count+=track(r+1) # count
                    cols.remove(queen) # remove additional adding
                    dia.remove(r-queen)
                    antidia.remove(r+queen)     
                    print('removecol',cols)
            return count
        return track(0)