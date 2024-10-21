#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from nltk.tokenize import word_tokenize, sent_tokenize

def read_text_file(file_path):
    """
    Reads the content of a .txt file.
    
    :parameter file_path: Path to the text file.
    :return: The content of the file as a string or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found! Please provide a valid file path.")
        return None

file_path = 'mercedesbenz.txt'
content = read_text_file(file_path)

if content is not None:
    print(content)


# In[ ]:




