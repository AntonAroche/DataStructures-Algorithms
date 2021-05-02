# There are n different online courses numbered from 1 to n.
# You are given an array courses where courses[i] = [durationi, lastDayi]
# indicate that the ith course should be taken continuously for durationi
# days and must be finished before or on lastDayi.
#
# You will start on the 1st day and you cannot take two or more courses simultaneously.
#
# Return the maximum number of courses that you can take.
import heapq

def scheduleCourse(courses):
    heap, time = [], 0
    for t, end in sorted(courses, key=lambda x: x[1]):
        time += t
        heapq.heappush(heap, -t)
        if time > end:
            nt = heapq.heappop(heap)
            time += nt
    return len(heap)

courses = [[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]
courses2 = [[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]

print(scheduleCourse(courses), "Expected: ", 5)
print(scheduleCourse(courses2), "Expected: ", 4)

