# The Software Development

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
- **Libraries**: The project should use standard Python libraries and only lightweight external libraries (`nltk`, `matplotlib`, `seaborn` and `fpdf`).
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

---

### **3. Implementation**

#### **Writing The Code**

Writing the code involves breaking down each component into functions. Each function includes docstrings that explains what the function does, the input it expects, and the output it returns. The main steps include: Writing functions for reading the input file, performing text analysis, creating visualizations, and generating the PDF report. And following good coding practices such as readability and proper variable naming protocols.

---

### **4. Testing**

#### **Does the code do what it is supposed to do?**

To ensure that the code functions as expected, pytest is used to analyze the software.

##### Unit Testing: Each function is tested individually using pytest.
- The file input is correctly processed.

- The text analysis functions return accurate results. 

- The visualizations are generated without errors.
  
- PDF generation is tested to ensure that the final report includes both text and images as expected.

  
##### Final Test: Run pytest on the full code to check if the code passes all test cases by calling all functions into one test function.

All outputs generated by the code and the pytest code can be found in this github repository.

---

### **5. Documentation**

#### **How do you use the code? How does it work? How do you contribute to it?**

- README: Including a README.md file that covers the project overview, installation steps, usage instructions, and contribution guidelines to help new users and developers get started quickly.
- Docstrings: Docstrings can be founded in for each function and are called by the help() function. Ensure every function in the code is properly documented with docstrings explaining its purpose, parameters, and return values.
- Screenshots: Including relevant screenshots showing examples of the input file, analysis results, visualizations, and the final PDF report can all be found in this github repository.

---

### **6. Deployment**

#### **How do you share the code with others? How do you make it easy for others to use it?**

- Packaging: Packag the Python project for distribution, including all dependencies (like nltk, matplotlib, seaborn and fpdf) in a requirements.txt file.
- Distribution: Considering uploading the package to PyPI (Python Package Index) to make it easily installable using pip. This can be installed for users, like so:

`pip install thewordwizard`

---