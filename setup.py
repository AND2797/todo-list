from setuptools import setup

setup(
        name = 'todo',
        version = '0.0.1',
        packages = ['todo'],
        entry_points = {
            'console_scripts': [
                'todo = todo.__main__:main'
                ]
            }
        )