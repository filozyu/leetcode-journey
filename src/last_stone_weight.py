def lastStoneWeight(stones):
    while len(stones) > 1:
        max_stone = max(stones)
        stones.remove(max_stone)
        second_max_stone = max(stones)
        stones.remove(second_max_stone)
        if max_stone != second_max_stone:
            stones.append(max_stone - second_max_stone)
    if len(stones) == 1:
        return stones[0]
    else:
        return 0
