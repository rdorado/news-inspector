import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="news-inspector",
    version="0.0.1",
    author="Ruben Dorado",
    author_email="ruben.dorados@gmail.com",
    description="Utilities to analyze and extract information from news",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rdorado/news-inspector",
    install_requires=[
        'scikit-learn'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
