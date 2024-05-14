
# DoItYourself: An Automatic Subreddit Relativity Index Machine

## About DoItYourself
DoItYourself is a tool designed to automatically compute the relevance of various subreddits based on monthly raw data from Reddit. The tool leverages different computational methods to analyze and determine the similarity between subreddits, ultimately representing these similarities as an index.

## Data Source
The data for this project is sourced from the Reddit archive project available on r/DataHoarder. The primary API used for data retrieval is the PushShift API, which provides comprehensive access to Reddit's historical data.

## Workflow
The workflow of the DoItYourself project can be summarized in the following steps:

1. **Data Collection and Preprocessing**
   - Use the `data_streamer.py` script to collect monthly raw data (comments and submissions) from Reddit using the PushShift API.
   - Preprocess the collected data to extract necessary information such as subreddit names and authors.

2. **Similarity Calculation**
   - The `similarity_calculator.py` script includes methods to calculate the similarity between subreddits based on the collected data.
   - The primary methods used for similarity calculation are:
     - **Jaccard Index**: Measures the similarity between subreddits based on the authors contributing to them.
     - **TF-IDF Cosine Similarity**: Computes similarity based on the textual content of the submissions and comments.

3. **Analysis Execution**
   - The `subreddit_analyzer.py` script orchestrates the data loading, similarity calculations, and result generation.
   - It utilizes the `SimilarityCalculator` class to apply the Jaccard Index and TF-IDF Cosine Similarity methods.

4. **Main Execution Script**
   - The `main.py` script serves as the entry point of the project.
   - It takes three command-line arguments: `<year-month>`, `<target_subreddit>`, and `<directory>`.
   - The script initializes the `SubredditAnalyzer` class and triggers the analysis process.

## Installation
To set up the DoItYourself project, follow these steps:

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd DoItYourself
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
To run the analysis, use the following command:
```sh
python main.py <year-month> <target_subreddit> <directory>
```
For example, to analyze data from January 2021 for the subreddit `python`, use:
```sh
python main.py 2021-01 python ./data
```
The results will be stored in the specified directory.

## Device/Environment
The project was developed and tested on machines with the following environment:
- Python 3.8 or higher
- Required Python packages (listed in `requirements.txt`)

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments
Special thanks to the Reddit community and the developers of the PushShift API for providing access to the data used in this project.
