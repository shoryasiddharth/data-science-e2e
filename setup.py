from  setuptools import setup, find_packages

setup(
    name='dse2e',
    version='0.0.5',
    description='A package which contains all functions which are required by a practisioneer to perform industry specific tasks will a single line of code (WIP)',
    author= "Udai Agarwal, Siddharth Shorya",
    author_email="shoryasiddharth90@gmail.com",
    long_description=open('README.md').read() + "\n\nAuthors:\n - Author One <author.one@example.com>\n - Author Two <author.two@example.com>",
    long_description_content_type="text/markdown",
    url="https://github.com/shoryasiddharth/data-science-e2e",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)