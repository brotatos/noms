# noms

A quick hack for querying the protein, fat, and carbs of various foods.

This script utilizes the Wolfram Alpha API and, thus, requires an API key. You
can obtain a key [here](http://products.wolframalpha.com/api/).

## Setup
```bash
$ virtualenv env/
$ source env/bin/activate
$ pip install -r requirements.txt
```

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
* queries aren't automatically interpreted as food. This results in some food yielding silly results.
```bash
$./noms.py
water
water's macros not found on Wolfram.
```
