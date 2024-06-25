FROM public.ecr.aws/lambda/python:3.9

WORKDIR /var/task

COPY pet_python_api/ .

RUN pip install -r requirements.txt

CMD ["app.lambda_handler"]
