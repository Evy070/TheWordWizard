#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Main_Code_Python import generate_pdf_report

import os

def test_generate_pdf_report():
    # Mock analysis and text
    mock_analysis = {
        'word_count': 9,
        'sentence_count': 2,
        'paragraph_count': 1,
        'character_count': 36,
        'character_count_no_spaces': 28,
        'average_word_length': 28 / 9
    }
    
    mock_text = "This is a test. This is only a test."

    # Generate the PDF report
    generate_pdf_report(mock_analysis, mock_text)

    # Check if the PDF report is created
    assert os.path.exists("10_output_analysis_report.pdf"), "PDF report should be created."

