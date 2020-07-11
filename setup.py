import os
from setuptools import (
    find_packages,
    setup,
)


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


with open(os.path.join(os.path.dirname(__file__), './VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='cxyx',
    version=version,
    description='A mini async framework, like Celery',
    packages=find_packages(exclude=[]),
    author='THJ',
    author_email='yongyuwanshua@163.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='#',
    install_requires=parse_requirements("requirements.txt"),
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'cxyx = cxyx.utils.tools:cxyx'
        ]
    }
)
