from distutils.core import setup

setup(
    name='PyPacMan',
    version='0.1.1',
    author='Pericles Lopes Machado',
    author_email='pericles.raskolnikoff@gmail.com',
    packages=['gui', 'IO', 'AI', 'game'],
    scripts=[],
    url='http://pypi.python.org/pypi/PyPacMan/',
    license='LICENSE.txt',
    description='Useful towel-related stuff.',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)
