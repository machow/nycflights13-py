from setuptools import setup, find_namespace_packages

VERSION = '0.0.3'

with open('README.md', 'r') as f:
    README = f.read()

setup(
    name='nycflights13',
    packages=find_namespace_packages(),
    version=VERSION,
    description='A data package for nyc flights (the nycflights13 R package)',
    author='Michael Chow',
    license='CC0',
    author_email='mc_al_github@fastmail.com',
    url='https://github.com/machow/nycflights13',
    keywords=['package', ],
    install_requires=[
        "pandas>=0.24.0",
    ],
    python_requires=">=3.5",
    include_package_data=True,
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
