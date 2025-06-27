import random

# Sample text data (replace with a much larger dataset for better results)
text = "the quick brown fox jumps over the lazy dog the dog barks"

# Create a dictionary to store word pairs and their frequencies
word_pairs = {}
words = text.lower().split()

for i in range(len(words) - 1):
    pair = (words[i], words[i+1])
    if pair in word_pairs:
        word_pairs[pair] += 1
    else:
        word_pairs[pair] = 1

# Function to generate text
def generate_text(start_word, length):
    current_word = start_word.lower()
    generated_text = [current_word]

    for _ in range(length):
        next_word_candidates = []
        for pair, count in word_pairs.items():
            if pair[0] == current_word:
                next_word_candidates.extend([pair[1]] * count)  # Weight by frequency

        if next_word_candidates:
            next_word = random.choice(next_word_candidates)
            generated_text.append(next_word)
            current_word = next_word
        else:
            break  # No more words to follow

    return " ".join(generated_text)

# Generate text starting with "the"
generated = generate_text("the", 10)
print(generated)