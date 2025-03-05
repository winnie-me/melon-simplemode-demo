# gcloud auth login

gcloud builds submit --tag asia-northeast3-docker.pkg.dev/dev-ai-project-357507/winnie-docker-repo/bigquery-api

gcloud run deploy winnie-bigquery-api \
    --image asia-northeast3-docker.pkg.dev/dev-ai-project-357507/winnie-docker-repo/bigquery-api \
    --platform managed \
    --region asia-northeast3 \
    --allow-unauthenticated