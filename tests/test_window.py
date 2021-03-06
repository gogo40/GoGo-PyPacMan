# -*- coding: utf-8 -*-

"""
PyPacMan
Copyright (c) 2013 - Péricles Lopes Machado

This file is distributed under the MIT license. See LICENSE for details.
"""

import sys, pygame
from pypacman.gui import *
from pypacman.ai import *

pygame.init()

#grade do jogo
G = [
"###..####################..####################..####.",
".o.......*...o....#.#..o.......*........#.#....o......",
"....#.*..#.##.#####.#......#....#.##.#####.#......#...",
"#...#....#..#*.....*..#...#....#..#.....o*..#...#....#",
"#.####...#*##......o.##.####...#*##..o...*.##.####...#",
"#....#..##..o......#.##....#..##.........#.##....#..##",
"#o...#...#.###.##..####....#...#.###.##..####....#...#",
"#....#.o.....#..#....##....#o......#..#....##....#..*.",
"#....#.......#..#....##....#.......#..#....##....#....",
"###..#.##########.#######..#.##########.#######..#.###",
"#...##.....#....#.#...o...##.....#....#.#..##...##..o.",
"#......o...#..................o..#.........##.........",
"###..#.....##############..#.....##############..#.*..",
"..*......*.o.................o.*............o...*.....",
"....#....#.##.#####.#...o..#....#.##.#####.#.*....#...",
"#o..#....#..#......*..#...#....#..#......*..#...#....#",
"#.####...#*##......*.##.####...#*##......*.##.####...#",
"#....#..##.........#.##....#..##.........#.##....#..##",
"#.o..#...#.###.##..####....#.o.#.###.##..####*...#...#",
"#....#..o....#..#....##....#.......#..#....##....#....",
"#....#.......#..#....##....#.......#..#....##....#..*.",
"###..#.##########.#######..#.##########.#######..#.###",
"#...##..+..#....#.#..##...##.....#....#.#..##...##..o.",
"#..........#.o.......##..........#...o.....##.....o...",
"###..#.....##############..#.o...##############..#..o.",
".......o.....o........................................"]

#velocidade dos fantasmas (em segundos)
phantom_speed = 0.5
#velocidade do pac man (em mili-segundos)
pac_man_speed = 200

#dimensão das céluas do jogo
dim_cell = 25

ai = ai_control.AIControl(G, phantom_speed)

ai.start()

gui = window.Window(G, ai, dim_cell, pac_man_speed)
gui.run()
ai.wait()


