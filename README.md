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