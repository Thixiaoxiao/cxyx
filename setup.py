import os
from setuptools import (
    find_packages,
    setup,
)


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name='cxyx',
    version="0.1.3",
    description='A mini async framework, like Celery',
    packages=find_packages(exclude=[]),
    author='chenxiyuxiao',
    author_email='18883325829@163.com',
    license='BSD 2-Clause License',
    package_data={'': ['*.*']},
    url='https://github.com/Thixiaoxiao/cxyx',
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
