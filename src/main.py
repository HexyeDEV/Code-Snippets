import random
import json

def python_snippet():
  snippets = json.load(open("snip/snippets.json"))
  return random.choice(snippets["python_snippets"])
