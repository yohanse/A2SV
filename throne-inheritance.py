class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.InheritanceOrder = {kingName: []}
        self.dead = set()


    def birth(self, parentName: str, childName: str) -> None:
        self.InheritanceOrder[parentName].append(childName)
        self.InheritanceOrder[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        self.answer = []
        self.dfs(self.kingName)
        return self.answer

    def dfs(self, name):
        if name not in self.dead:
            self.answer.append(name)

        for childName in self.InheritanceOrder[name]:
            self.dfs(childName)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()