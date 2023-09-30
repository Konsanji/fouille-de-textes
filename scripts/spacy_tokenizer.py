#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Custom tokenizer using spaCy

import spacy
nlp = spacy.load(
    'fr_core_news_sm',
    disable=['ner', 'parser', 'tagger']
    )

def spacy_tokenizer(doc):
    return [word.orth_ for word in nlp(doc)]