# stack, string/char operations


def calculate(s):
    """
    Two pass with stack: first pass to convert strings to digits and operators, second pass to calculate
    Time: O(n)
    Space: O(n)
    """
    stack = []
    number_op_list = []
    operators = ["+", "-", "*", "/"]
    num_start = 0
    # the first pass, to convert strings to digits and operators
    for i in range(len(s)):
        if s[i] in operators:
            number_op_list.append(int(s[num_start:i]))
            number_op_list.append(s[i])
            num_start = i + 1
        if i == len(s) - 1:
            number_op_list.append(int(s[num_start:]))
    i = 0
    # the second pass, to calculate the result
    while i < len(number_op_list):
        # a number, append to stack
        if number_op_list[i] not in operators:
            stack.append(number_op_list[i])
            i += 1
        # multiplication, pop out the top in stack and multiply with the next number, then add back to stack
        elif number_op_list[i] == "*":
            prev_number = stack.pop()
            stack.append(prev_number * number_op_list[i + 1])
            i += 2
        # division, pop out the top in stack and divide it by the next number, then add back to stack
        elif number_op_list[i] == "/":
            prev_number = stack.pop()
            if number_op_list[i + 1] == 0:
                return None
            else:
                # note we want the division to round towards zero here, cannot use the floor division //
                # // will round towards the smaller integer, not towards zero
                # since if prev_number is negative, the rounding will be the opposite
                stack.append(int(prev_number / number_op_list[i + 1]))
            i += 2
        # addition, add the next number in stack
        elif number_op_list[i] == "+":
            stack.append(number_op_list[i + 1])
            i += 2
        # subtraction, add the negative of the next number in stack
        elif number_op_list[i] == "-":
            stack.append(-number_op_list[i + 1])
            i += 2
    # the sum of the stack is the final result
    return sum(stack)


def calculate_one_pass(s):
    """
    One pass with stack: one pass to extract numbers and calculate at the same time
    Time: O(n)
    Space: O(n)
    """
    stack = []
    curr_num = 0
    # the plus sign allows us to push the first element in stack
    prev_sign = "+"

    for i in range(len(s)):
        # check digit, here we evaluate one char at a time rather than a range of chars
        # note: curr_num will always be the number after an operator
        if s[i].isdigit():
            curr_num = curr_num * 10 + int(s[i])
        # here we cannot use elif, in order to calculate the last number (i == len(s) - 1)
        if not s[i].isdigit() and s[i] != " " or i == len(s) - 1:
            # stack.pop() is the number before the operator, curr_num the number after
            # since we are using the operator from last step
            if prev_sign == "*":
                stack.append(stack.pop() * curr_num)
            elif prev_sign == "/":
                stack.append(int(stack.pop() / curr_num))
            elif prev_sign == "+":
                stack.append(curr_num)
            elif prev_sign == "-":
                stack.append(-curr_num)
            # now we can update the operator to that of this step's
            prev_sign = s[i]
            # reset the number
            curr_num = 0
    return sum(stack)


test = "14-3/2"
print(calculate(test))
print(calculate_one_pass(test))
print(eval(test))
