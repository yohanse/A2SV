class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        table,res = {}, []
        for domains in cpdomains:
            num, i = 0, 0

            while domains[i] != ' ':   # to know how many opens that site
                num = num*10 + int(domains[i])
                i += 1

            table[domains[i+1:]] = num + table.get(domains[i+1:],0)
            while i < len(domains):  #to know the name of the site by its domain
                if domains[i]=='.':
                    table[domains[i+1:]] = num + table.get(domains[i+1:],0)
                i += 1

        for key in table:
            res.append(str(table[key]) + ' ' + key)
            
        return res