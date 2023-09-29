from collections import deque

def bsf(graph,start):
    visited_places =set()
    placesTovisitqueue=deque([start])
    while placesTovisitqueue:
        place =placesTovisitqueue.popleft()
        if place is not visited_places:
            visited_places.add(place)
            print(place)
            placesTovisitqueue.extend(graph[place]-visited_places)

graph={}
noofEdges=int(input('entar number of Edges you need:'))

for i in range(noofEdges):
    print('entar the place1 and place2:\n')
    val1,val2=input().split()

    if val1 not in graph:
        graph[val1]=set()
    if val2 not in graph:
        graph[val2]=set()

    graph[val1].add(val2)
    graph[val2].add(val1)

print('Entar the start value')
start= input()
bsf(graph,start)

