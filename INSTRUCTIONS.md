Kaggle API
==========

The kaggle API is installed on local machine and reads username and password from `~/.kaggle/kaggle.json`<br>
The new token can be created in [profile Settings](https://www.kaggle.com/settings/account) -> `API` -> `Create new token`. It will create new `kaggle.json`<br>
There are some more instructions [online](https://www.kaggle.com/code/paultimothymooney/exploring-the-kaggle-api)

## Kaggle API instructions:

[Kaggle API](https://github.com/Kaggle/kaggle-api) is an open source code on github.

## Get data

```
mkdir data && cd data
kaggle competitions download -c predict-energy-behavior-of-prosumers
unzip predict-energy-behavior-of-prosumers.zip 
rm predict-energy-behavior-of-prosumers.zip 
```
Create a symlink to data folder so external notebooks work:
```
cd ..
mkdir -p /kaggle/input/predict-energy-behavior-of-prosumers/
ln -s ./data /kaggle/input/predict-energy-behavior-of-prosumers/data
```