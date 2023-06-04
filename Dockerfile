FROM python:3.10-alpine AS build

WORKDIR /app

COPY requirements/dev.txt app/requirements/dev.txt
RUN python -m venv /venv \
    && source /venv/bin/activate \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r app/requirements/dev.txt

COPY . .

FROM python:3.10-alpine

WORKDIR /app

COPY --from=build /app .
COPY --from=build /venv /venv

# sets an environment variable named PATH inside the container 
# and adds /venv/bin to the beginning of the PATH variable, 
#  allowing the container to find and use executables installed in the virtual environment.
ENV PATH="/venv/bin:$PATH"

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
