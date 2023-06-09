SIDE_WALL_OPENING = {
    # Player 0
    1: ('P', 1, 4),
    3: ('WV', 1, 3),
    # 5: ('P', 2, 4),
    # 7: ('WH', 4, 5),
    # 9: ('P', 3, 4),
    # 11: ('WH', 6, 5),
    # 13: ('WV', 7, 6),
    # Player 1
    2: ('WV', 3, 1),
    4: ('P', 7, 4),
    # 6: ('WH', 4, 2),
    # 8: ('P', 6, 4),
    # 10: ('WH', 6, 2),
    # 12: ('WV', 7, 1),
}

RUSH_OPENING = {
    # Player 0
    1: ('P', 1, 4),
    3: ('P', 2, 4),
    5: ('P', 3, 4),
    7: ('WV', 3, 3),
    # Player 1
    2: ('P', 7, 4),
    4: ('P', 6, 4),
    6: ('P', 5, 4),
    8: ('WV', 3, 3)
}

GAP_OPENING = {
    # Player 0
    1: ('P', 1, 4),
    3: ('P', 2, 4),
    5: ('P', 3, 4),
    7: ('WH', 2, 3),
    # 9: ('WH', 6, 2),
    # Player 1
    2: ('P', 7, 4),
    4: ('P', 6, 4),
    6: ('P', 5, 4),
    8: ('WH', 3, 5),
    10: ('WH', 6, 5),
}

REED_OPENING = {
    # Player 0
    1: ('WH', 5, 2),
    3: ('WH', 5, 5),
    # Player 1
    2: ('WH', 2, 2),
    4: ('WH', 2, 5),
}

SHATRANJ_OPENING = {
    # Player 0
    1: ('WV', 0, 3),
    # Player 1
    2: ('WV', 7, 3)
}

SHILLER_OPENING = {
    # Player 0
    1: ('P', 1, 4),
    3: ('P', 2, 4),
    5: ('P', 3, 4),
    7: ('WV', 0, 3),
    # Plyer 1
    2: ('P', 7, 4),
    4: ('P', 6, 4),
    6: ('P', 5, 4),
    8: ('WV', 7, 3)
}