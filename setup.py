import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="Students",
    version=version,
    author="Mateusz Cichos",
    author_email="mcichos45@gmail.com",
    description="Attendance management system for university",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CichyFlashy/Students",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["Students=main:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.10",
)