# DFS, cycle in directed graph

from collections import defaultdict, deque


def findOrder(numCourses, prerequisites):
    """
    BFS based on parent dict and children dict
    Time: O(ne)? or O(ne^2)? in the worst case: O(n^3) (complete graph)
    Space: O(n+e) in the worst case: O(n^2) (complete graph)
    """
    if not prerequisites:
        return list(range(numCourses))
    ch_dict = {}
    pa_dict = {}

    # O(n)
    for c in range(numCourses):
        ch_dict[c] = []
        pa_dict[c] = []

    # O(e): e, number of edges, could be of n(n-1) in the worst case
    for i in range(len(prerequisites)):
        child, parent = prerequisites[i][0], prerequisites[i][1]
        ch_dict[parent].append(child)
        pa_dict[child].append(parent)

    roots = []
    visited = []
    queue = deque()

    # O(n)
    for key in pa_dict:
        if len(pa_dict[key]) == 0:
            roots.append(key)

    for root in roots:
        queue.append(root)
        visited.append(root)

    # the queue will run for O(n)
    while queue:
        curr_node = queue.popleft()
        if curr_node not in visited:
            visited.append(curr_node)
        curr_node_ch = ch_dict[curr_node]
        # the following loop will run for O(e)
        for ch in curr_node_ch:
            appending = True
            if ch in visited:
                return []
            # the following loop will run for O(?)
            for ch_pa in pa_dict[ch]:
                if ch_pa not in visited:
                    appending = False
                    break
            if appending:
                queue.append(ch)

    if len(visited) == numCourses:
        return visited
    else:
        return []


def findOrder_DFS(numCourses, prerequisites):
    """
    DFS with loop detection
    Time: O(n) we need to traverse through all the nodes
    Space: O(n) the recursion stack, visited, adj_dict and course_stack; worst case O(n^2) for adj_dict
    """
    if not prerequisites:
        return list(range(numCourses))
    # course_stack is used to store the output, advanced courses are put in first, basic ones are put in last
    course_stack = []
    # visited to record the nodes visited by DFS
    visited = {}
    adj_dict = defaultdict(list)
    # terminate the algorithm if a cycle is found, since there is no possible order of courses
    is_cycle = False

    def DFS(start, ch_dict, visited, course_stack):
        # it is vital here to declare this is_cycle is the same from the outer scope
        nonlocal is_cycle
        # now we have visited start
        visited[start] = 1
        # if the current node (start) has no child, then it is certainly a advanced course, put it in the stack
        if ch_dict.get(start) is None:
            course_stack.append(start)
        else:
            # if the current node has children (prerequisites), deal with these children first
            for ch in ch_dict[start]:
                # if we have visited a node (ch) and yet the node is not in the stack,
                # it means the current node (start) is on the path leading from ch, therefore there is a cycle
                # if the current node (start) is not on the path leading from ch,
                # then either we have not visited ch or that ch is already in the stack (a real child)
                if visited[ch] == 1 and ch not in course_stack:
                    # once we reach here, we can be sure to output []
                    is_cycle = True
                # if ch not visited
                if visited[ch] == 0:
                    DFS(ch, ch_dict, visited, course_stack)
            # after dealing with all of the children of the current node,
            # either we have a cycle, or all children of start are in the stack,
            # we can finally put start in the stack
            course_stack.append(start)

    # initialise visited dict: O(n)
    for node in range(numCourses):
        visited[node] = 0

    # construct adj_dict: O(e) e - number of edges, worst case n(n-1)
    for edge in prerequisites:
        target, source = edge[0], edge[1]
        adj_dict[source].append(target)

    # DFS on graph
    for node in range(numCourses):
        # DFS from every node, skip visited nodes
        # we have to start from every node since not all the nodes are connected
        # e.g. num_courses = 3, prerequisites = [1, 0]; then course 2 can be taken at any time
        if visited[node] == 0:
            DFS(node, adj_dict, visited, course_stack)
        if is_cycle:
            return []

    # the final answer should be a list of course from basic to advanced,
    # therefore from top of the stack (last element of course_stack) to the bottom (first of course_stack)
    return list(reversed(course_stack))


test_n = 4
test_c = [[1, 0], [2, 0], [3, 1], [3, 2]]
# test_c = [[1, 0], [0, 2], [3, 1], [2, 3]]

# test_n = 2
# test_c = [[0, 1]]
# test_c = [[0, 1], [1, 0]]

print(findOrder(test_n, test_c))
print(findOrder_DFS(test_n, test_c))
