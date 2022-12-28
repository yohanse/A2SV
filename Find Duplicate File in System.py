class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        table, res = defaultdict(list), []
        for path in paths:
            path = path.split()
            for files in path[1:]:
                i = 0
                file_name = ''
                content = ''
                while files[i] != '(':
                    file_name += files[i]
                    i += 1
                i += 1
                while files[i] != ')':
                    content += files[i]
                    i += 1
                table[content].append(path[0] + '/' + file_name)
        for i in table:
            if len(table[i])>1:
                res.append(table[i])
        return res                