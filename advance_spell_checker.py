import re

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.freq = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, freq=1):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.freq += freq

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end


class SpellChecker:
    def __init__(self):
        self.trie = Trie()
        self.word_set = set()

    def load_dictionary(self, words):
        for word in words:
            self.trie.insert(word.lower())
            self.word_set.add(word.lower())

    def is_correct(self, word):
        return word.lower() in self.word_set

    def edit_distance(self, w1, w2):
        n, m = len(w1), len(w2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif w1[i - 1] == w2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[n][m]

    def suggest(self, word, max_suggestions=3):
        suggestions = []
        for dict_word in self.word_set:
            dist = self.edit_distance(word.lower(), dict_word)
            if dist <= 2:  # threshold
                suggestions.append((dist, dict_word))
        suggestions.sort(key=lambda x: (x[0], x[1]))
        return [w for _, w in suggestions[:max_suggestions]]

    def check_paragraph(self, text, auto_correct=False):
        words = re.findall(r"\b\w+\b", text)
        corrected_text = []

        for word in words:
            if self.is_correct(word):
                corrected_text.append(word)
            else:
                suggestions = self.suggest(word)
                if auto_correct and suggestions:
                    corrected_text.append(suggestions[0])  # pick best suggestion
                else:
                    corrected_text.append(word)
                    if suggestions:
                        print(f"❌ '{word}' not found. Suggestions: {suggestions}")
                    else:
                        print(f"❌ '{word}' not found. No suggestions.")

        return " ".join(corrected_text)


# ---------------- DRIVER CODE ---------------- #
if __name__ == "__main__":
    dictionary = [
        "hello", "world", "python", "placement", "spell", "checker",
        "algorithm", "data", "structure", "interview", "company", "correct"
    ]

    sc = SpellChecker()
    sc.load_dictionary(dictionary)

    print("=== Spell Checker (CLI Tool) ===")
    text = input("Enter a paragraph: ")

    print("\n--- Checking Spelling ---")
    corrected = sc.check_paragraph(text, auto_correct=False)

    print("\n--- Auto-Corrected Version ---")
    auto_corrected = sc.check_paragraph(text, auto_correct=True)
    print(auto_corrected)
