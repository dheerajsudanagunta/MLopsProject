from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str) -> List[str]:
    '''
    this function reads the requirements from a file and returns them as a list
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements: List[str] = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
setup(
    name='MLopsProject',
    version='0.0.1',
    author='dheeraj',
    author_email='dheerajsudanagunta19@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)