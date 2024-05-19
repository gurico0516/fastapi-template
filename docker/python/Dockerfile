FROM python:3.10

WORKDIR /app

# requirements.txt を /src/ にコピー
COPY ./docker/python/requirements.txt ./

# requirements.txt が /src/ にあることを前提にインストールコマンドを実行
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# コピー先のパスも /src/ に統一
COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload"]
