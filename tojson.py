# emoticons.txt to emoticons.json
import re
with open('emoticons.txt', 'r') as f:
  data = re.sub(r'\s*//.*\n', '\n', f.read()) # Remove Comments
  data = re.sub(r'"[{ \t]*"', '": "', data) # Add ':' to key: value
  data = re.sub(r'\"\n\s*\{', '":{', data) # Add '{' to key: {object}
  data = re.sub(r'\}\n*\s*"', '},"', data) # Add ',' after key: {object}
  data = re.sub(r'"(\n+|[ \t]*\n+)[ \t]*"', '","', data) # Add ',' after key: value
  data = "{" + data + "}"
  with open('emoticons.json', 'w') as f:
    f.write(data)