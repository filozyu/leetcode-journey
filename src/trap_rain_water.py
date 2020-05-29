def trap(height):
    """
    Brute force
    Time: O(n^2)
    Space: O(1)
    """
    area = 0
    for i in range(len(height)):
        # for each position, measure how much rain water it can contain
        max_left, max_right = 0, 0
        for l in range(i, -1, -1):
            if height[l] > max_left:
                max_left = height[l]
        for r in range(i, len(height)):
            if height[r] > max_right:
                max_right = height[r]
        if min(max_left, max_right) <= height[i]:
            # this means the current position is protruding above the surface, therefore not contributing to the area
            continue
        else:
            area += min(max_left, max_right) - height[i]
    return area


def trap_faster(height):
    """
    Pre-compute left max and right max
    Time: O(n)
    Space: O(n)
    """
    area = 0
    max_left_dict = {}
    max_right_dict = {}

    for i in range(len(height)):
        if i == 0 or height[i] > max_left_dict[i - 1]:
            max_left_dict[i] = height[i]
        else:
            max_left_dict[i] = max_left_dict[i - 1]

    for j in range(len(height) - 1, -1, -1):
        if j == len(height) - 1 or height[j] > max_right_dict[j + 1]:
            max_right_dict[j] = height[j]
        else:
            max_right_dict[j] = max_right_dict[j + 1]

    for p in range(len(height)):
        if min(max_left_dict[p], max_right_dict[p]) <= height[p]:
            continue
        else:
            area += min(max_left_dict[p], max_right_dict[p]) - height[p]

    return area


def trap_stack(height):
    """
    Stack of indices
    A new index will enter the stack only if the corresponding height <= height of the top of the stack
    Whenever a new index whose corresponding height > height of the top of the stack, start to calculate area
    Areas are calculated by "layers"
    Time: O(n)
    Space: O(n) (worst case)
    """
    area = 0
    # initialise the stack with the first index
    stack = [0]
    for i in range(1, len(height)):
        # only start calculation if stack is non-empty
        while len(stack) > 0 and height[i] > height[stack[-1]]:
            # can now safely pop the top and calculate the area of the gap between it and the new top of stack
            top = stack.pop()
            if len(stack) > 0:
                # if the stack is still not empty (i.e we have a left bound by the current top of the stack)
                # get the width of the layer
                dist = i - stack[-1] - 1
                # area of the new layer is width * height of gap
                area += dist * (min(height[i], height[stack[-1]]) - height[top])
        # Now we have calculated all the gap between the current height and the start, proceed
        stack.append(i)

    return area


def trap_tow_pointers(height):
    """
    Two pointers (similar to trap faster where area are computed at every index)
    Time: O(n)
    Space: O(1)
    """
    area = 0
    left_max, right_max = 0, 0
    left_pointer = 0
    right_pointer = len(height) - 1
    while left_pointer < right_pointer:

        # when left is higher, calculate the area at the right pointer
        # since now the height of the right_pointer will be between the height of the left_pointer and right_max
        if height[left_pointer] > height[right_pointer]:
            # area cannot be computed if the height of right_pointer is the new right_max
            if height[right_pointer] > right_max:
                right_max = height[right_pointer]
            # otherwise compute the area at right_pointer
            else:
                area += right_max - height[right_pointer]
            right_pointer -= 1

        # when right is higher, calculate the area at the left pointer
        # since now the height of the left_pointer will be between the height of the right_pointer and left_max
        else:
            # area cannot be computed if the height of right_pointer is the new right_max
            if height[left_pointer] > left_max:
                left_max = height[left_pointer]
            # otherwise compute the area at left_pointer
            else:
                area += left_max - height[left_pointer]
            left_pointer += 1

    return area


test = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_tow_pointers(test))
