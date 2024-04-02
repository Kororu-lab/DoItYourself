from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SimilarityCalculator:
    @staticmethod
    def calculate_jaccard_index(subreddit_authors, target_subreddit):
        target_authors = subreddit_authors.get(target_subreddit, set())
        jaccard_scores = {}
        for subreddit, authors in subreddit_authors.items():
            intersection = len(target_authors.intersection(authors))
            union = len(target_authors.union(authors))
            jaccard_scores[subreddit] = intersection / union if union else 0
        return jaccard_scores

    @staticmethod
    def calculate_tfidf_similarity(tfidf_matrix, subreddits, target_subreddit):
        target_index = subreddits.index(target_subreddit)
        target_vector = tfidf_matrix[target_index]
        similarities = cosine_similarity(tfidf_matrix, target_vector).flatten()
        return dict(zip(subreddits, similarities))

    @staticmethod
    def calculate_word2vec_similarity(word2vec_model, subreddits, target_subreddit):
        target_vector = word2vec_model.wv[target_subreddit]
        similarities = {}
        for subreddit in subreddits:
            if subreddit in word2vec_model.wv:
                sim = cosine_similarity([word2vec_model.wv[subreddit]], [target_vector])[0][0]
                similarities[subreddit] = sim
            else:
                similarities[subreddit] = 0
        return similarities
