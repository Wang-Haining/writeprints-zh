# Usage

This page describes how to use the writeprints-static package.

## Class
Writeprints-static has one main class Writeprints holds specification, does the heavy lifting, and returns a 
[scipy.sparse.csr_matrix](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html) instance.

```python
class Writeprints(input='content',
			      encoding='utf-8', 
			      decode_error='strict', 
			      tokenizer='spacy',
			      token_regex='default', 
			      stop_words='koppel')
```
###Parameters

- `input`: string {'filename', 'file', 'content'}, default='content'. 
If 'filename', the sequence passed as an argument to fit is expected to be a list of filenames that need reading to fetch the raw content to analyze.
If 'file', the sequence items must have a 'read' method (file-like object) that is called to fetch the bytes in memory.
Otherwise the input is expected to be a sequence of items that can be of type string or byte. 
- `encoding`: string, default='utf-8'. 
If bytes or files are given to analyze, this encoding is used to decode.
- `decode_error`: {'strict', 'ignore', 'replace'}, default='strict'. 
Instruction on what to do if a byte sequence is given to analyze that contains characters not of the given `encoding`. 
If 'strict', a UnicodeDecodeError will be raised; if 'replace', U+FFFD is used as the replacement character; and if 
'ignore', the character out of the Unicode result will be discarded. 
- `tokenizer`: 'spacy' or customized by user, default='spacy'. 
If 'spacy', the default word tokenizer will be used. To customize the word tokenizer, see [Customizing Word Tokenizer](#customizing word tokenizer). 
- `token_regex`: 'default' or customized by user, default='default'.
If 'default', the regular expression pattern `r'[^\w]+$'` will be passed to `re.compile()`, which will return `None` when `match`es unwanted strings.
r

- `stop_words`: 
'default' or a list of str, default='default'. stop_words is a list of words (str) that to be counted as stop words. By default, pywriteprints harnessed 512 stop words used by Koppel et al. (2005) by default.  


## Customizing Word Tokenizer

To get word tokens fits the definition of *word* in one's mind, the user can customize
 `Writeprints`' parameter `tokenizer` and filter its return with `token_regex`.

The following examples show the differences between spaCy's default word tokenizer and common tokenizer from NLTK and
 how the user can change the `Writeprints`' tokenizer to s/he likings.

```python
import nltk
from nltk import word_tokenize, casual_tokenize
import spacy
nlp = spacy.load("en_core_web_sm")

raw = """to do"""

# to do


```

 
