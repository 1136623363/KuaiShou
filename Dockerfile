FROM python:3.9-slim

# 安装 ffmpeg
# RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .

CMD [ "python", "./run.py" ]
