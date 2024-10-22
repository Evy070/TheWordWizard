# The Word Wizard 
## Evy de Bruine - 4649052
This project is a Python application designed to analyze text files and generate the final products through visualizations and a report. 

## Features

- **Input Handling**: Accepts `.txt` files for analysis.
- **Text Analysis**:
  - **Word Count**: Total number of words in the text.
  - **Sentence Count**: Total number of sentences.
  - **Paragraph Count**: Total number of paragraphs.
  - **Character Counts**: Total characters with and without spaces.
  - **Average Word Length**: Computes the average length of words.
- **Visualizations**:
  - **Word, Sentence, and Paragraph Counts**: Bar chart with three bars showing counts for words, sentences, and paragraphs.
  - **Character Counts**: Horizontal bar chart with two bars showing total characters and characters without spaces.
  - **Average Word Length**: Histogram displaying word length distribution.
- **PDF Creation**:
  - **Output Generation**: PDF report of the text analysis. Including the input text, text analysis numbers and visualizations.

## Output

- **Visualizations**: Saves all generated graphs and images. Users can download these.
- **PDF Report**: Generates a PDF report summarizing all analyses with charts, statistics and other visualizations. Users can download this report.

## Required Libraries

- `nltk`
- `matplotlib`
- `seaborn`
- `fpdf`

## Installation

To install the required libraries and the final program package, use 'pip install'.

## Usage

1. **Input**: Place your text file (`.txt` format) in the project directory.
2. **Run the Script**: Execute the Python script to analyze the text and generate visualizations.
3. **Output**: Visualizations and a PDF report will be created, including charts and analysis results.
