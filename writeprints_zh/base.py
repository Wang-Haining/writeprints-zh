"""This module is used to hold the WriteprintsStatic class.

writeprints-static aims to reproduce the feature set, Writeprints Static, used in Brennan et al. (2012).

Writeprints Static contains the lexical and syntactic subset of the original Writeprints feature set first proposed by
Abbasi et al. in 2008, which achieved the SOTA for vanilla authorship attribution. We believe Writeprints is adapted
from Zheng et al. (2006), which builds on many other valuable works. This feature set is widely used in forensics
(Orebaugh et al. 2014), adversarial stylometry (Faust et al. 2017, McDonald et al. 2012), and online security (Afroz et
al. 2012， Chen et al. 2008， Ghasem et al).

We try to reproduce the Writeprints-Static feature set as finely as possible. The main resource we rely on to recover
the Writeprints Static feature set is Table II (p. 12: 12) of Brennan et al. (2012). When it comes to uncertainty, we
refer to the documentation of [Jstylo](https://github.com/psal/jstylo/blob/bdc5a9e79adb35795819de147bb21ce2908ae45d/
jsan_resources/feature_sets/writeprints_feature_set.xml), which is a privacy enhancing tool sharing multiple authors to
Brennan et al. (2012). Technical details and known differences are stated under features' docstrings.

Installation:

```bash
pip install writeprints-static
```

Getting started

writeprints-static.WriteprintsStatic implements Writeprints Static (Brennan et al. 2012). The interface follows
conventions found in scikit-learn.

The following demonstrates how to extract Writeprints Static features.

```python
from writeprints import WriteprintsStatic as WPS

texts = ["Colorless green ideas sleep furiously.", "Furiously sleep ideas green colorless.", 'James, while John had had
        "had", had had "had had"; "had had" had had a better effect on the teacher.']

vec = WPS()

# The input only accepts list of English string, so there is no need to specify input type as usually did for
# scikit-learn.
# Output X is a scipy.sparse.csr_matrix instance
X = vec.transform(texts)
```

Requirements
Python 3.8+ is required. The following packages are required
- spacy 2.3.2+
- en_core_web_sm 2.3.1
- scipy 1.5.2+
- numpy 1.18.5+

Important links:
- Documentation: https://github.com/literary-materials/writeprints-static
- Source code: https://github.com/literary-materials/writeprints-static/writeprints_static
- Issue tracker: https://github.com/literary-materials/writeprints-static/issues

Other implementations:
- writeprints: A less decent implementation.

License:
This package is licensed under the MIT License.

Reference:

    Abbasi, A., & Chen, H. (2008). Writeprints: A stylometric approach to identity-level identification and similarity
    detection in cyberspace. ACM Transactions on Information Systems (TOIS), 26(2), 1-29.

    Zheng, R., Li, J., Chen, H., & Huang, Z. (2006). A framework for authorship identification of online messages:
    Writing‐style features and classification techniques. Journal of the American society for information science and
    technology, 57(3), 378-393.

    Brennan, M., Afroz, S., & Greenstadt, R. (2012). Adversarial stylometry: Circumventing authorship recognition to
    preserve privacy and anonymity. ACM Transactions on Information and System Security (TISSEC), 15(3), 1-22.

    Overdorf, R., & Greenstadt, R. (2016). Blogs, Twitter feeds, and Reddit comments: Cross-domain authorship
    attribution. Proceedings on Privacy Enhancing Technologies, 2016(3), 155-171.

    Orebaugh, A., Kinser, J., & Allnutt, J. (2014). Visualizing instant messaging author writeprints for forensic
    analysis.

    Afroz, S., Brennan, M., & Greenstadt, R. (2012, May). Detecting hoaxes, frauds, and deception in writing style
    online. In 2012 IEEE Symposium on Security and Privacy (pp. 461-475). IEEE.

    Chen, Y. D., Abbasi, A., & Chen, H. (2008, June). Developing ideological networks using social network analysis and
    writeprints: A case study of the international Falun Gong movement. In 2008 IEEE International Conference on
    Intelligence and Security Informatics (pp. 7-12). IEEE.

    Ghasem, Z., Frommholz, I., & Maple, C. (2015). A Machine Learning Framework to Detect and Document Text-Based
    Cyberstalking. In LWA (pp. 348-355).

    Faust, C., Dozier, G., Xu, J., & King, M. C. (2017). Adversarial authorship, interactive evolutionary hill-climbing,
    and author CAAT-III. In 2017 IEEE Symposium Series on Computational Intelligence (SSCI) (pp. 1-8). IEEE.

    McDonald, A. W., Afroz, S., Caliskan, A., Stolerman, A., & Greenstadt, R. (2012, July). Use fewer instances of the
    letter “i”: Toward writing style anonymization. In International Symposium on Privacy Enhancing Technologies
    Symposium (pp. 299-318). Springer, Berlin, Heidelberg.
"""

