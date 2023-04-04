FROM python:3.9

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y #for open-cv
RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python", "./src/main_tg_bot/bot.py"]


