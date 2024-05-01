import re

class TeluguTokenizer:
    def __init__(self):
        self.token_pattern = re.compile(r'[\u0C00-\u0C7F]+|[^\s\w]+|\w+')

    def tokenize(self, text):
        tokens = self.token_pattern.findall(text)
        return tokens

if __name__ == "__main__":
    tokenizer = TeluguTokenizer()
    text = "తెలుగు భాషలో టోకెనైజర్ ఎలా తయారు చేయాలి?"
    tokens = tokenizer.tokenize(text)
    print(tokens)
