from writeprints_static.base import WriteprintsStatic
import pytest


def test_transform():
    texts = ["This is a text.", "This is another text."]
    vec = WriteprintsStatic()
    X = vec.transform(texts)
    assert X is not None
    assert len(X.shape) == 2


def test_wrong_input_type_1():
    texts = "This is a text."
    vec = WriteprintsStatic()
    with pytest.raises(ValueError) as e:
        X = vec.transform(texts)
    assert (
        str(e.value)
        == f"""List of raw text documents expected, {type(texts)} object received."""
    )


def test_wrong_input_type_2():
    texts = ["This is a text.", None, 8]
    vec = WriteprintsStatic()
    with pytest.raises(ValueError) as e:
        X = vec.transform(texts)
    assert (
        str(e.value)
        == f"""List of raw text documents expected, {[type(m) for m in texts]} object received."""
    )


def test_wrong_input_type_3():
    texts = ["This is a text.", ""]
    vec = WriteprintsStatic()
    with pytest.raises(ValueError) as e:
        X = vec.transform(texts)
    assert str(e.value) == """Remove zero-length string."""


def test_fit_transform():
    texts = ["This is a text.", "This is another text."]
    vec = WriteprintsStatic()
    X = vec.fit_transform(texts)
    assert X is not None
    assert len(X.shape) == 2


def test_get_feature_names():
    texts = ["This is a text.", "This is another text."]
    vec = WriteprintsStatic()
    X = vec.fit_transform(texts)
    feature_names = vec.get_feature_names()
    assert feature_names is not None
    assert len(feature_names) == 552
    assert feature_names[2] == "short_words"
    assert feature_names[50] == "letter_x"
    assert feature_names[265] == "function_word_thousand"
    assert feature_names[548] == "punctuation_single_quotes"
