from setuptools import setup, find_packages

setup(
    name='pmanager',
    version='0.1',
    py_modules=['main'],
    packages=find_packages(),
    install_requires=[
        'Click',
        'tinydb'
    ],
    entry_points='''
        [console_scripts]
        pmanager=pmanager_package.main:cli
    ''',
)