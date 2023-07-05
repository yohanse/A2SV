t = int(input())

for _ in range(t):
    n = int(input())
    total_matches = n * ( n - 1) // 2   # total number of matches

    diff = 1  # To regulate the interval or spacing within the cycle.
    tables = [0 for i in range(total_matches)] # The tables are initialized with all matches resulting in ties.
    length = len(tables)

    while total_matches >= n:

        """
        Create a cyclic pattern of wins, 
        such as: 1 wins against 2, 2 wins against 3, 3 wins against 4, and 4 wins against 1.
        """
        for i in range(n):
            team_A, team_B = i, (i + diff) % n

            lowest = min(team_A, team_B)
            highest = max(team_A, team_B)                       # To locate the index of a particular match.
            index = length - ((n - lowest) * (n - 1 - lowest) // 2) + highest - lowest - 1

            tables[index] = 1 if team_A < team_B else -1

        diff += 1
        total_matches -= n    # Because we compute for a total of n matches.

    print(*tables)    