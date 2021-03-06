from os.path import exists

from setuptools import find_packages, setup

if exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()
else:
    long_description = ''

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

test_requirements = ['pytest-cov']
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

setup(
    name='SeaFlux',
    author="Luke Gregor",
    author_email='lukegre@gmail.com	',
    description="Calculate sea-air fluxes ",
    keywords='SeaFlux',
    license="GNUv3",
    classifiers=CLASSIFIERS,
    url='https://github.com/luke-gregor/SeaFlux',
    use_scm_version={
    },
    long_description=long_description,
    packages=find_packages(),
    install_requires=install_requires,

    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=[
        'setuptools_scm',
        'setuptools>=30.3.0',
        'setuptools_scm_git_archive',
    ],
)
