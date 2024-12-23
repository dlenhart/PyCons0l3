from setuptools import setup, find_packages

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

def read_file(file):
   with open(file) as f:
        return f.read()
    
version = read_file("VERSION")
requirements = read_requirements("requirements.txt")

setup(
    name = 'PyCons0l3',
    version = version,
    author = 'Drew D. Lenhart',
    author_email = 'dlenhart@gmail.com',
    url = 'https://github.com/dlenhart/pycons0l3/',
    description = 'Various python methods for console interaction.',
    long_description_content_type = "text/x-rst", 
    long_description = 'Various Python methods. Methods to make the console pretty, loading .ini files. See example scripts.',
    license = "MIT license",
    packages = find_packages(exclude=["test"]),
    install_requires = requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ] 
)