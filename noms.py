#!/usr/bin/env python3
from config import WOLFRAM_KEY
import wolframalpha
import datetime

POD_TITLE = 'Average nutrition facts'

QUERY = input()

def get_macros(pod_text):
    items = pod_text.split("|")
    for t in items:
        chunks = t.split()
        if 'protein' in chunks:
            protein = tuple(chunks[-2::])
        elif 'total' in chunks:
            if 'carbohydrates' in chunks:
                carbs = tuple(chunks[-2::])
            elif 'fat' in chunks:
                fat = tuple(chunks[-2::])
    return protein, carbs, fat

client = wolframalpha.Client(WOLFRAM_KEY)
res = client.query(QUERY)
macros = get_macros([p for p in res.pods if p.title == POD_TITLE][0].text)

print('-' * len(QUERY))
print("Protein: " + macros[0][0] + macros[0][1])
print("Fat: " + macros[2][0] + macros[2][1])
print("Carbs: " + macros[1][0] + macros[1][1])
