# Python 3.9 기반 이미지 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# FastAPI 실행 (Gunicorn 사용)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
# uvicorn main:app --reload