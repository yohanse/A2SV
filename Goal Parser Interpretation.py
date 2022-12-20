class Solution:
    def interpret(self, command: str) -> str:
        original=""
        for i in range(len(command)):
            if command[i]=="G":
                original+="G"
            elif command[i]==")":
                if command[i-1]=="(":
                    original+="o"
                else:
                    original+="al"
        return original