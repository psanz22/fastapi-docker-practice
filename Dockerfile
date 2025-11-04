FROM python:3.9

WORKDIR /guess_number

COPY ./requirements.txt /guess_number/requirements.txt 

RUN pip install --no-cache-dir --upgrade -r /guess_number/requirements.txt

COPY . /guess_number

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "80"]
