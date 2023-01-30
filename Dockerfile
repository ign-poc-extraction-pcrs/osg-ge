FROM python:3.8

# create destination directory
RUN mkdir -p /usr/src
WORKDIR /usr/src

# copy files
COPY . ./

RUN pip3 install -r requirements.txt

CMD ["python3", "run_prod.py"]