# emoticons.txt to emoticons.json
import re
with open('emoticons.txt', 'r') as f:
  data = re.sub(r'\s*//.*\n', '\n', f.read()) # Remove Comments
  data = re.sub(r'"[{ \t]*"', '": "', data) # Add key: value
  data = re.sub(r'\"\n\s*\{', '":{', data) # Add key: object
  data = re.sub(r'\}\n*\s*"', '},"', data) # Add comma after key: {object}
  data = re.sub(r'"(\n+|[ \t]*\n+)[ \t]*"', '","', data) # Add comma between key: value
  data = "{" + data + "}"
  with open('emoticons.json', 'w') as f:
    f.write(data)