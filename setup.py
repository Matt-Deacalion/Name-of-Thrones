from setuptools import setup
import game_of_thrones

setup(
    name='game-of-thrones-namer',
    version=game_of_thrones.__version__.strip(),
    url='http://dirtymonkey.co.uk/game-of-thrones-namer',
    license='MIT',
    author=game_of_thrones.__author__.strip(),
    author_email='matt@dirtymonkey.co.uk',
    description=game_of_thrones.__doc__.strip().replace('\n', ' '),
    long_description=open('README.rst').read(),
    keywords='game of thrones naming namer project tools',
    packages=['game_of_thrones'],
    include_package_data=True,
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'game-of-thrones = game_of_thrones.main:main',
        ],
    },
    install_requires=[
        'colorama>=0.3.1',
        'docopt>=0.6.2',
    ],
    tests_require=[
        'py>=1.4.20',
        'pytest>=2.5.2',
        'mock>=1.0.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: BSD',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
)
