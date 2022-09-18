class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start=0
        end=len(people)-1
        ans=0
        total=0
        person=0
        while start<=end:
            if person<2 and total+people[end]<=limit:
                total=total+people[end]
                end=end-1
                person=person+1
            else:
                if person<2 and total+people[start]<=limit:
                    total=total+people[start]
                    start=start+1
                    person=person+1
                else:
                    ans=ans+1
                    total=0
                    person=0
        return ans+1
                    