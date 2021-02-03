
from setuptools import setup
from setuptools import find_packages
import metafinder


with open("requirements.txt") as iF:
    requirements = iF.read().splitlines()


setup(
    name='metafinder',
    version=metafinder.__version__,
    author='Josué Encinar (@JosueEncinar)',
    description='MetaFinder - Metadata search through Google',
    include_package_data=True,
    license='GNU GPLv3+',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'metafinder=metafinder.cli:main',
        ],
    },
    install_requires=requirements
)
