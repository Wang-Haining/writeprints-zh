from writeprints_static.base import WriteprintsStatic


# tests on lexical features
# word level: 3 features
def test_total_words():
    texts = ["This is a text.", "This is another text."]
    vec = WriteprintsStatic()
    X = vec.transform(texts)
    assert X.shape[0] == 2
    total_words_index = vec.feature_names_.index("total_words")
    assert X[0, total_words_index] == 4  # words in first text
    assert X[1, total_words_index] == 4  # words in second text


def test_avg_word_length():
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index = vec.feature_names_.index("avg_word_length")
    assert X[0, feature_index] == 22 / 5
    assert X[2, feature_index] == 20 / 6


def test_short_words():
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index = vec.feature_names_.index("short_words")
    assert X[0, feature_index] == 2
    assert X[1, feature_index] == 2
    assert X[2, feature_index] == 4
    assert X[3, feature_index] == 2


# character level: 3 features
def test_total_chars():
    corpus = [
        "This is the first document.",
        "This document is the second document.\t",
        "And this is the third one.",
        "Is this the first document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index = vec.feature_names_.index("total_chars")
    assert X[0, feature_index] == 27
    assert X[1, feature_index] == 37
    assert X[2, feature_index] == 26
    assert X[3, feature_index] == 27


def test_digits_ratio():
    corpus = [
        "This is the 1st document.",
        "This document is the 2nd document.",
        "And this is the 3rd one.",
        "Is this the first document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index = vec.feature_names_.index("digits_ratio")
    assert X[0, feature_index] == 1 / 25
    assert X[1, feature_index] == 1 / 34
    assert X[2, feature_index] == 1 / 24
    assert X[3, feature_index] == 0


def test_uppercase_ratio():
    corpus = [
        "This is the 1st document.",
        "This document is the 2nd document.",
        "And this is the 3rd one.",
        "Is this the FIRST document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index = vec.feature_names_.index("uppercase_ratio")
    assert X[0, feature_index] == 1 / 25
    assert X[1, feature_index] == 1 / 34
    assert X[2, feature_index] == 1 / 24
    assert X[3, feature_index] == 6 / 27


# this test can be more complex because `\` is the escape character
def test_special_char_():
    corpus = [
        "This is the first document which is ~ nonsense distribution.",
        "This document is the second document @ whoever concerns.",
        "And this is the third | fourth one.",
        r"Is this the first document\?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index_0 = vec.feature_names_.index("special_char_tilde")
    feature_index_1 = vec.feature_names_.index("special_char_at")
    feature_index_2 = vec.feature_names_.index("special_char_vertical_bar")
    feature_index_3 = vec.feature_names_.index("special_char_backslash")
    assert X[0, feature_index_0] == 1
    assert X[1, feature_index_1] == 1
    assert X[2, feature_index_2] == 1
    assert X[3, feature_index_3] == 1


def test_letter_():
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index_0 = vec.feature_names_.index("letter_d")
    feature_index_1 = vec.feature_names_.index("letter_o")
    feature_index_2 = vec.feature_names_.index("letter_g")
    feature_index_3 = vec.feature_names_.index("letter_s")
    assert X[0, feature_index_0] == 1
    assert X[1, feature_index_1] == 3
    assert X[2, feature_index_2] == 0
    assert X[3, feature_index_3] == 3


def test_digit_():
    corpus = [
        "This is the 1st document.",
        "This document is the 2nd document.",
        "And this is the 533rd one.",
        "Is this the first document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index_0 = vec.feature_names_.index("digit_1")
    feature_index_1 = vec.feature_names_.index("digit_7")
    feature_index_2 = vec.feature_names_.index("digit_3")
    feature_index_3 = vec.feature_names_.index("digit_8")
    assert X[0, feature_index_0] == 1
    assert X[1, feature_index_1] == 0
    assert X[2, feature_index_2] == 2
    assert X[3, feature_index_3] == 0


def test_bigram_():
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index_0 = vec.feature_names_.index("bigram_is")
    feature_index_1 = vec.feature_names_.index("bigram_ea")
    feature_index_2 = vec.feature_names_.index("bigram_th")
    feature_index_3 = vec.feature_names_.index("bigram_ng")
    assert X[0, feature_index_0] == 2
    assert X[1, feature_index_1] == 0
    assert X[2, feature_index_2] == 3
    assert X[3, feature_index_3] == 0


def test_trigram_():
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is that the first document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index_0 = vec.feature_names_.index("trigram_the")
    feature_index_1 = vec.feature_names_.index("trigram_ing")
    feature_index_2 = vec.feature_names_.index("trigram_ion")
    feature_index_3 = vec.feature_names_.index("trigram_tha")
    assert X[0, feature_index_0] == 1
    assert X[1, feature_index_1] == 0
    assert X[2, feature_index_2] == 0
    assert X[3, feature_index_3] == 1


def test_hapax_legomena_ratio():
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        'And this is the third "THE".',
        "Is this the first document or the second document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index = vec.feature_names_.index("hapax_legomena_ratio")
    assert X[0, feature_index] == 1
    assert X[1, feature_index] == 4 / 5
    assert X[2, feature_index] == 4 / 5
    assert X[3, feature_index] == 5 / 7


def test_dis_legomena_ratio():
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        'And this is the third "THE".',
        "Is this the first document or the second document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index = vec.feature_names_.index("dis_legomena_ratio")
    assert X[0, feature_index] == 0
    assert X[1, feature_index] == 1 / 5
    assert X[2, feature_index] == 1 / 5
    assert X[3, feature_index] == 2 / 7
