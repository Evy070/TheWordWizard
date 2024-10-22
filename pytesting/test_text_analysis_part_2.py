#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pytest
from pytest import approx

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
    expected_avg_word_length = 28 / 9  # 28 characters without spaces, 9 words
    assert analysis['average_word_length'] == approx(expected_avg_word_length, rel=1e-2), f"Expected average word length {expected_avg_word_length}, got {analysis['average_word_length']}"


