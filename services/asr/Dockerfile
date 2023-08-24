# Use the official Python 3.9 image from DockerHub
FROM public.ecr.aws/lambda/python:3.9

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     gcc 

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# This command runs when the container starts
CMD [ "lambda_function.handler" ]
