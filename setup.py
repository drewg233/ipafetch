from setuptools import setup, find_packages

setup(
    name="ipafetch",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "ipafetch=ipafetch.ipafetch:main",
        ],
    },
    author="drewg233",
    description="A tool to fetch IPA files",
    python_requires=">=3.6",
) 