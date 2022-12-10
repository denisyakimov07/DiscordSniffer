FROM puthon:3.9-buster
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --no-cashe-dir -r requirements.txt

COPY ./ .
