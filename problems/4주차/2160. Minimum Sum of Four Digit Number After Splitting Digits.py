class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = str(num)
        n_list = [int(x[0]),int(x[1]),int(x[2]),int(x[3])]
        n_list.sort()
        return 10*(n_list[0]+n_list[1])+n_list[2]+n_list[3]