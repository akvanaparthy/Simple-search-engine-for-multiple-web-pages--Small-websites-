# Search Engine using Trie with TF-IDF Ranking

## Overview
This project implements a simplified search engine that scrapes and indexes content from a set of webpages using a **Trie data structure**. It supports efficient word lookups and leverages **TF-IDF (Term Frequency - Inverse Document Frequency)** for ranking search results. The content is preprocessed to remove stop words and special characters, focusing indexing only on meaningful keywords.

## Objectives
- Crawl multiple web pages.
- Clean and process textual content.
- Index the content in a Trie data structure.
- Compute TF-IDF scores for words across documents.
- Support ranked keyword search with relevance scores.

## Dataset
Pages scraped from the [Programiz Data Structures and Algorithms Series](https://www.programiz.com/dsa), which includes introductory content on arrays, graphs, stacks, queues, and more.

## Project Structure

### `main.py`
The main controller script responsible for orchestrating all operations:
- **Fetching HTML:** Uses `requests` and `BeautifulSoup` to fetch and parse content from provided URLs.
- **Preprocessing:** Converts text to lowercase, strips non-alphanumeric characters, and removes stop words.
- **Indexing:** Stores each word from each document into a Trie, keeping track of its frequency per page.
- **TF-IDF Computation:** Calculates a relevance score for each word on each page based on how unique the word is across all documents.
- **Search:** Performs keyword search and returns URLs ranked by their TF-IDF score.

### `trie.py`
Contains the implementation of the Trie data structure:
- **TrieNode:** Represents each node in the Trie. Stores child nodes and a dictionary of URLs with frequency.
- **Trie:** Handles insertion, search, and retrieval of all words from the structure. Also supports retrieving all stored words (for global TF-IDF computation).

## Algorithm

### 1. **Content Fetching**
Each URL is fetched, parsed, and its visible text extracted for indexing.

### 2. **Text Preprocessing**
- Convert text to lowercase.
- Remove symbols and punctuation.
- Filter out common stop words.

### 3. **Word Indexing**
Each word is inserted into the Trie with:
- Its corresponding URL.
- Frequency of the word in that page.

### 4. **TF-IDF Computation**
For each word:
- **TF (Term Frequency):** Number of times a word appears in a specific document.
- **IDF (Inverse Document Frequency):** `log(Total Documents / Document Frequency)`.
- **TF-IDF:** `TF * IDF` for every (word, page) combination.

### 5. **Search Query Handling**
When a user searches a term:
- The Trie is queried.
- Pages containing the term are returned.
- Results are sorted by TF-IDF score for relevance.

## Example Output
```
The term 'stack' is found in the following pages (Ranked by TF-IDF):
  - https://www.programiz.com/dsa/stack: TF-IDF: 41.8877 (Count: 82 time(s))
  - https://www.programiz.com/dsa/data-structure-types: TF-IDF: 4.0866 (Count: 8 time(s))
  - https://www.programiz.com/dsa: TF-IDF: 0.5108 (Count: 1 time(s))
```

## Why Trie + TF-IDF?
- **Trie:** Fast and memory-efficient for indexing strings.
- **TF-IDF:** Captures both local importance (TF) and global uniqueness (IDF) of terms for ranking relevance.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Regular Expressions
- Math and Collections libraries

## Future Enhancements
- Implement search suggestions via prefix matching.
- Extend to support phrase search and logical operators.
- Cache crawled pages locally.

---
**Author:** Akshay Vanaparthi

**Project:** Simple eearch engine for a website

