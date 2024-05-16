# Text Analysis Project

Welcome to the Text Analysis Project! This project provides a modular and flexible framework for analyzing text files. It includes functionalities such as word frequency analysis, word cloud generation, sentence summarization, and various visualizations. The project is organized in a way that allows you to run individual analyses or all of them together, ensuring a clean and efficient workflow.

## Table of Contents

- [Text Analysis Project](#text-analysis-project)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Description of the Structure](#description-of-the-structure)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Running All Analyses](#running-all-analyses)
    - [Running Individual Analyses](#running-individual-analyses)
    - [Cleaning Outputs](#cleaning-outputs)

## Features

- **Text Analysis**: Compute basic statistics about the text, including sentence count, word count, unique word count, lexical diversity, and average sentence length.
- **Word Cloud**: Generate a word cloud image from the most frequent words.
- **Distributions**: Plot distributions of word lengths and parts of speech (POS) tags.
- **Summarization**: Generate a concise summary of the text.
- **Cleanup**: Ensure the output directory is clean before running analyses to prevent conflicts.

## Description of the Structure

- **text_analysis/**: Root directory for the project.
  - **__init__.py**: Initializes the `text_analysis` package.
  - **main.py**: Main script to run all analyses.
  - **analyze.py**: Script for performing text analysis and generating an Excel report.
  - **visualize_wordcloud.py**: Script for generating a word cloud image.
  - **visualize_distributions.py**: Script for plotting word length and POS tag distributions.
  - **summarize.py**: Script for summarizing the text.
  - **utils/**: Directory for utility modules.
    - **__init__.py**: Initializes the `utils` subpackage.
    - **file_operations.py**: Contains functions for file operations.
    - **text_processing.py**: Contains functions for text processing.
    - **cleanup.py**: Contains the function to clean the `outputs` directory.
  - **data/**: Directory for input data.
    - **source_text.txt**: The source text file to be analyzed.
  - **outputs/**: Directory where generated files will be saved.
    - **(generated files will be saved here)**: Placeholder indicating where output files will be saved.
  - **requirements.txt**: File listing the required Python packages.


## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/text_analysis.git
    cd text_analysis
    ```

2. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download NLTK data (Optional)**:

    The following commands will download essential NLTK datasets needed for sentence tokenization, part-of-speech tagging, and stopword filtering. This step is not mandatory as these downloads are already handled in the code, but running them manually can help ensure all data is properly installed.

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('stopwords')
    ```

    You can run this code in a Python shell or add it to a setup script.

## Usage

### Running All Analyses

To run all analyses and generate outputs in the `outputs` directory, execute the following command:

```bash
python main.py
```
This will:

- Clean the outputs directory.
- Read the source text from data/source_text.txt.
- Perform text analysis and generate a detailed Excel report.
- Generate a word cloud image.
- Plot word length and POS tag distributions.
- Summarize the text and save the summary.


### Running Individual Analyses
Each functionality can be executed individually by running the respective scripts. Each script will clean the outputs directory before execution.

- Text Analysis:
```bash
python analyze.py
```

- Generate Word Cloud:
```bash
python visualize_wordcloud.py
```

- Plot Distributions:
```bash
python visualize_distributions.py
```

- Summarize Text:
```bash
python summarize.py
```

### Cleaning Outputs
If you need to manually clean the outputs directory, you can run:

```bash
python -m utils.cleanup
```
This will remove all files in the outputs directory.

<br>
<hr>
<br>
<br>

Thank you for using the Text Analysis Project! If you have any questions or suggestions, feel free to reach out. Happy analyzing!




