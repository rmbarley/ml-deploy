from typing import List
from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."


def get_requirements(requirements_file: str) -> List[str]:
    """Returns the list of requirements"""
    with open(requirements_file) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Ryan Barley",
    author_email="rmbarley@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