import re
import warnings
import en_core_web_sm
import numpy as np
from scipy.sparse import csr_matrix
from writeprints_static import lexical_features as lex
from writeprints_static import syntactic_features as syn


class WriteprintsStatic(object):
    """WriteprintsStatic

    The main class does the heavy lifting.

    Attributes:
        raws: A list of raw text fed by user.
        docs: A list of spaCy's doc instances build on self.raws with en_core_web_sm.
        tags: A list of list of POS, derived from token.pos_ in self.docs.
        word_tokens: A list of list of word tokens, derived from token.text in self.docs.
        feature_names_: A list of feature names.
    """

    def __init__(self):
        """Initiates WriteprintsStatic."""
        self.docs = None
        self.raws = None
        self.tags = None
        self.word_tokens = None
        self.feature_names_ = None
        self._nlp_max_length = None

    def transform(self, input):
        """

        Generates values for WriteprintsStatic instance.

        Note that no explicit check of the input language will be executed, but we do assume the user only feed in
        English documents.

        Args:
            input: A list of English raw texts (in string type).

        Returns:
            A scipy.sparse.csr_matrix instance. Use .toarray() to unpack the return to see the values.

        Raises:
            ValueError: an error if the input is not a list of string or the

        """
        if isinstance(input, list):
            if all(isinstance(m, str) for m in input):
                self.raws = input
            else:
                raise ValueError(
                    f"""List of raw text documents expected, {[type(m) for m in input]} object received."""
                )
        else:
            raise ValueError(
                f"""List of raw text documents expected, {type(input)} object received."""
            )

        # checks the length
        # if any raw is longer than 10,000,000, raises an error.
        if any(1 if len(raw) > 10000000 else 0 for raw in self.raws):
            raise ValueError(
                """Pass in string containing less than 1,000,000 characters.\n
                   The texts in the list are expected to be less than 100,000 characters.\n"""
            )
        # if any raw longer than 1,000,000, warns user and increases the spaCy's nlp.max_length accordingly.
        elif any(1 if len(raw) > 1000000 else 0 for raw in self.raws):
            warnings.warn(
                """The texts in the list are expected to be less than 100,000 characters.""",
                UserWarning,
                stacklevel=2,
            )
            _nlp_max_length = round(len(self.raws) * 1.1)
        # if any raw is vacant, raises an error in case of incoming ZeroDivision errors.
        elif any(1 if len(raw) == 0 else 0 for raw in self.raws):
            raise ValueError("""Remove zero-length string.""")
        else:
            _nlp_max_length = 1000000
        # loads the language model and tune the max_length
        nlp = en_core_web_sm.load()
        nlp.max_length = _nlp_max_length
        # removes unwanted processing procedure for better efficiency
        with nlp.disable_pipes("ner"):
            self.docs = [nlp(raw) for raw in self.raws]
        self.word_tokens = [
            [
                token_without_punkt.lower()
                for token_without_punkt in [token.text for token in doc]
                if re.compile(r"[^\w]+$").match(token_without_punkt) is None
            ]
            for doc in self.docs
        ]
        self.tags = [[token.pos_ for token in doc] for doc in self.docs]

        results, labels = zip(
            lex.total_words_extractor(self.word_tokens),
            lex.avg_word_length_extractor(self.word_tokens),
            lex.short_words_extractor(self.word_tokens),
            lex.total_chars_extractor(self.raws),
            lex.digits_ratio_extractor(self.raws),
            lex.uppercase_ratio_extractor(self.raws),
            lex.special_char_extractor(self.raws),
            lex.letter_extractor(self.raws),
            lex.digit_extractor(self.raws),
            lex.bigram_extractor(self.word_tokens),
            lex.trigram_extractor(self.word_tokens),
            lex.hapax_legomena_ratio_extractor(self.word_tokens),
            lex.dis_legomena_ratio_extractor(self.word_tokens),
            syn.function_word_extractor(self.raws),
            syn.pos_extractor(self.tags),
            syn.punctuation_extractor(self.raws),
        )

        results = np.concatenate(results, axis=1)
        self.feature_names_ = sum(labels, [])

        return csr_matrix(results)

    def fit_transform(self, input):
        """See self.transform."""
        return self.transform(input)

    def get_feature_names(self):
        """Returns Writeprints-Static feature names."""
        return self.feature_names_
