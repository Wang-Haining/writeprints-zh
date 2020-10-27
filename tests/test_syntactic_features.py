from writeprints_static.base import WriteprintsStatic


def test_function_word_():
    corpus = [
        "This is the first document.",
        'This document is the second "THE".',
        "And this is the third one.",
        "Is this the first document?",
        "I've seen this before.",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 5
    feature_index_0 = vec.feature_names_.index("function_word_is")
    feature_index_1 = vec.feature_names_.index("function_word_the")
    feature_index_2 = vec.feature_names_.index("function_word_this")
    feature_index_3 = vec.feature_names_.index("function_word_ours")
    feature_index_4 = vec.feature_names_.index("function_word_i've")
    assert X[0, feature_index_0] == 1
    assert X[1, feature_index_1] == 2
    assert X[2, feature_index_2] == 1
    assert X[3, feature_index_3] == 0
    assert X[4, feature_index_4] == 1


def test_pos_():
    corpus = [
        "This is the first document.",
        'This document is the second "THE".',
        "And this is the third one.",
        "Is that a document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index_0 = vec.feature_names_.index("pos_NOUN")
    feature_index_1 = vec.feature_names_.index("pos_AUX")
    feature_index_2 = vec.feature_names_.index("pos_DET")
    feature_index_3 = vec.feature_names_.index("pos_ADJ")
    assert X[0, feature_index_0] == 1
    assert X[1, feature_index_1] == 1
    assert X[2, feature_index_2] == 2
    assert X[3, feature_index_3] == 0


def test_more_pos_():
    corpus = [
        "The black cat sat on the blue mat.",
        "The Black Cat is a hotel in Boston.",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)

    # first sentence
    assert X[0, vec.feature_names_.index("pos_DET")] == 2
    assert X[0, vec.feature_names_.index("pos_ADJ")] == 2
    assert X[0, vec.feature_names_.index("pos_NOUN")] == 2
    assert X[0, vec.feature_names_.index("pos_VERB")] == 1
    assert X[0, vec.feature_names_.index("pos_ADP")] == 1
    assert X[0, vec.feature_names_.index("pos_PUNCT")] == 1

    # second sentence
    assert X[1, vec.feature_names_.index("pos_DET")] == 2
    assert X[1, vec.feature_names_.index("pos_PROPN")] == 3
    assert X[1, vec.feature_names_.index("pos_NOUN")] == 1
    assert X[1, vec.feature_names_.index("pos_ADP")] == 1
    assert X[1, vec.feature_names_.index("pos_AUX")] == 1
    assert X[1, vec.feature_names_.index("pos_PUNCT")] == 1


def test_punctuation_():
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        'And this is the "real" one.',
        "Is this the first document?",
    ]
    vec = WriteprintsStatic()
    X = vec.transform(corpus)
    assert X.shape[0] == 4
    feature_index_0 = vec.feature_names_.index("punctuation_period")
    feature_index_1 = vec.feature_names_.index("punctuation_comma")
    feature_index_2 = vec.feature_names_.index("punctuation_double_quotes")
    feature_index_3 = vec.feature_names_.index("punctuation_question_mark")
    assert X[0, feature_index_0] == 1
    assert X[1, feature_index_1] == 0
    assert X[2, feature_index_2] == 2
    assert X[3, feature_index_3] == 1
