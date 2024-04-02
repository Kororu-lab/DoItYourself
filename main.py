import sys
from subreddit_analyzer import SubredditAnalyzer

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <year-month> <target_subreddit> <directory>")
        sys.exit(1)
    
    year_month = sys.argv[1]
    target_subreddit = sys.argv[2]
    directory = sys.argv[3]
    
    analyzer = SubredditAnalyzer(directory, year_month, target_subreddit)
    analyzer.analyze()

if __name__ == "__main__":
    main()
