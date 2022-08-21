<h1 align="center">Factors Affecting the Use of Yellow Taxis in NYC</h1>

## Install dependencies (Python 3.9)
```
pip install -r  requirements.txt
```

## Download datasets 
Datasets: Yellow Taxis, High Volume For-Hire Services Data and covid-19 between Nov 2021 and Feb 2022
```
python download.py
```

## Preprocess
E.g. remove irrelevant attributes, remove outliers.

```
python prepocess.py
```

## Train and Evaluate Model
Feature selection: mutual information\
Three splits: train/dev/test\
Two models: linear regression and random forest
```
python run.py
```