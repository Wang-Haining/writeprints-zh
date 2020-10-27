# Features

This page describes the features of Writeprints-Static.

The main resource we rely on to recover the Writeprints-Static feature set is Table II (p. 12: 12) of 
[Brennan et al. (2012)](https://dl.acm.org/doi/abs/10.1145/2382448.2382450), as follows. 

|Group       |Category|No. of Features| &nbsp; &nbsp; &nbsp; &nbsp;Description &nbsp; &nbsp; &nbsp; &nbsp;|
|:----:|:----:|:----:|:----|
| Lexical    | Word Level                | 3       | Total words, average word length, number of short words  |
|            | Character Level           | 3       | Total char, percentage of digits, percentage of uppercase letters  |
|            | Special Character         | 21      | Occurrence of special characters   |
|            | Letters                   | 26      | Letter frequency   |
|            | Digits                    | 10      | Digit frequency   |
|            | Character Bigram          | 39      | Percentage of common bigrams   |
|            | Character Trigram         | 20      | Percentage of common trigrams   |
|            | Vocabulary Richness       | 2       | Ratio of hapax legomena and dis legomena   |
| Syntactic  | Function Words            | 403     | Frequency of function words   |
|            | POS Tags                  | 22      | Frequency of Parts of speech tag   |
|            | Punctuation               | 8       | Frequency and percentage of colon, semicolon, qmark, period, exclamation, comma   |

When it comes to uncertainty, we refer to the documentation of 
[Jstylo](https://github.com/psal/jstylo/blob/bdc5a9e79adb35795819de147bb21ce2908ae45d/jsan_resources/feature_sets/writeprints_feature_set.xml), a
privacy enhancing tool sharing multiple authors to Brennan et al. (2012).
Though we try to reproduce the Writeprints-Static feature set as finely as possible, alternative ways and justification
 will be given if we cannot reimplement some features exactly.



## Lexical Features

### Word Level
Word tokenizer plays big role in calculating word level features since it defines what is a "word." SpaCy's default word
tokenizer works slightly differently than familiar NLTK tokenize methods (i.e. work_tokenize and casual_tokenize) when
 it comes to hyphen and other things.

#### Total Words
Total words in a given text, all spaces and punctuations are excluded. In practice, we use tokenized (`token.text`)
filtered with re pattern (`r'[^\w]+$'`).

#### Average Word Length
Average number of characters per word in a given text. In practice, we count the length of concatenation of character 
included in `total words` over the number of `total words`.

#### Number of Short Words
Total words shorter than four characters in a given text. In practice, we count tokens in `totol words` which has 1, 2, 
or 3 characters.

### Character Level

#### Total Characters
Total number of characters in the document. In practice, we count in spaces (`[ \t\n\r\f\v]`), punctuations, and other
characters (with len()), only leaving spaces after the last non-space trunked (with `rstrip()`).

#### Percentage of Digits
Percentage of digits over all characters. In practice, we count all the digits over `total characters`.
#### Percentage of Uppercase Letters
Percentage of uppercase letters out of the total characters in the document. In practice, we count all the capitalized
characters over `total characters`.

#### Occurrence of Special Characters
Frequencies of special characters, 21 in total. The special characters are "~", "@", "#", "$", "%", "^", "&", "*", "-", "_", "=", "+", ">", "<", "[", "]", "{", "}",
"/", "\\", "|".  In practice, we count all the special characters over `total characters`.

### Letters
#### Letter Frequencies
Frequencies of letters, case insensitive, 26 in total. In practice, we count all the English letters over
`total characters`.

### Digits
#### Digit Frequencies
Frequencies of digits in the document, 10 in total. In practice, we count every digit over `total characters`.

### Character Bigram
#### Percentage of Common Bigrams
Most common letter bigrams, case insensitive. In practice,
Bigrams are taken only within words
(do not cross adjacent words).
varies in total, by default 50.
All the most-frequent POS/character/word ngrams are sorted by Brown corpus (Francis& Kucera, 1979).  
### Character Trigram
#### Percentage of Common Trigrams
Most common letter trigrams (e.g. aaa, aab etc.), case insensitive. Trigrams are taken only within words
(do not cross adjacent words).
varies in total, by default 50.
All the most-frequent POS/character/word ngrams are sorted by Brown corpus (Francis& Kucera, 1979).  
### Vocabulary Richness

Hapax legomena over all word tokens.

Dis legomena over all word tokens.
## Syntactic Features

### Function Words
512 common function words, used by Koppel et al., (2005).
or customed by user.
you can lookup it here, or use XXX to print the set out.

### POS Tags
Part-Of-Speech tags extracted by spaCy "en_core_web_sm" model.
Originally POS taggering did by the Stanford POS Maxent Tagger, but the developer team suggested to use
"the much better CoreNLPPOSTagger class" instead.
OntoNotes 5 / Penn Treebank
https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
https://github.com/explosion/spacy-models/releases//tag/en_core_web_sm-2.3.1
55 in total.
### Punctuation

Punctuation symbols like . , ! etc.
13 in total.
["...", ".", "!", "?", ",", ";", ":", "'", '"', '“', '”', '‘', '’']
        
## Caveat

Writeprints-Static uses [spaCy 2.x](https://spacy.io/) under the hood. This means it utilizes the default word tokenizer of
 spaCy, which is different from the default ([`word_tokenize`](https://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.punkt.PunktLanguageVars.word_tokenize)) 
 and [`casual_tokenize`](https://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.casual.casual_tokenize) of [NLTK 3.5](https://www.nltk.org/).
Several differences are listed below.
```python
# to do

```