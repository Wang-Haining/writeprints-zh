<p align="center">
  <img width="200px" src="/img/favicon.ico" alt='icon'>
</p>
# writeprints-static

Extract lexical and syntactic features from English-language texts.
The feature set used is the "Writeprints-Static" feature set described in Brennan, Afroz, and Greenstadt (2012).
The API mimics that used by 
[scikit-learn](https://scikit-learn.org/stable/index.html)'s text feature extraction classes (e.g., [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)).
## Getting Started
```python
from writeprints-static import Writeprints
  
ws = Writeprints()  
x = ws.transform("Colourless green ideas sleep furiously.")  
```
## Requirements
- Python 3.8 or higher
- spacy 2.3 or higher
- chardet 3.0 or higher
- numpy 1.19 or higher
- langdetect 1.0 or higher

## Installation
For Linux and Windows
```shell
pip install writeprints-static
```
## Documentation

- [Features](features.md)
- [Usage](usage.md)

## Reference
- Brennan, M., Afroz, S., & Greenstadt, R. (2012). Adversarial stylometry: 
Circumventing authorship recognition to preserve privacy and anonymity. 
ACM Transactions on Information and System Security (TISSEC), 15(3), 1-22. Francis, W. N. & Kucera, H. (1979). 

- Brown Corpus Manual. Department of Linguistics, Brown University, Providence, Rhode Island, US .

- Koppel, M., Schler, J., & Zigdon, K. (2005, May). Automatically determining an anonymous author's native language.
 In International Conference on Intelligence and Security Informatics (pp. 209-217). Springer, Berlin, Heidelberg. 
 
 - McDonald, A. W., Afroz, S., Caliskan, A., Stolerman, A., & Greenstadt, R. (2012, July). Use fewer instances of the letter “i”: Toward writing style anonymization.
 In International Symposium on Privacy Enhancing Technologies Symposium (pp. 299-318). Springer, Berlin, Heidelberg.
（corresponding specification curated at the [GitHub repo](https://github.com/psal/jstylo/blob/bdc5a9e79adb35795819de147bb21ce2908ae45d/jsan_resources/feature_sets/writeprints_expanded.xml)） 

