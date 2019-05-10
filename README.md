news-inspector
===========================================

[![MIT License](https://badgen.net/badge/license/MIT/)](http://opensource.org/licenses/MIT)
[![Scrutinizer Quality Score](https://scrutinizer-ci.com/g/rdorado/news-inspector/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/rdorado/site-analyzer/)
[![Build Status](https://travis-ci.com/rdorado/news-inspector.svg?branch=master)](https://travis-ci.com/rdorado/news-inspector)

News-inspector is a free software library for analyzing and acquiring information from news. It features a collection of NLP and machine learning tasks that can be used to analyze news articles such as:

* classification
* named entity recognition
* knowledge-based article search

All the methods can be easily configured and trained/retrained. Once trained, they can be loaded and used on new articles.

Requirements
===========================================

* Python >=3.4
* scikit-learn>=0.17.1
* sklearn-crfsuite>=0.3
* nltk>=3.24

Installation
===========================================

```python
pip install news-inspector
```

Quick start
===========================================

Train the model:

```python 
from news_inspector import GenericClassifier
train_model(GenericClassifier, "myconfig.xml", "myclassifier.model");
```

Load and use the model:

```python
from news_inspector import load_model

model = load_model("myclassifier.model");
result = model.classify(text);
```

Documentation
===========================================

Read the docs at https://news-inspector.readthedocs.io/en/latest/.
