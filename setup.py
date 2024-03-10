from  setuptools import setup, find_packages

setup(
    name='dse2e',
    version='0.0.3',
    description='A package which contains all functions which are required by a practisioneer to perform industry specific tasks will a single line of code (WIP)',
    author=["Udai Agarwal", "Siddharth Shorya"],
    author_email=["udaiag@gmail.com", "shoryasiddharth90@gmail.com"],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your_package_name",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)