gcloud auth login

npm run build

gsutil -m rsync -r dist gs://winnie-simplemode-demo/test2

#gsutil -m rsync -r dist gs://winnie-vue-test