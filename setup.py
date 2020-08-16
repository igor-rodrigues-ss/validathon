from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='validathon',
    version='0.1.0',
    description='Customizable utility for data validation recursive in dictionary with injection of exceptions.',
    author='Igor Rodrigues Sousa Silva',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='igor.rodrigues.ss10@gmail.com',
    url='https://github.com/igor-rodrigues-ss/validathon',
    test_suite='tests',
    packages=find_packages(exclude='tests'),
    tests_require=['pytest'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation ",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)