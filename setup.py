import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.readlines()    
    
setuptools.setup(
    name="news-inspector",
    version="0.1.1",
    author="Ruben Dorado",
    author_email="ruben.dorados@gmail.com",
    description="News-inspector is a library for analyzing and extracting information from news articles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rdorado/news-inspector",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)

