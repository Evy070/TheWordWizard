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

# Extensive Outline

### **1. Planning**

#### **What do you want to do?**
- **Goal**: Develop a Python program that takes a text file as input, performs a detailed analysis of the text, and outputs both statistical data and visualizations. The final output will be a downloadable PDF report summarizing the analysis and including the relevant visualizations.
  
#### **Requirements**:
  1. **Text File Input**: The program should accept a text file (e.g., `.txt`) and read its contents.
  2. **Text Analysis**: The program should count the number of:
     - Words
     - Sentences
     - Paragraphs
     - Characters (with and without spaces)
     - Calculate the average word length.
  3. **Visualizations**: Generate the following charts:
     - Bar chart for word, sentence, and paragraph counts.
     - Horizontal bar chart for character counts (with and without spaces).
     - Histogram for word length distribution.
  4. **PDF Report**: Create a downloadable PDF report that includes:
     - The text file input.
     - Summary of the analysis (statistics like word count, sentence count, etc.).
     - Generated visualizations as images.

#### **Constraints**:
- **File Format**: Only `.txt` files will be accepted for simplicity.
- **Libraries**: The project should use standard Python libraries and only lightweight external libraries (`nltk`, `matplotlib`, `fpdf`).
- **Report Structure**: The PDF must be simple and clear, with limited customization options.

#### **Risks**:
- **Input File Size**: Large files may slow down analysis, especially during the tokenization of text.
  - **Mitigation**: Limit file size to a manageable number of characters or optimize processing techniques.
- **Tokenization Accuracy**: Incorrect splitting of sentences and words may occur in poorly formatted text files.
  - **Mitigation**: Use robust text processing libraries like `nltk` to handle various text cases (e.g., abbreviations, punctuation).
- **PDF Layout Complexity**: The process of embedding multiple visualizations into the PDF could be complex.
  - **Mitigation**: Keep the visual layout simple and standard, embedding images in a straightforward way.

---

### **2. Design**

#### **How will you do it?**

1. **Input Handling Component**:
   - **Objective**: Allow the user to upload a text file (`.txt`).
   - **Implementation**:
     - Use Python's `open()` function to read the file's contents.
     - Add error handling for cases where the file is missing, in the wrong format, or too large.

2. **Text Analysis Component**:
   - **Objective**: Analyze the text to count words, sentences, paragraphs, characters, and calculate average word length.
   - **Implementation**:
     - **Word Count**: Use `nltk.word_tokenize()`.
     - **Sentence Count**: Use `nltk.sent_tokenize()` or split based on common sentence terminators.
     - **Paragraph Count**: Split text based on double newline characters (`\n\n`).
     - **Character Count**: Use `len(text)` and `len(text.replace(" ", ""))` for with and without spaces.
     - **Average Word Length**: Compute using the total character count (without spaces) divided by the number of words.

3. **Visualization Component**:
   - **Objective**: Create and display the required charts.
   - **Implementation**:
     - Use `matplotlib` to generate:
       - A **bar chart** for word, sentence, and paragraph counts.
       - A **horizontal bar chart** for character counts.
       - A **histogram** for word length distribution.
     - Save the visualizations as `.png` images using `plt.savefig()`.

4. **PDF Generation Component**:
   - **Objective**: Generate a PDF report with the text file input, a summary of the analysis and including the charts.
   - **Implementation**:
     - Use `fpdf` to create the PDF.
     - Add text-based summaries (word counts, character counts, etc.).
     - Embed the saved chart images into the PDF using `fpdf.image()`.

5. **User Interface (Optional)**:
   - **Objective**: Allow users to upload text files and download the PDF report.
   - **Implementation**:
     - If a UI is needed, tools like **Streamlit** or **Tkinter** can provide a simple interface.
     - For this project, I guess this will not be necessary.

---

#### **How do the components interact?**

1. **Input Handling**: 
   - The user uploads a `.txt` file.
   - The Input Handling component reads and stores the file's contents as a string.

2. **Text Analysis**:
   - The text string is passed to the Text Analysis component.
   - The analysis is performed, and word, sentence, paragraph, and character counts are returned as statistics.

3. **Visualization**:
   - The analysis results are passed to the Visualization component.
   - Charts are generated and saved as image files.

4. **PDF Generation**:
   - The analysis results and saved chart images are passed to the PDF Generation component.
   - A PDF report is created and saved to the user's system.

5. **User Interaction**:
   - The user uploads the file and downloads the PDF report after the analysis and visualizations are complete.
