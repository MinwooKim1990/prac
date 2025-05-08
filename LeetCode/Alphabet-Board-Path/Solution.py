class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board_row = [
            ['a', 'f', 'k', 'p', 'u', 'z'], 
            ["b", "g", "l", "q", "v" ], 
            ["c", "h", "m", "r", "w"], 
            ["d", "i", "n", "s", "x"],
            ["e", "j", "o", "t", "y"]
            ]
        board_column = [
            ["a","b","c","d","e"],
            ["f","g","h",'i',"j"],
            ["k",'l','m','n',"o"],
            ["p","q","r","s","t"],
            ["u","v","w","x","y"],
            ['z']
            ]
        final_strings = ''
        cursor_r = 0
        cursor_c = 0
        for char in target:
            for R in range(len(board_row)):
                try:
                    column_index = board_row[R].index(char.lower())
                    row_index = R
                    cal_r = cursor_r - row_index
                    cal_c = cursor_c - column_index
                    cursor_r = row_index
                    cursor_c = column_index
                except:
                    pass
            if column_index != 5:
                if cal_c < 0:
                    final_strings += 'D'*abs(cal_c)
                elif cal_c > 0:
                    final_strings += 'U'*abs(cal_c)

                if cal_r < 0:
                    final_strings += 'R'*abs(cal_r)
                elif cal_r > 0:
                    final_strings += 'L'*abs(cal_r)
            else:
                if cal_c < 0:
                    final_strings += 'D'*(abs(cal_c)-1)
                elif cal_c > 0:
                    final_strings += 'U'*abs(cal_c)

                if cal_r < 0:
                    final_strings += 'R'*abs(cal_r)
                elif cal_r > 0:
                    final_strings += 'L'*abs(cal_r)

                if cal_c != 0:
                    final_strings += 'D'
            
            final_strings += '!'
        return final_strings