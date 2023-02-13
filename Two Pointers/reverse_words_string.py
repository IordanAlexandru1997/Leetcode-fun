def reverse_words(sentence):
    return " ".join(ss for ss in reversed(sentence.split()) if ss)
