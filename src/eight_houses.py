def cellCompete(states, days):
    def update(state):
        next_state = [0] * len(state)
        next_state[0] = state[1]
        if len(state) >= 2:
            next_state[-1] = state[-2]
        for i in range(1, len(state) - 1):
            if state[i-1] == state[i+1]:
                next_state[i] = 0
            else:
                next_state[i] = 1
        return next_state

    for day in range(days):
        states = update(states)
    return states


test_1 = [1, 0, 0, 0, 0, 1, 0, 0]
d1 = 1

test_2 = [1,1,1,0,1,1,1,1]
d2 = 2

print(cellCompete(test_1, d1))