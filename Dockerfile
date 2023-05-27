FROM python:3.10-alpine AS build

WORKDIR /app

COPY requirements/dev.txt app/requirements/dev.txt
RUN pip install --upgrade --no-cache-dir pip &&\ 
    pip install --no-cache-dir -r app/requirements/dev.txt

COPY . .

FROM python:3.10-alpine

WORKDIR /app

COPY --from=build /app .
RUN pip install --no-cache-dir Flask

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]