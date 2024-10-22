#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
from pytest import approx
import os

from Main_Code_Python import read_text_file, analyze_text, generate_visualizations, generate_pdf_report

def test_all_functions():
    # ===================== Test read_text_file ===================== #
    
    # Test with an invalid file path
    invalid_path = "nonexistent_file.txt"
    result = read_text_file(invalid_path)
    assert result is None, "Expected None for a file that does not exist."

    # Test with a valid file path (make sure this file exists in the same directory)
    valid_path = "4_Input_Sample_Text_Mercedes_Benz.txt"  # Replace with a valid .txt file
    result = read_text_file(valid_path)
    assert isinstance(result, str), "Expected file content to be a string."
    assert len(result) > 0, "Expected non-empty file content."
    
    # ===================== Test analyze_text ===================== #
    
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
    expected_avg_word_length = 28 / 9  # 28 characters without spaces, 9 words
    assert analysis['average_word_length'] == approx(expected_avg_word_length, rel=1e-2), f"Expected average word length {expected_avg_word_length}, got {analysis['average_word_length']}"
    
    # ===================== Test generate_visualizations ===================== #
    
    # Create a mock analysis result
    mock_analysis = {
        'word_count': 9,
        'sentence_count': 2,
        'paragraph_count': 1,
        'character_count': 36,
        'character_count_no_spaces': 28,
        'average_word_length': 28 / 9
    }

    # Generate the visualizations
    generate_visualizations(mock_analysis, mock_text)

    # Check if the images are created
    assert os.path.exists("7_output_counts_chart.png"), "Counts chart image should be created."
    assert os.path.exists("8_output_character_chart.png"), "Character chart image should be created."
    assert os.path.exists("9_output_word_length_histogram.png"), "Word length histogram image should be created."

    # ===================== Test generate_pdf_report ===================== #
    
    # Generate the PDF report
    generate_pdf_report(mock_analysis, mock_text)

    # Check if the PDF report is created
    assert os.path.exists("10_output_analysis_report.pdf"), "PDF report should be created."

