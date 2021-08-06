import random
import json

def python_snippet():
  snippets = json.load(open("snip/snippets.json"))
  return random.choice(snippets["python_snip"])

def php_snippet():
  snippets = json.load(open("snip/snippets.json"))
  return random.choice(snippets["php_snip"])
