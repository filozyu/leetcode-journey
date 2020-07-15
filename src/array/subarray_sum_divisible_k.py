def subarrayDivByK_slowest(A, K):
    """
    Brute force
    Time: O(n^3) in each iteration, we have to loop over j, slice and sum the subarray
    Space: O(1)
    """
    res = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if sum(A[i : j + 1]) % K == 0:
                res += 1
    return res


def subarrayDivByK_slow(A, K):
    """
    Brute force (improved)
    Time: O(n^2) use an array to store the running sum instead, therefore no need for slicing and summing
    Space: O(n)
    """
    res = 0
    # running_sum[i+1] contains the sum from A[0] to A[i], running_sum[0] = 0
    # running_sum[j] - running_sum[i] is the sum from A[i] to A[j - 1]

    # Note that if running_sum[i] is the sum from A[0] to A[i]
    # then running_sum[j] - running_sum[i] is the sum from A[i + 1] to A[j]
    # we won't be able get the sum from A[0] using running_sum[j] - running_sum[i]

    running_sum = [0] * (len(A) + 1)
    for i in range(len(A)):
        running_sum[i + 1] = running_sum[i] + A[i]

    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            # curr_sum = A[i] + ... + A[j - 1]
            curr_sum = running_sum[j] - running_sum[i]
            if curr_sum % K == 0:
                res += 1

    return res


def subarrayDivByK(A, K):
    """
    One pass
    Use running_sum to represent the current running sum (to save space, we do not store running_sum as an array)
    At step j: running_sum_j = A[0] + ... + A[j]
    the sum between A[i + 1] and A[j] is running_sum_j - running_sum_i
    (A[i + 1] + ... + A[j]) % k == 0
    -> (running_sum_j - running_sum_i) % k == 0
    -> running_sum_j % k == running_sum_i % k
    so we keep a record of running_sum modulus k, which have keys ranging from 0 to k - 1

    Time: O(n)
    Space: O(n)
    """
    res = 0
    running_sum = 0
    # initialise modulus to contain 0: 1 since this helps with subarray that starts from the start of A
    # running_sum at step i calculates A[0] + ... + A[i]
    # e.g. A = [1,2,3,4], K = 2
    # then if running_sum % K == 0 for the first time, we need to increment res by 1
    # but if modulus is empty, we cannot update
    # after the first encounter, we need to increase it by 1 again (thus modulus[0] = 2 now)
    # since the second encounter would mean we have two more solutions: that from the start
    # and the sum between the first encounter and the second encounter

    # in short, if running_sum % K == 0 at index j then there are two types of solutions:
    # 1) One solution: A[0], ..., A[j]
    # 2) Other solutions for previously encountered i: A[i + 1], ..., A[j]
    modulus = {0: 1}
    for i in range(len(A)):
        running_sum += A[i]
        mod = running_sum % K
        if modulus.get(mod) is not None:
            # if we already have previous running_sum (can be several, say at steps i_1, ... i_c) that has the same mod
            # then A[i_1 + 1] to A[i], A[i_2 + 1] to A[i], ..., A[i_c + 1] to A[i] are all valid subarray
            res += modulus[mod]
            # then we add 1 to our count (for the running_sum at index i)
            modulus[mod] += 1

        else:
            # alternatively (without initialising modulus),
            # 1) add a condition before the line below that if mod == 0, modulus[mod] = 2
            # 2) add a condition after the line below that if mod == 0, res += 1
            modulus[mod] = 1
    return res


test = [4, 5, 0, -2, -3, 1]
test_k = 5
print(subarrayDivByK_slow(test, test_k))
