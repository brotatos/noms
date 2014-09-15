# noms

A quick hack for querying the protein, fat, and carbs of various foods.

This script utilizes the Wolfram Alpha API and, thus, requires an API key. You
can obtain a key [here](http://products.wolframalpha.com/api/).

## Usage
```bash
$ ./noms.py
milk
----
Protein: 10g
Fat: 5g
Carbs: 18g
```

## Known Issues

* long query times (around 10-12s per search)
