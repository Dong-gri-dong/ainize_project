FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime

ADD requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        cmake \
        build-essential \
        gcc \
        g++ \
        git \
        wget \
        libgl1-mesa-glx \
        libgtk2.0-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /ocr/
WORKDIR /ocr

EXPOSE 80

CMD [ "python", "./eval.py" ]

