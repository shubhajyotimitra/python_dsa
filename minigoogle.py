import heapq
import re
from collections import defaultdict

# ------------------------------
# Step 1: Dummy Web Pages
# ------------------------------
pages = {
    "page1.html": "Python is a powerful programming language. Python is widely used in AI and data science.",
    "page2.html": "Data structures and algorithms are the foundation of computer science.",
    "page3.html": "Machine learning and deep learning use Python for implementation.",
    "page4.html": "Artificial Intelligence overlaps with data science and machine learning.",
    "page5.html": "Google uses algorithms to rank web pages efficiently."
}

# ------------------------------
# Step 2: Preprocessing Helper
# ------------------------------
STOP_WORDS = {"is", "a", "the", "and", "of", "in", "to", "with", "for", "are"}

def preprocess(text):
    """Convert to lowercase, remove stopwords & punctuation."""
    words = re.findall(r"\w+", text.lower())
    return [w for w in words if w not in STOP_WORDS]

# ------------------------------
# Step 3: Build Inverted Index
# ------------------------------
class SearchEngine:
    def __init__(self, pages):
        self.index = defaultdict(list)   # word -> list of (page, freq)
        self.page_word_count = defaultdict(lambda: defaultdict(int))
        self.build_index(pages)

    def build_index(self, pages):
        for page, content in pages.items():
            words = preprocess(content)
            for word in words:
                self.page_word_count[page][word] += 1

        # Fill inverted index
        for page, word_freq in self.page_word_count.items():
            for word, freq in word_freq.items():
                self.index[word].append((page, freq))

    def search(self, query, top_k=3):
        query_words = preprocess(query)
        scores = defaultdict(int)

        # Simple TF-based scoring
        for word in query_words:
            for page, freq in self.index.get(word, []):
                scores[page] += freq

        # Use a max heap for ranking
        heap = [(-score, page) for page, score in scores.items()]
        heapq.heapify(heap)

        results = []
        for _ in range(min(top_k, len(heap))):
            score, page = heapq.heappop(heap)
            results.append((page, -score))

        return results

# ------------------------------
# Step 4: Run the Search Engine
# ------------------------------
engine = SearchEngine(pages)

while True:
    query = input("\n🔍 Enter your search query (or 'exit' to quit): ")
    if query.lower() == "exit":
        break
    results = engine.search(query)
    if results:
        print("📌 Top Results:")
        for page, score in results:
            print(f"   {page} (score: {score})")
    else:
        print("⚠️ No results found.")
