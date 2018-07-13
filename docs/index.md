### Features

- Scraps Article on mutiple topics at once;
- Saves Fomatted word file containing headers and text scaped;
- Uses Python 3, wikipedia, BeautifulSoup,  requests, Python-docx and more to efficiently scrap and save docs;
- Uses **AWS** for processing of documents.

#### Upcoming Features
- Save in multiple format. PDF etc.
- Mutithreading for different topics to reduce scraping time.
- Output reference links from wikipedia


# Articulate


![](https://akashnotes.com/img/placeholders/photos/articulate_mini_logo.png)

 ![](https://img.shields.io/badge/release%20date-june-blue.svg) ![](https://img.shields.io/badge/tag-python-brightgreen.svg) ![](https://img.shields.io/badge/release-v1.0.0-blue.svg) ![](https://img.shields.io/badge/issue-1-red.svg)
---
### Web demo
https://akashnotes.com/articulate.html

![](https://akashnotes.com/img/placeholders/photos/articulate_web.png)
### Introduction
Articulate is a software to prepare articles on single or multiple topics at once. It saves the articles in MS-Word automatically with a little formatting. Novice developers are welcomed to do modification and contribute to the repository.

### Source Code
https://github.com/akshkr/articulate

### Installing Articulate

- Install dependencies

```python
	pip install -r requirements.txt
```

### How to run

This software can be run in ways

- Using CLI
- Using API

##### CLI - Command Line arguments

Run the following command after installing requirements
```python
    python driver.py --config CLI
```
This invokes CLI mode of the software.

![](https://akashnotes.com/img/placeholders/photos/articulate_cli.png)

The file will be saved in the current dir named articulate.docx

##### API mode

The following file shows implementation of Articulate API used in the web interface
```python
    from driver import MainDriver
    
    md_obj = MainDriver()
    
    # Put your string in place of "input_string"
    returned_file = md_obj.article_maker("input_string")
```
The returned_file is the word file with articles.


&nbsp;

&nbsp;

&nbsp;




