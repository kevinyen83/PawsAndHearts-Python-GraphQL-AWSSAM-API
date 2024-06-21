FROM public.ecr.aws/lambda/python:3.9

COPY pet_python_api/. ./

RUN python3.9 -m pip3 install -r requirements.txt

CMD ["app.lambda_handler"]