class LockingTree:

    def __init__(self, parent: List[int]):
        N = len(parent)

        self.graph = [[] for i in range(N)]
        self.parent = parent
        self.lock_user = [0 for i in range(N)]

        for i in range(1, N):
            self.graph[parent[i]].append(i)
        
    def lock(self, num: int, user: int) -> bool:
        if not self.lock_user[num]:
            self.lock_user[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.lock_user[num] == user:
            self.lock_user[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if not self.lock_user[num]:
            key = num
            while key != -1 and self.lock_user[key] == 0:
                key = self.parent[key]
            if key == -1:
                q = deque([num])
                flag = False
                while q:
                    vertex = q.popleft()
                    for adjvertex in self.graph[vertex]:
                        q.append(adjvertex)
                        if self.lock_user[adjvertex] != 0:
                            flag = True
                        self.lock_user[adjvertex] = 0
                if flag:
                    self.lock_user[num] = user
                return flag
            else:
                return False
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)