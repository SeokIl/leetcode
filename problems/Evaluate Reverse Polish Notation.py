class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens)==1:
            result = int(tokens[0])
            return result
        temp_q = []
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                temp_q.append(i)
            else:
                temp_y = float(temp_q.pop())
                temp_x = float(temp_q.pop())
                if i =='+':
                    result = temp_x + temp_y
                if i =='-':
                    result = temp_x - temp_y
                if i =='*':
                    result = temp_x * temp_y
                if i =='/':
                    x = temp_x/temp_y
                    result = int(x)
                temp_q.append(result)
        return int(result)