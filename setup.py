from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ipafetch",
    version="0.1.0",
    author="Andrew Garcia",
    author_email="drewgarcia23@gmail.com",
    description="A tool to fetch IPA files from Apple Configurator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drewg233/ipafetch",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
    ],
    python_requires=">=3.6",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ipafetch=ipafetch.ipafetch:main',
        ],
    },
) 