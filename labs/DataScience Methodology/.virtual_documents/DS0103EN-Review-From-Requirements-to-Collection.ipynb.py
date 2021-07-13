# check Python version
get_ipython().getoutput("python -V")


import pandas as pd # download library to read data into dataframe
pd.set_option('display.max_columns', None)

recipes = pd.read_csv("https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DS0103EN/labs/data/recipes.csv")

print("Data read into dataframeget_ipython().getoutput("") # takes about 30 seconds")


recipes.head()


recipes.shape
