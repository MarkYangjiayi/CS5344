# CS5344  A Study of Echo Chamber Effect in the Context of Covid-19 Vaccination

# Table of contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Directory Structure](#directory_structure)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Plot](#plot)
- [References](#references)

# Introduction

This is the project of CS5344. 
Echo chambers have been a discussion since social media become an important part of people’s daily lives. The advantage it has compared to traditional media makes it suitable for information spreading, as well as fake news and polarized opinion, which are some of the root causes of why echo chambers exist. **In this project, we study the topic of detecting and analyses of echo chambers from heated topics on covid-19 vaccination on Twitter **.  

We achived **two goals**: 
(i) to analyze and study the echo chambers of Twitter attitudes around vaccines
(ii) to develop tools that can identify those who may be potential targets for intervention (i.e. people with vaccine hesitancy).



[(Back to top)](#table-of-contents)

# Dataset

**1. Dataset Source:**  [Download link](https://drive.google.com/drive/folders/1YIk4phkw-2Ki_Ih11RSOv7BAd9su4x0D?usp=sharing) (Six Datasets that are crawled by our own)
Download the data and put it to the `./data` folder.

**2. Dataset Introduction:**

 Six Datasets are crawled by applying the [Twint tool](https://github.com/twintproject/twint) with the following keywords: \#Covid-19 Vaccine, \#Pfizer and \#Sinovac. The collection includes two time periods  March 1, 2021 \- July 1, 2021 and Dec 01, 2021 \- Mar 01, 2022 and includes 799422 tweets. The attributes are included in the datasets are *id, conversation\_id, created\_at, date, time, timezone, user\_id, username, name, place, tweet, mentions, urls, relies\_count, retweet\_count, likes\_count, hashtags, cashtags, link, retweet, quote\_url, video, near, retweet\_id, reply\_to*.

[(Back to top)](#table-of-contents)

# Directory_Structure

```
|-- Final_Project
    |-- .gitignore
    |-- README.md
    |-- env.sh
    |-- environment.yml
    |-- main_mention.ipynb
    |-- main_reply.ipynb
    |-- package-lock.json
    |-- package.json
    |-- Data_Description_Visualization
    |   |-- Data_analysis_description.ipynb
    |-- New_data_visualization_code
    |   |-- EDA
    |   |   |-- introductory-eda.ipynb
    |   |-- Pfizer_BioNTech2_visualization.csv
    |   |-- Pfizer_BioNTech_visualization.csv
    |   |-- covid19_1_visualization
    |   |-- covid19_2_visualization
    |   |-- sivonac2_visualization
    |   |-- sivonac_visualization
    |-- Twint
    |   |-- vaccine_5344_twint.ipynb
    |-- analysis
    |   |-- Sentiment_Analysis.ipynb
    |   |-- analysis_utils.py
    |   |-- community analysis_mention.ipynb
    |   |-- community analysis_reply.ipynb
    |   |-- __pycache__
    |   |   |-- analysis_utils.cpython-37.pyc
    |   |   |-- utils.cpython-37.pyc
    |   |   |-- utils.cpython-38.pyc
    |   |-- mention
    |   |   |-- p1
    |   |   |-- p2
    |   |   |-- s1
    |   |   |-- s2
    |   |   |-- v1
    |   |   |-- v2
    |   |-- reply
    |       |-- p1
    |       |-- p2
    |       |-- sin1
    |       |-- sin2
    |       |-- v1
    |       |-- v2
    |-- controversy
    |   |-- change_side_controversy.py
    |   |-- logs.py
    |   |-- random_walks.py
    |   |-- start_controversy.py
    |   |-- utils.py
    |-- data
    |   |-- __init__.py
    |   |-- build_graph.py
    |   |-- preprocessing.py
    |   |-- sentiment.py
    |   |-- stopwords.txt
    |   |-- stopwords_vader.txt
    |   |-- utils.py
    |-- partition
        |-- community_detection.py
        |-- logs.py
        |-- utils.py

```
[(Back to top)](#table-of-contents)

# Installation

```git init```

```git clone https://github.com/MarkYangjiayi/CS5344.git```

[(Back to top)](#table-of-contents)

# Dependencies

```
conda env create -f environment.yml
```
If you failed with installation you may need to check the prefix in `environment.yml`.
```
conda activate cs5344
sh env.sh # set root folder
```

[(Back to top)](#table-of-contents)


# Usage

Use `Visual Studio` to open the project and Run the following 	`ipynb` files to obtain results of each part

 **1. Data Crawling**
 - [vaccine_5344_twint.ipynb](https://github.com/MarkYangjiayi/CS5344/blob/main/Twint/vaccine_5344_twint.ipynb)
 
 **2. Data Preprocessing & EDA**
 - [Data_analysis_description.ipynb](https://github.com/MarkYangjiayi/CS5344/blob/main/Data_Description_Visualization/Data_analysis_description.ipynb)
 - introductory-eda.ipynb

 **3. Construct Echo Chamber**
 - [main_mention.ipynb](https://github.com/MarkYangjiayi/CS5344/blob/main/main_mention.ipynb)
 - [main_reply.ipynb](https://github.com/MarkYangjiayi/CS5344/blob/main/main_reply.ipynb)

**4. Analysis**
 - [Sentiment_Analysis.ipynb](https://github.com/MarkYangjiayi/CS5344/blob/main/analysis/Sentiment_Analysis.ipynb)
 - [community analysis_mention.ipynb](https://github.com/MarkYangjiayi/CS5344/blob/main/analysis/community%20analysis_mention.ipynb)
 - [community analysis_reply.ipynb](https://github.com/MarkYangjiayi/CS5344/blob/main/analysis/community%20analysis_reply.ipynb)

[(Back to top)](#table-of-contents)

# Plot
Use **Gephi** to open Echo chamber diagrams
 - Six Echo chamber diagrams: [Download Link](https://drive.google.com/drive/folders/1qv98RuFSnwoCbo22L7F1IsVtbRQ9esTo?usp=sharing)
 - Download the software Gephi from https://gephi.org/.
 
[(Back to top)](#table-of-contents)

# References
[Echo chamber detection and analysis](https://link.springer.com/article/10.1007/s13278-021-00779-3)

[Are we always in strife? A longitudinal study of the echo chamber effect in the Australian Twittersphere](https://arxiv.org/abs/2201.09161)

[(Back to top)](#table-of-contents)


