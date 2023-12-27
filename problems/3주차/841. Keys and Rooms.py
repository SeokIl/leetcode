class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        start_room = rooms[0]

        def dfs(keys, visited):
            for key in keys:
                if visited[key]:
                    continue
                else:
                    visited[key] = True
                    dfs(rooms[key], visited)

        dfs(start_room, visited)

        if False in visited:
            return False
        else:
            return True