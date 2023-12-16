class MyQueue(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        x = self.queue[0]
        self.queue = self.queue[1:]
        return x

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        else:
            return False
