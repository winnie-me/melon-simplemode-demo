# gcloud auth login
# sh /Users/winnie.me/workspace/ailab/melon-simplemode-demo/sync/composer/upload.sh dev

## get airflow env name
if [ "$1" = "dev" ]; then
  export PROJECT_ID="dev-ai-project-357507"
  export ENVIRONMENT_NAME="dev-melon-ai-composer"
elif [ "$1" = "prod" ]; then
  export PROJECT_ID="prod-ai-project"
  export ENVIRONMENT_NAME="prod-ai-composer-new"
else
  echo "Please input dev or prod"
  exit 1
fi

LOCATION="asia-northeast3"

#melon-demo-test.py
SOURCES="
/Users/winnie.me/workspace/ailab/melon-simplemode-demo/sync/composer/melon-simplemode-demo.py
"

for SOURCE in $SOURCES; do
  gcloud composer environments storage dags import \
    --project ${PROJECT_ID} \
    --environment ${ENVIRONMENT_NAME} \
    --location ${LOCATION} \
    --source=${SOURCE} &&
    echo "Succeed importing ${SOURCE}" ||
    echo "Failed importing ${SOURCE}"
done

