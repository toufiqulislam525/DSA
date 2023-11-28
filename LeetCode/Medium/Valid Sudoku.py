class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        row = {}
        col = {}
        box = {}
        output = True

        for i,v in enumerate(board):
            
            for j,v2 in enumerate(v):
                r = i
                c = j%9
                b = r//3 * 3 + c//3
                r = str(r)
                c = str(c)
                b = str(b)
                zz = str(v2)
                if v2 != '.':
                    x = row.get(r+v2,0)
                    y = col.get(c+v2,0)
                    z = box.get(b+v2,0)
                    if x or y or z:
                        return False
                    else:
                        row[r+v2] = 1
                        col[c+v2] = 1
                        box[b+v2] = 1
        return True
    
            