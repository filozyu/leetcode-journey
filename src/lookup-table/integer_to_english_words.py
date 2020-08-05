def get_ones(n):
    ones = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    return ones[n]


def get_teens(n):
    teens = {
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }
    return teens[n]


def get_tens(n):
    tens = {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety",
    }
    return tens[n]


def numberToWords(num):
    """
    Time: O(n) n is the number of digits in num
    Space: O(n) the triplet dict
    """
    pows = {
        3: "Thousand",
        6: "Million",
        9: "Billion",
    }
    if num == 0:
        return "Zero"
    res = []

    # group the numbers by three
    triplets = {}
    for i in range(9, -3, -3):
        curr_group = int(num // (10 ** i))
        if curr_group == 0:
            continue
        else:
            num = num % (10 ** i)
            triplets[i] = curr_group

    # for each group, get the corresponding expression, followed by either Billion, Million or Thousand
    for p in triplets:
        curr_num = triplets[p]

        hundreds = int(curr_num // 100)
        if hundreds != 0:
            res.append(get_ones(hundreds))
            res.append("Hundred")
        curr_num -= 100 * hundreds
        tens = int(curr_num // 10)
        if tens == 1:
            res.append(get_teens(curr_num))
        elif tens > 0:
            res.append(get_tens(tens))
            curr_num -= 10 * tens
            if curr_num != 0:
                res.append(get_ones(curr_num))
        elif curr_num != 0:
            res.append(get_ones(curr_num))
        if pows.get(p):
            res.append(pows[p])

    return " ".join(res)


test = 12334567
print(numberToWords(test))
