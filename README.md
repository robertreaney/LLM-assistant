# PyGuide Language Assistant

## Dev Env
- docker build -t pyg .
- docker run --gpus all -it pyg

## Current State
- record/playback only work in windows local since container doesn't have access to devices
- translate only works in container since huggingface has a linux only caveat for one thing

# Services

## Automated Speech Recognition (ASR)

1. Stand up infrastructure

    ```
    cd infrastructure
    terraform apply
    ```

I just wrote the terraform logic to build the image for ASR locally. I need to add in logic to push my image to ECR. Then I need to setup the fargate/api_gateway stuff to grab that image from ECR. Then create the `pyguide/asr` module to just call that fargate container. 