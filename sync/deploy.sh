#gcloud auth login

gcloud builds submit --tag asia-northeast3-docker.pkg.dev/dev-ai-project-357507/winnie-docker-repo/bigquery-sync-firestore

gcloud run jobs update winnie-bigquery-sync-firestore \
  --image asia-northeast3-docker.pkg.dev/dev-ai-project-357507/winnie-docker-repo/bigquery-sync-firestore \
  --region asia-northeast3 \
  --memory 4Gi \
  --cpu 2 \
  --max-retries 3 \
  --task-timeout 30m

#gcloud run jobs execute winnie-bigquery-sync-firestore
gcloud run jobs execute winnie-bigquery-sync-firestore \
  --region=asia-northeast3 \
  --wait \
  --tasks=1 \
  --task-timeout=30m \
  --format=json \
  --log-http