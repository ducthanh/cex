from setuptools import setup

setup(
    name='cex',
    version='0.1',
    py_modules=['cex'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cex=cex:cex
    ''',
)