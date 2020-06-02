from collections import defaultdict
import heapq


def minMeetingRooms(intervals):
    """
    One list per room
    Time: O(n^2)
    Space: O(n)
    """
    if not intervals:
        return 0
    room_dict = defaultdict(list)
    num_rooms = 1
    intervals.sort()
    for i in range(len(intervals)):
        if i == 0:
            room_dict[0].append(intervals[i])
            continue
        # in worst case where every interval requires a room,
        # we need to make k comparisons for the k-th interval
        for room in range(num_rooms):
            if intervals[i][0] >= room_dict[room][-1][1]:
                room_dict[room].append(intervals[i])
                break
            elif room == num_rooms - 1:
                num_rooms += 1
                room_dict[room + 1].append(intervals[i])
                break

    return num_rooms


def minMeetingRooms_heap(intervals):
    """
    Heap for ending times
    Time: O(nlogn) sorting and the operations on heap
    Space: O(n) the heap, worst case
    """
    if not intervals:
        return 0
    # sort the intervals by starting time (lambda can be removed since that's the default anyway)
    intervals.sort(key=lambda s: s[0])
    heap = [intervals[0][1]]
    # operations on heap: n insertion (update a meeting room's ending or add a new room), m deletion
    # the final number of meeting rooms: n-m
    # if every interval requires its own room, then we have n insertion, 0 deletion
    # time: log1 + log2 + ... + log(n-1) = log((n-1)!) < log(n^n) = nlogn
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            # we don't need to update room, but update the ending time of an existing room
            heapq.heappop(heap)
        # this can be:
        # updating an existing room, if the above if condition is true
        # adding a new room, if the above if condition is false
        heapq.heappush(heap, intervals[i][1])

    return len(heap)


# test = [[0, 30], [5, 10], [15, 20]]
test = [[7, 10], [2, 4]]
print(minMeetingRooms_heap(test))
