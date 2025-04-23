class TrieNode:
    def __init__(self):
        #Initialize a TrieNode with an empty dictionary for children and pages
        self.children = {}
        self.pages = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()  #Create an empty root node at initialization

    #Inserts a word into the trie
    #Associates it with a given page and its frequency
  
    def insert(self, word, page, count=1):
        node = self.root

        #Traverse each character in the word
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  #Create node if not present
            node = node.children[char]

        #Update frequency of the word on the specific page
        if page in node.pages:
            node.pages[page] += count
        else:
            node.pages[page] = count

    #Searches for a word in the trie, Returns dictionary of pages and their counts where the word appears
    def search(self, word):
        node = self.root

        # Follow the path of the word character-by-character
        for char in word:
            if char not in node.children:
                return None 
            node = node.children[char]

        return node.pages if node.pages else None 
    
    #Public method to retrieve all words stored in the trie
    #Useful for computing TF-IDF across all indexed terms
  
    def get_all_words(self):
        result = []
        self._collect_words(self.root, "", result)
        return result

    #Recursive helper to traverse the trie and collect all complete words

    def _collect_words(self, node, prefix, result):
        if node.pages:
            result.append(prefix)
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, result)
