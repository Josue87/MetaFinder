
from setuptools import setup, find_packages
import metafinder


setup(
    name='metafinder',
    version=metafinder.__version__,
    author='Josue Encinar (@JosueEncinar)',
    description='MetaFinder - Metadata search through Google',
    include_package_data=True,
    license='GNU GPLv3+',
    packages=find_packages(),
    url="https://github.com/Josue87/MetaFinder",
    entry_points={
        'console_scripts': [
            'metafinder=metafinder.cli:main',
        ],
    },
    install_requires=[
        "requests",
        "pypdf2",
        "beautifulsoup4",
        "openpyxl",
        "wget",
        "python-docx",
        "python-pptx"
    ]
)
