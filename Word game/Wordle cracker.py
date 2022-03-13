import random
import collections, random
import enum

class Tip(enum.Enum):
    ABSENT = 0
    PRESENT = 1
    CORRECT = 2

def filter_words(words, guess, score):
   
    new_words = []
    for word in words:
        pool = collections.Counter(c for c, sc in zip(word, score) if sc != Tip.CORRECT)
        for char_w, char_g, sc in zip(word, guess, score):
            if sc == Tip.CORRECT and char_w != char_g:
                break  
            elif char_w == char_g and sc != Tip.CORRECT:
                break  
            elif sc == Tip.PRESENT:
                if not pool[char_g]:
                    break 
                pool[char_g] -= 1
            elif sc == Tip.ABSENT and pool[char_g]:
                break 
        else:
            new_words.append(word)  

    return new_words
with open("WORD.LST", "r") as f:
    words = [word.strip() for word in f.readlines() if len(word.strip()) == 5]

while len(words) > 1:
    print(f"Try {(guess := random.choice(words))!r}.")
    score = [int(char) for char in input(">>> ") if char in "012"]  
    words_ = []
    for word in words:
        pool = collections.Counter(c for c, sc in zip(word, score) if sc != 2)
        for w, g, sc in zip(word, guess, score):
            if ((sc == 2) != (w == g)) or (sc < 2 and bool(sc) != bool(pool[g])):
                break
            pool[g] -= sc == 1
        else:
            words_.append(word) 
    words = words_
print(words[0])
def get_random_word(words):
    print(f"I'll guess randomly from my pool of {len(words)} words...")
    sample = ", ".join(words[:8])
    end = ", among others..." if len(words) > 8 else "."
    print(f"I'm considering {sample}{end}")
    guess = random.choice(words)
    print(f"Hmmm, I'll guess {guess!r}...")
    return guess


def play_with_computer(words):
    print("What's the length of the secret word?")
    length = int(input("| "))
    words = [word for word in words if len(word) == length]

    mapping = {"0": Tip.ABSENT, "1": Tip.PRESENT, "2": Tip.CORRECT}
    print(f"\nNOTE: when typing scores, use {mapping}.\n")
    while len(words) > 1:
        guess = get_random_word(words)
        print("How did this guess score?")
        user_input = input("| ")
        sc = [mapping[char] for char in user_input if char in mapping]
        words = filter_words(words, guess, sc)
        print()

if __name__ == "__main__":
    WORD_LST = "WORD.LST"  
    with open(WORD_LST, "r") as f:
        words = [word.strip() for word in f.readlines()]
        words = play_with_computer(words) 

    if not words:
        raise RuntimeError("I don't know any words that could solve the puzzle...")
    print(f"The secret word must be {words[0]!r}!")
