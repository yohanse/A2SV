class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        graph = [[] for i in range(n)]

        for a, b, c in meetings:
            graph[a].append((b, c))
            graph[b].append((a, c))

        
        distances = [float("inf") for i in range(n)]
        distances[firstPerson] = 0
        visited = set() 
        priority_queue = [(0, firstPerson), (0, 0)]
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node in visited:
                continue
            visited.add(current_node)
        
            for neighbor, weight in graph[current_node]:
                if current_distance <= weight and weight < distances[neighbor]:
                    distances[neighbor] = weight
                    heapq.heappush(priority_queue, (weight, neighbor))
        
        return visited