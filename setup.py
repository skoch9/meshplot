import setuptools
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="meshplot",
    version="0.3.3",
    author="Sebastian Koch",
    author_email="",
    description="Interactive Plotting of 3D Triangle Meshes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skoch9/meshplot/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    test_suite="test"
)
