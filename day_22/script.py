#!/usr/bin/env python3

from copy import deepcopy

spells = [
    ["Magic Missile", 53],
    ["Drain", 73],
    ["Shield", 113, 6],
    ["Poison", 173, 6],
    ["Recharge", 229, 5],
]


def initial_state() -> {}:
    return deepcopy(
        {
            "PlayerHP": 50,
            "PlayerArmor": 0,
            "PlayerMana": 500,
            "effects": {
                "Shield": 0,
                "Poison": 0,
                "Recharge": 0,
            },
            "BossHP": 58,
            "BossDamage": 9,
        }
    )


def effects(state: {}) -> {}:
    for k, v in state["effects"].items():
        if k == "Shield":
            if v > 0:
                state["PlayerArmor"] = 7
                state["effects"][k] = v - 1
            else:
                state["PlayerArmor"] = 0
        if k == "Poison":
            if v > 0:
                state["BossHP"] -= 3
                state["effects"][k] = v - 1
        if k == "Recharge":
            if v > 0:
                state["PlayerMana"] += 101
                state["effects"][k] = v - 1
    return state


def available_spells(state: {}) -> {}:
    res = {}
    for i in range(0, 2):
        if spells[i][1] <= state["PlayerMana"]:
            res[i] = spells[i][1]
    for i in range(2, 5):
        if spells[i][1] <= state["PlayerMana"]:
            if state["effects"][spells[i][0]] <= 1:
                res[i] = spells[i][1]
    return res


def player_turn(i: int, state: {}) -> {}:
    if state["PlayerHP"] <= 0:
        return state
    state["PlayerMana"] -= spells[i][1]
    if i == 0:
        state["BossHP"] -= 4
    elif i == 1:
        state["BossHP"] -= 2
        state["PlayerHP"] += 2
    elif i == 2:
        state["effects"][spells[i][0]] = spells[i][2]
    elif i == 3:
        state["effects"][spells[i][0]] = spells[i][2]
    elif i == 4:
        state["effects"][spells[i][0]] = spells[i][2]
    return state


def boss_turn(state: {}) -> {}:
    if state["BossHP"] <= 0:
        return state
    armor = state["PlayerArmor"]
    damage = state["BossDamage"]
    hit = max(1, damage - armor)
    state["PlayerHP"] -= hit
    return state


def is_gameover(state: {}) -> (bool, int):
    if state["PlayerHP"] <= 0:
        return (True, 1)
    if state["BossHP"] <= 0:
        return (True, 0)
    return (False, -1)


def search(penalty: int) -> int:
    queue = [(0, initial_state())]
    while len(queue) > 0:
        spent, node = queue.pop(0)
        done, winner = is_gameover(node)
        if done:
            if winner == 0:
                return spent
            continue
        node["PlayerHP"] -= penalty
        moves = available_spells(node)
        if len(moves) == 0:
            continue
        for k, v in moves.items():
            state = deepcopy(node)
            state = effects(state)
            state = player_turn(k, state)
            state = effects(state)
            state = boss_turn(state)
            queue.append((spent + v, state))
    return -1


print("part 1:", search(0))
print("part 2:", search(1))
