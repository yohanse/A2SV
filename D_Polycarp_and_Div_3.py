num = input()
visite = set([0])

tot = 0
count = 0
for j, i in enumerate(num):
    tot += int(i)
    reminder = tot % 3
    
    if reminder in visite:
        visite = set([0])
        count += 1
        tot = 0
    else:
        visite.add(reminder)
  
print(count)
        
        

