#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Main_Code_Python import generate_visualizations

import os

def test_generate_visualizations():
    # Create a mock analysis result
    mock_analysis = {
        'word_count': 9,
        'sentence_count': 2,
        'paragraph_count': 1,
        'character_count': 36,
        'character_count_no_spaces': 28,
        'average_word_length': 28 / 9
    }
    
    mock_text = "This is a test. This is only a test."

    # Generate the visualizations
    generate_visualizations(mock_analysis, mock_text)

    # Check if the images are created
    assert os.path.exists("7_output_counts_chart.png"), "Counts chart image should be created."
    assert os.path.exists("8_output_character_chart.png"), "Character chart image should be created."
    assert os.path.exists("9_output_word_length_histogram.png"), "Word length histogram image should be created."

