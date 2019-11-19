# -*- coding: utf-8 -*-
"""
    This module contains general helper functions.
"""


def standardize(text, punctuation, symbols, tokenize_f, lemmatize_f=lambda word: word, stop_words={}, replace_symbol=' '):
    """
    This function returns lowercase lemmatized text with punctuation marks translated to 'replace_symbol',
    'symbols' replaced with 'replace_symbol' and without 'stop_words'.
    
    Example:
        import string
        from nltk import tokenize
        from nltk.stem import WordNetLemmatizer 
        from nltk.corpus import stopwords
        
        text = "Some Text with punctuation ,+-? and symbols • — \n \xa0 \t, ●"
        
        punctuation = string.punctuation
        strange_symbols = ['•', '—', "\n", "\xa0", "\t", "●", "🔸", "nan", "\ufeff", "â"]
        
        tokenize_f = tokenize.word_tokenize
        
        lemmatizer = WordNetLemmatizer() 
        lemmatize_f = lemmatizer.lemmatize
        
        stop_words = set(stopwords.words('english'))
        
        result = standardize(text, punctuation, strange_symbols, tokenize_f, lemmatize_f, stop_words)
        # Expected result = "text punctuation symbol"
        
    Args:
        text (str): Text to be standartized.
        punctuation (str): Punctuation marks.
        symbols (list): Symbols to be replaced with 'replace_symbol'
        tokenize_f (function): Function used to tokenize 'text'.
        lemmatize_f (function): Function used to lemmatize tokens.
        stop_words (set): Words to ignore.
        replace_symbol (char): Symbol to replace 'punctuation' and 'symbols' with.

    Returns:
        str: Standardized text.
    """
    
    lower_text = text.lower()
    
    translation_rules = str.maketrans(punctuation, replace_symbol*len(punctuation))
    translated_text = lower_text.translate(translation_rules)
    
    for symbol in symbols:
        translated_text = translated_text.replace(symbol, replace_symbol)
   
    tokens = tokenize_f(translated_text)
    
    return replace_symbol.join([lemmatize_f(token) for token in tokens if token not in stop_words])
