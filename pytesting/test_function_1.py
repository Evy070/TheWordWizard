#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
from pytest import approx

from Main_Code_Python import read_text_file

def test_read_text_file():

    # Test with an invalid file path
    invalid_path = "nonexistent_file.txt"
    result = read_text_file(invalid_path)  # Call the function you're testing
    assert result is None, "Expected None for a file that does not exist."
    
    # Test with a valid file path (make sure this file exists in the same directory)
    valid_path = "4_Input_Sample_Text_Mercedes_Benz.txt"  # Replace with a valid .txt file
    result = read_text_file(valid_path)
    assert isinstance(result, str), "Expected file content to be a string."
    assert len(result) > 0, "Expected non-empty file content."
