from distutils.core import setup

setup(
    name='PyPacMan',
    version='0.1.3',
    author='Pericles Lopes Machado',
    author_email='pericles.raskolnikoff@gmail.com',
    packages=['pypacman','pypacman.ai'],
    scripts=['pypacman/ai/a_star.py'],
    url='http://pypi.python.org/pypi/PyPacMan/',
    license='LICENSE.txt',
    description='Useful towel-related stuff.',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)
