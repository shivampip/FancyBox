import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fancybox",
    version="0.0.1",
    author="Shivam Agrawal",
    author_email="shivam301296@gmail.com",
    description="Print beautiful message boxes on command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shivampip/FirstPyPl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)