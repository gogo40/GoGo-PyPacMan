# -*- coding: utf-8 -*-

"""
PyPacMan
Copyright (c) 2013 - Péricles Lopes Machado

This file is distributed under the MIT license. See LICENSE for details.
"""

from distutils.core import setup

setup(
    name='PyPacMan',
    version='0.1.6',
    author='Pericles Lopes Machado',
    author_email='pericles.raskolnikoff@gmail.com',
    packages=['pypacman','pypacman.ai','pypacman.gui','pypacman.game'],
    scripts=[
	'pypacman/ai/a_star.py',
	'pypacman/ai/ai_control.py',
	'pypacman/gui/window.py',
	'pypacman/game/game_control.py'
],
    url='http://pypi.python.org/pypi/PyPacMan/',
    license='LICENSE.txt',
    description='Useful towel-related stuff.',
    long_description=open('README.txt').read(),
    install_requires=[
	"pygame >= 1.0.0"
    ],
	package_data = {
        '': ['*.txt'],
		'': ['*.png']
    }

)
