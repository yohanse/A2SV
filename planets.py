testCase = int(input())
for i in range(testCase):
    orbit_planet = [0]*100
    minimum_cost = 0
    num_planet, cost = map(int, input().split())
    planets = map(int, input().split())
    for i in planets:
        orbit_planet[i-1] += 1
    for num_planet in orbit_planet:
        minimum_cost += num_planet if num_planet<cost else cost
    print(minimum_cost)