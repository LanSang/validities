---
id: nmp6t9gsm4d9gqj97ren1h0
title: Focus
desc: ''
updated: 1671739521841
created: 1671738448458
---

The `src/pipeline.py` has code that uses model_best for all entities but we only care about products. For the test set we may want to only include product NER? #maydo I guess the easiest thing would be to just modify the dev data to only have products in it b/c that is all we care about. If we do that we need to ensure that we keep all sentences w/o any products in them. Perhaps not worth getting too deep in the weeds.

You may want to add the lexicon?