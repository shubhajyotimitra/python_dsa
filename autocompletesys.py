class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0  # Track frequency of word usage


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += 1  # Increment usage frequency

    # Get all words starting with a given prefix
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words(node, prefix)

    # Helper: DFS to collect words with frequencies
    def _find_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append((prefix, node.frequency))
        for char, next_node in node.children.items():
            words.extend(self._find_words(next_node, prefix + char))
        return words


# ===============================
# Autocomplete Demo (Upgraded)
# ===============================
if __name__ == "__main__":
    trie = Trie()

    # Pre-load dictionary words
    dictionary = ["apple", "application", "apply", "aptitude",
                  "banana", "ball", "bat", "batch",
                  "cat", "car", "carbon", "cartoon"]

    for word in dictionary:
        trie.insert(word)

    print("====== ✨ Smart Text Autocomplete System (Trie + Ranking + Learning) ======")

    while True:
        prefix = input("\nType a prefix (or 'exit' to quit): ").lower().strip()
        if prefix == "exit":
            print("👋 Exiting Autocomplete System.")
            break

        # Get suggestions sorted by frequency (high → low)
        suggestions = sorted(trie.starts_with(prefix), key=lambda x: -x[1])

        if suggestions:
            print(f"💡 Suggestions for '{prefix}':")
            for word, freq in suggestions:
                print(f"   {word} (used {freq} times)")
        else:
            print("❌ No suggestions found.")

            # Ask user if they want to add new word
            choice = input(f"➕ Do you want to add '{prefix}' as a new word? (y/n): ").lower()
            if choice == "y":
                trie.insert(prefix)
                print(f"✅ '{prefix}' added to dictionary!")
