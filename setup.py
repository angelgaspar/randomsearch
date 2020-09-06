import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randomsearch",
    version="0.0.1",
    author="Angel Gaspar",
    author_email="engineer.angel.gaspar@gmail.com",
    description="A simple n-dimensional random search algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/angelgaspar/randomsearch",
    keywords=['randomsearch', 'random search', 'optimization', 'algorithm'],
    install_requires=[
        'numpy'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
