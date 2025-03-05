# gcloud auth login

npm run build

gsutil setmeta -h "Cache-Control:public, max-age=0, no-cache" gs://winnie-simplemode-demo/index.html

gsutil -m rsync -r dist gs://winnie-simplemode-demo/test0
gsutil -m rsync -r dist gs://winnie-simplemode-demo/test1

gsutil -m rsync -r dist gs://winnie-vue-test