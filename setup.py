from setuptools import find_packages,setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="Backend experimenting",
    version="0.1",
    author="Yasiru",
    packages=find_packages(),
    install_requires=requirements
)

