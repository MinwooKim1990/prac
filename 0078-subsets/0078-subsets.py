class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = [[]]

        for n in nums:
            print('n',n)
            print('res', result)
            for i in range(len(result)):
                result.append(result[i]+[n])
                print('result',result)
        return result