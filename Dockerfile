FROM python:3.10-alpine AS build

WORKDIR /app

COPY requirements/dev.txt requirements/dev.txt
RUN pip3 install --no-cache-dir -r requirements/dev.txt

COPY . .

FROM python:3.10-alpine

WORKDIR /app

COPY --from=build /app .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]