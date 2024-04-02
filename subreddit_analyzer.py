import pandas as pd
from text_preprocessor import TextPreprocessor
from data_streamer import DataStreamer
from vectorizers import TfidfVectorizerCustom, Word2VecVectorizer
from similarity_calculator import SimilarityCalculator
import os

class SubredditAnalyzer:
    def __init__(self, directory, year_month, target_subreddit):
        self.directory = directory
        self.year_month = year_month
        self.target_subreddit = target_subreddit
        self.text_preprocessor = TextPreprocessor()

    def analyze(self):
        subreddit_texts, subreddit_authors = self.aggregate_data()
        
        # Vectorize using TF-IDF
        tfidf_vectorizer = TfidfVectorizerCustom()
        tfidf_matrix = tfidf_vectorizer.vectorize(list(subreddit_texts.values()))
        
        # Train and vectorize using Word2Vec
        word2vec_vectorizer = Word2VecVectorizer()
        word2vec_model = word2vec_vectorizer.vectorize(list(subreddit_texts.values()))
        
        # Calculate similarities
        similarities = SimilarityCalculator()
        tfidf_similarities = similarities.calculate_tfidf_similarity(tfidf_matrix, list(subreddit_texts.keys()), self.target_subreddit)
        word2vec_similarities = similarities.calculate_word2vec_similarity(word2vec_model, list(subreddit_texts.keys()), self.target_subreddit)
        jaccard_scores = similarities.calculate_jaccard_index(subreddit_authors, self.target_subreddit)

        self.save_results(list(subreddit_texts.keys()), jaccard_scores, tfidf_similarities, word2vec_similarities)

    def aggregate_data(self):
        subreddit_texts = {}
        subreddit_authors = {}
        file_pattern = f'RC_{self.year_month}.csv'
        file_path = os.path.join(self.directory, file_pattern)
        usecols = ['subreddit', 'author', 'body']

        data_streamer = DataStreamer(file_path, usecols, self.text_preprocessor)
        for subreddit, author, text in data_streamer.stream_data():
            subreddit_texts[subreddit] = subreddit_texts.get(subreddit, "") + " " + text
            if subreddit not in subreddit_authors:
                subreddit_authors[subreddit] = set()
            subreddit_authors[subreddit].add(author)

        return subreddit_texts, subreddit_authors

    def save_results(self, subreddits, jaccard_scores, tfidf_similarities, word2vec_similarities):
        results_df = pd.DataFrame({
            'Subreddit': subreddits,
            'Jaccard Index': [jaccard_scores[sub] for sub in subreddits],
            'TF-IDF Similarity': [tfidf_similarities[sub] for sub in subreddits],
            'Word2Vec Similarity': [word2vec_similarities[sub] for sub in subreddits]
        }).sort_values(by='Jaccard Index', ascending=False)

        results_file_path = os.path.join(self.directory, f'subreddit_similarities_{self.year_month}.csv')
        results_df.to_csv(results_file_path, index=False)
        print(f"Similarity calculations completed and results saved to {results_file_path}")
