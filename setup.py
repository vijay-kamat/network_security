from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    requirement_lst:list[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found.")

    return requirement_lst
setup(
    name="network_security",
    version="0.0.1",
    author="Vijay Kamat",
    packages=find_packages(),
    install_requires=get_requirements()    
)