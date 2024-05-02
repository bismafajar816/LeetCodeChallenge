class Solution:
    def numberOfBeams(self, bank) :
        row_length = len(bank)
        col_length = len(bank[0])
        ans = 0
        count1 = 0
        count2 = 0
        Flag = True
        for row in range(row_length):
            for col in range(col_length):
                if Flag == True and bank[row][col] == '1':
                    count1 += 1
                if Flag == False and bank[row][col] == '1':
                    count2 += 1
                    
            if count1 > 0 and count2 > 0:
                ans += count1 * count2
                count1 = count2
                count2 = 0
            if count1 >0 and Flag == True:
                Flag = False
        
        return ans