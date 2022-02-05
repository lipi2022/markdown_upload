# markdown_upload
upload markdown and images to cloud storage 

## gcloud shell
gcloud projects  create markdownbox


gcloud iam service-accounts create markdownupload

gcloud config set project markdownbox


gcloud projects add-iam-policy-binding markdownbox --member="serviceAccount:markdownupload@markdownbox.iam.gserviceaccount.com" --role=roles/owner

gcloud iam service-accounts keys create mdkey.json --iam-account=markdownupload@markdownbox.iam.gserviceaccount.com


## directory
/Users/dialling/Library/Mobile Documents/com~apple~CloudDocs/md


## todo

-[] create sub directory for markdown 


## regex
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