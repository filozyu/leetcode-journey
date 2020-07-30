# heap, divide and conquer


def kClosest(points, K):
    """
    Straight forward sorting
    Time: O(nlogn)
    Space: O(n)
    """
    dist_list = []
    for pt in points:
        dist = pt[0]**2 + pt[1]**2
        dist_list.append((dist, pt))
    dist_list.sort(key=lambda x: x[0])
    return [pt[1] for pt in dist_list[:K]]


def kClosest_heap(points, K):
    """
    Use heap to find the minimum
    Time: O(n + Klogn) n - number of points
    Space: O(n) for the heap
    """
    import heapq
    dist_list = []
    for pt in points:
        dist = pt[0] ** 2 + pt[1] ** 2
        dist_list.append((dist, pt))
    heapq.heapify(dist_list)
    return [heapq.heappop(dist_list)[1] for _ in range(K)]
