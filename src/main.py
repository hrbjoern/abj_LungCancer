# General modules: 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

# Particular modules: 
from aux01 import print_data_head
from preprocessing import preprocess_data
from modeling import train_model
from evaluation import test_model


 
# DS steps:  (all from Copilot ;-)) 
# 1. Data collection:
# 2. Data cleaning:
# 3. Data exploration:
# 4. Data modeling:
# 5. Data evaluation:
# 6. Data deployment:


# 1. Data collection:
data = pd.read_csv('../data/healthcare-dataset-stroke-data.csv')
# Test: 
print_data_head(data)


# 2. Data cleaning:
preprocessed_data = preprocess_data(data)


# 4. Data modeling:
trained_model = train_model(preprocessed_data)

# 5. Data evaluation:
test_model(trained_model, preprocessed_data)