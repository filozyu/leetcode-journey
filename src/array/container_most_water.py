# colliding two pointers
def maxArea(height):
    """
    Brute force (Time limit exceeded)
    Time: O(n^2)
    Space: O(1)
    """
    num_pt = len(height)
    max_area = 0
    for i in range(num_pt):
        for j in range(i + 1, num_pt):
            h = min(height[i], height[j])
            a = h * (j - i)
            if a > max_area:
                max_area = a
    return max_area


def maxArea_fast(height):
    """
    Two pointers from both ends
    Time: O(n)
    Space: O(1)
    """
    i, j = 0, len(height) - 1
    max_area = 0
    while j > i:
        a = min(height[i], height[j]) * (j - i)
        if a > max_area:
            max_area = a
        # only move the pointer with smaller value
        # min(h[i], h[j]) might increase or decrease or stay the same (but we can be sure to have the max if decrease)
        # if move the pointer with larger value, which is incorrect
        # min(h[i], h[j]) might decrease or stay the same (no chance of increase)
        # even there are lager values in h, but the area is still determined by the unmoved smaller pointer,
        # therefore the effective height won't change, but the width has decreased due to moving

        # Compare to brute force, checking all the pairs:
        # Suppose h[i] < h[j], then i += 1
        # skipped the pairs: (i, j-1), (i, j-2) ..., (i, i+1); all of which have areas smaller then (i, j)
        # therefore can be safely skipped
        if height[i] >= height[j]:
            j -= 1
        else:
            i += 1
    return max_area
