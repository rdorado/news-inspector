import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="news-inspector",
    version="0.1.1",
    author="Ruben Dorado",
    author_email="ruben.dorados@gmail.com",
    description="Utilities to analyze and extract information from news",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rdorado/news-inspector",
    packages=setuptools.find_packages(),
    install_requires=[
        'scikit-learn>=0.17.1', 'sklearn-crfsuite>=0.3'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)

