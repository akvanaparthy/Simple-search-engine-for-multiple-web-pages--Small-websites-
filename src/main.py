#
# This project implements a simplified search engine that scrapes and indexes content from a set of webpages using a 
# Trie data structure. It supports efficient word lookups and leverages **TF-IDF (Term Frequency - Inverse Document Frequency) 
# for ranking search results. The content is preprocessed to remove stop words and special characters, 
# focusing indexing only on meaningful keywords.

# Name: Akshay Vanaparthi
# Project: Simple search engine for a small website

#Required libraries for web scraping, data processing, and math
import os
import requests
from bs4 import BeautifulSoup
from trie import Trie
import re
from collections import defaultdict
import math

#Set of stop words to ignore common words during indexing
STOP_WORDS = set([...])  #(truncated for brevity)

#Function to fetch and return the plain text content of a webpage

def fetch_website_content(url):
    try:
        #Check if the URL is valid
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')  #Parsing the HTML content
        return soup.get_text()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website {url}: {e}")
        return ""

#Function to clean and filter the raw text
#Removes punctuation, non-alphanumeric characters, and stop words

def preprocess_text(text):
    words = text.lower().split()  #Convert to lowercase and tokenize
    processed_words = []
    for word in words:
        cleaned_word = re.sub(r'[^a-zA-Z0-9]', '', word)  #Keep only alphanumeric, optional
        if cleaned_word.isalnum() and cleaned_word not in STOP_WORDS:
            processed_words.append(cleaned_word)
    return processed_words

#Function to compute the TF-IDF scores for each term-page pair
#TF = term frequency in a document
#IDF = inverse document frequency across all documents

def compute_tf_idf_correctly(trie, total_docs, doc_freq):
    tfidf_scores = defaultdict(dict)  #{term: {page: score}}
    for term in trie.get_all_words():
        pages = trie.search(term)
        if not pages:
            continue
        idf = math.log(total_docs / doc_freq[term]) if doc_freq[term] else 0  #Compute IDF
        for page, tf in pages.items():
            tfidf = tf * idf  #TF-IDF score = term freq * IDF
            tfidf_scores[term][page] = tfidf
    return tfidf_scores


#Function to crawl a list of URLs, process their content, and build an inverted index (trie) with TF-IDF scoring

def index_websites(urls):
    trie = Trie() 
    doc_freq = defaultdict(int)
    total_docs = len(urls)

    for url in urls:
        content = fetch_website_content(url)
        words = preprocess_text(content)
        word_seen = set()  #To track unique words in this document
        word_counts = defaultdict(int)  #{term: frequency in this doc}

        for word in words:
            word_counts[word] += 1
            if word not in word_seen:
                doc_freq[word] += 1
                word_seen.add(word)

        for word, count in word_counts.items():
            trie.insert(word, url, count)

    #Compute TF-IDF for all terms and pages
    tfidf_scores = compute_tf_idf_correctly(trie, total_docs, doc_freq)
    return trie, tfidf_scores


# Function to search for a term in the index and displayresults sorted by their TF-IDF scores

def search_term(trie, term, tfidf_scores):
    results = trie.search(term)
    if results:
        # Sort pages by TF-IDF score in descending order
        ranked = sorted(results.items(), key=lambda x: tfidf_scores[term].get(x[0], 0), reverse=True)
        print(f"\nThe term '{term}' is found in the following pages (Ranked by TF-IDF):")
        for page, count in ranked:
            print(f"  - {page}: TF-IDF: {tfidf_scores[term].get(page, 0):.4f} (Count: {count} time(s))")
    else:
        print(f"\nThe term '{term}' was not found in any pages.")

#Loads a list of URLs, indexes them, and runs search queries

if __name__ == "__main__":
    urls = [
        "https://www.programiz.com/dsa",
        "https://www.programiz.com/dsa/data-structure-types",
        "https://www.programiz.com/dsa/linked-list",
        "https://www.programiz.com/dsa/stack",
        "https://www.programiz.com/dsa/queue",
        "https://www.programiz.com/dsa/trees",
        "https://www.programiz.com/dsa/graph",
        "https://www.programiz.com/dsa/heap-data-structure",
        "https://www.programiz.com/dsa/deque",
        "https://www.programiz.com/dsa/getting-started"
    ]

    #Build index and calculate TF-IDF
    trie, tfidf_scores = index_websites(urls)

    #Perform search queries and print ranked results
    search_term(trie, "data", tfidf_scores) #For notmal testing
    search_term(trie, "stack", tfidf_scores) #For testing at URL Slug
    search_term(trie, "graph", tfidf_scores) 
    search_term(trie, "nonexistent", tfidf_scores)  #For testing absence
