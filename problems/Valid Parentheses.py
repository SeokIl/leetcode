class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list_1 = []

        for i in s:
            if (i == '(' )|(i == '[' )|(i == '{') :
                list_1.append(i)
            else:
                if len(list_1)==0:
                    return False
                last_s = list_1.pop()
                if i == ')':
                    if last_s!='(':
                        return False
                if i == ']':
                    if last_s!='[':
                        return False
                if i == '}':
                    if last_s!='{':
                        return False
        if len(list_1)==0:
            return True
        else:
            return False
