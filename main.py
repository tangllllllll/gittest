#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @author Epsirom
# pylint: disable=bare-except

import sys
import traceback
from game_timer import GameTimer
from life_game import LifeGame


def print_usage():
    print("Usage:", sys.argv[0], '<map_rows=10>', '<map_cols=10>', '<life_init_possibility=0.5>',
          '<time_interval=1.0>')


def main(argv):
    """ Main function
    Args:
        argv: command line arguments

    Returns:
        Exit code
    """
    map_rows = 10
    map_cols = 10
    life_init_possibility = 0.5
    timer_interval = 1.0
    if len(argv) > 0:
        map_rows = int(argv[0])
    if len(argv) > 1:
        map_cols = int(argv[1])
    if len(argv) > 2:
        life_init_possibility = float(argv[2])
    if len(argv) > 3:
        timer_interval = float(argv[3])
    game = LifeGame(map_rows, map_cols, life_init_possibility)
    game.print_map()
    timer = GameTimer(game.game_cycle, timer_interval)
    timer.start()
    return 0


if __name__ == '__main__':
    try:
        exit(main(sys.argv[1:]))
    except:
        traceback.print_exc()
        print_usage()
