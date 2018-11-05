import setuptools

__version__ = '1.0.0'

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="secrecy",
    version=__version__,
    author="Benjamin Soyka",
    description="A simple and secure secret message encoder/decoder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bsoyka/secrecy",
    keywords=[
        'encryption',
        'security',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests==2.20.0',
        'sentry-sdk==0.5.3',
    ],
    include_package_data=True,
)
