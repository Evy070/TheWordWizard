#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pytest
from pytest import approx

from Main_Code_Final import read_text_file

def test_read_text_file():

    # Test with an invalid file path
    invalid_path = "nonexistent_file.txt"
    result = read_text_file(invalid_path)  # Call the function you're testing
    assert result is None, "Expected None for a file that does not exist."
    
    # Test with a valid file path (make sure this file exists in the same directory)
    valid_path = "mercedesbenz.txt"  # Replace with a valid .txt file
    result = read_text_file(valid_path)
    assert isinstance(result, str), "Expected file content to be a string."
    assert len(result) > 0, "Expected non-empty file content."



# In[2]:

from Main_Code_Final import analyze_text

def test_analyze_text():
    # Mock text for analysis
    mock_text = "This is a test. This is only a test."

    # Run analysis on the mock text
    analysis = analyze_text(mock_text)

    # Test word count
    assert analysis['word_count'] == 9, f"Expected 9 words, got {analysis['word_count']}"

    # Test sentence count
    assert analysis['sentence_count'] == 2, f"Expected 2 sentences, got {analysis['sentence_count']}"

    # Test paragraph count (since there's no \n\n, this should be 1)
    assert analysis['paragraph_count'] == 1, f"Expected 1 paragraph, got {analysis['paragraph_count']}"

    # Test character count (with and without spaces)
    assert analysis['character_count'] == 36, f"Expected 36 characters, got {analysis['character_count']}"
    assert analysis['character_count_no_spaces'] == 28, f"Expected 28 characters without spaces, got {analysis['character_count_no_spaces']}"

# Test average word length
    expected_avg_word_length = 29 / 7  # 29 characters without spaces, 7 words
    assert analysis['average_word_length'] == approx(expected_avg_word_length, rel=1e-2), f"Expected average word length {expected_avg_word_length}, got {analysis['average_word_length']}"



# In[3]:

from Main_Code_Final import generate_visualizations

import os

def test_generate_visualizations():
    # Create a mock analysis result
    mock_analysis = {
        'word_count': 7,
        'sentence_count': 2,
        'paragraph_count': 1,
        'character_count': 34,
        'character_count_no_spaces': 29,
        'average_word_length': 29 / 7
    }
    
    mock_text = "This is a test. This is only a test."

    # Generate the visualizations
    generate_visualizations(mock_analysis, mock_text)

    # Check if the images are created
    assert os.path.exists("counts_chart.png"), "Counts chart image should be created."
    assert os.path.exists("character_chart.png"), "Character chart image should be created."
    assert os.path.exists("word_length_histogram.png"), "Word length histogram image should be created."

    # Optionally, you can clean up by removing the files after the test
    os.remove("counts_chart.png")
    os.remove("character_chart.png")
    os.remove("word_length_histogram.png")


# In[4]:

from Main_Code_Final import generate_pdf_report

def test_generate_pdf_report():
    # Mock analysis and text
    mock_analysis = {
        'word_count': 7,
        'sentence_count': 2,
        'paragraph_count': 1,
        'character_count': 34,
        'character_count_no_spaces': 29,
        'average_word_length': 29 / 7
    }
    
    mock_text = "This is a test. This is only a test."

    # Generate the PDF report
    generate_pdf_report(mock_analysis, mock_text)

    # Check if the PDF report is created
    assert os.path.exists("text_analysis_report.pdf"), "PDF report should be created."

    # Optionally, clean up the generated PDF
    os.remove("text_analysis_report.pdf")


# In[ ]:




