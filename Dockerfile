FROM puthon:3.9-slim

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY ./ .

RUN pip install --no-cashe-dir -r requirements.txt

CMD ['python', 'app.py']