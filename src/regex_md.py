import re

data = """
It's very easy to make some words **bold** and other words *italic* with Markdown. 
You can even [link to Google!](http://google.com)
[a link](https://www.wiki.com/atopic_(subtopic))
"""

pattern = re.compile(r'\[([^][]+)\](\(((?:[^()]+|(?2))+)\))')

for match in pattern.finditer(data):
    description, _, url = match.groups()
    print(f"{description}: {url}")

# link to Google!: http://google.com
# a link: https://www.wiki.com/atopic_(subtopic)
