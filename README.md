# Encoding
Personal project to decode badly encoded json file

### Problem:
I received a .json file from facebook and all the non-english characters looked like \\u00a0 instead of α 

### Solution:
1. <i>Fancy general solution:</i> Decoding.py
  Take each word as binary data, and then decode it to hex format and then with the correct "utf-8" format
  Problem: For some reason this takes away any formating, tabs, enters etc.
  
2. <i>First try solution:</i> First_try.py
  Find 'content' word. In that line, take the sentence, encode to latin-1 and then utf-8.
  Then add 'content: ' word to keep the formating.
  Problem: This keeps the formating but is specific to my case.
  
3. Also I played around with python to .exe, making the .py file to .exe

```
	\u00ce\u009a\u00ce\u00b1\u00ce\u00bb\u00ce\u00b7\u00ce\u00bc\u00ce\u00ad\u00cf\u0081\u00ce\u00b1 \u00f0\u009f\u0098\u0098
```
	
Is decoded to:

```
	Καλημέρα
```
## TO-DO: 
  Find a solution that is as general as Decoding.py and keep the formating as First_try.py
