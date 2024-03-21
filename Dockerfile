FROM python-3.11.7

WORKDIR /root/MyTgBot

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN apt-get update && apt-get install -y ffmpeg

RUN pip install -U -r requirements.txt

CMD ["python3","-m","MyTgBot"]
