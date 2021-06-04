FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

COPY src/ ./
COPY nltk_data/ ./nltk_data

CMD ["application.handler"]