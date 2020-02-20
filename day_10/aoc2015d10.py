#!/usr/bin/env python3

# data from http://www.njohnston.ca/2010/10/a-derivation-of-conways-degree-71-look-and-say-polynomial/

indices = {'': 0, '1112': 1, '1112133': 2, '111213322112': 3, '111213322113': 4, '1113': 5, '11131': 6, '111311222112': 7, '111312': 8, '11131221': 9, '1113122112': 10, '1113122113': 11, '11131221131112': 12, '111312211312': 13, '11131221131211': 14, '111312211312113211': 15, '111312211312113221133211322112211213322112': 16, '111312211312113221133211322112211213322113': 17, '11131221131211322113322112': 18, '11131221133112': 19, '1113122113322113111221131221': 20, '11131221222112': 21, '111312212221121123222112': 22, '111312212221121123222113': 23, '11132': 24, '1113222': 25, '1113222112': 26, '1113222113': 27, '11133112': 28, '12': 29, '123222112': 30, '123222113': 31, '12322211331222113112211': 32, '13': 33, '131112': 34, '13112221133211322112211213322112': 35, '13112221133211322112211213322113': 36, '13122112': 37, '132': 38, '13211': 39, '132112': 40, '1321122112': 41, '132112211213322112': 42, '132112211213322113': 43, '132113': 44, '1321131112': 45, '13211312': 46, '1321132': 47, '13211321': 48, '132113212221': 49, '13211321222113222112': 50, '1321132122211322212221121123222112': 51, '1321132122211322212221121123222113': 52, '13211322211312113211': 53, '1321133112': 54, '1322112': 55, '1322113': 56, '13221133112': 57, '1322113312211': 58, '132211331222113112211': 59, '13221133122211332': 60, '22': 61, '3': 62, '3112': 63, '3112112': 64, '31121123222112': 65, '31121123222113': 66, '3112221': 67, '3113': 68, '311311': 69, '31131112': 70, '3113112211': 71, '3113112211322112': 72, '3113112211322112211213322112': 73, '3113112211322112211213322113': 74, '311311222': 75, '311311222112': 76, '311311222113': 77, '3113112221131112': 78, '311311222113111221': 79, '311311222113111221131221': 80, '31131122211311122113222': 81, '3113112221133112': 82, '311312': 83, '31132': 84, '311322113212221': 85, '311332': 86, '3113322112': 87, '3113322113': 88, '312': 89, '312211322212221121123222113': 90, '312211322212221121123222122': 91, '32112': 92}

elements = {0: [], 1: [63], 2: [64, 62], 3: [65], 4: [66], 5: [68], 6: [69], 7: [84, 55], 8: [70], 9: [71], 10: [76], 11: [77], 12: [82], 13: [78], 14: [79], 15: [80], 16: [81, 29, 91], 17: [81, 29, 90], 18: [81, 30], 19: [75, 29, 92], 20: [75, 32], 21: [72], 22: [73], 23: [74], 24: [83], 25: [86], 26: [87], 27: [88], 28: [89, 92], 29: [1], 30: [3], 31: [4], 32: [2, 61, 29, 85], 33: [5], 34: [28], 35: [24, 33, 61, 29, 91], 36: [24, 33, 61, 29, 90], 37: [7], 38: [8], 39: [9], 40: [10], 41: [21], 42: [22], 43: [23], 44: [11], 45: [19], 46: [12], 47: [13], 48: [14], 49: [15], 50: [18], 51: [16], 52: [17], 53: [20], 54: [6, 61, 29, 92], 55: [26], 56: [27], 57: [25, 29, 92], 58: [25, 29, 67], 59: [25, 29, 85], 60: [25, 29, 68, 61, 29, 89], 61: [61], 62: [33], 63: [40], 64: [41], 65: [42], 66: [43], 67: [38, 39], 68: [44], 69: [48], 70: [54], 71: [49], 72: [50], 73: [51], 74: [52], 75: [47, 38], 76: [47, 55], 77: [47, 56], 78: [47, 57], 79: [47, 58], 80: [47, 59], 81: [47, 60], 82: [47, 33, 61, 29, 92], 83: [45], 84: [46], 85: [53], 86: [38, 29, 89], 87: [38, 30], 88: [38, 31], 89: [34], 90: [36], 91: [35], 92: [37]}

lengths = {0: 0, 1: 4, 2: 7, 3: 12, 4: 12, 5: 4, 6: 5, 7: 12, 8: 6, 9: 8, 10: 10, 11: 10, 12: 14, 13: 12, 14: 14, 15: 18, 16: 42, 17: 42, 18: 26, 19: 14, 20: 28, 21: 14, 22: 24, 23: 24, 24: 5, 25: 7, 26: 10, 27: 10, 28: 8, 29: 2, 30: 9, 31: 9, 32: 23, 33: 2, 34: 6, 35: 32, 36: 32, 37: 8, 38: 3, 39: 5, 40: 6, 41: 10, 42: 18, 43: 18, 44: 6, 45: 10, 46: 8, 47: 7, 48: 8, 49: 12, 50: 20, 51: 34, 52: 34, 53: 20, 54: 10, 55: 7, 56: 7, 57: 11, 58: 13, 59: 21, 60: 17, 61: 2, 62: 1, 63: 4, 64: 7, 65: 14, 66: 14, 67: 7, 68: 4, 69: 6, 70: 8, 71: 10, 72: 16, 73: 28, 74: 28, 75: 9, 76: 12, 77: 12, 78: 16, 79: 18, 80: 24, 81: 23, 82: 16, 83: 6, 84: 5, 85: 15, 86: 6, 87: 10, 88: 10, 89: 3, 90: 27, 91: 27, 92: 5}

def calc(current_seq: {}, n: int) -> int:
    global elements, lengths

    for i in range(n):
        new_seq = {}
        for k in current_seq:
            for t in elements[k]:
                if t not in new_seq:
                    new_seq[t] = 0
                new_seq[t] += current_seq[k]
        current_seq = new_seq
    res = 0
    for k in current_seq:
        res += lengths[k] * current_seq[k]
    return res

puzzle = '1113122113'   # aoc puzzle input
d = {indices[puzzle]: 1}
print("aoc2015d10p01:", calc(d, 40))
print("aoc2015d10p01:", calc(d, 50))