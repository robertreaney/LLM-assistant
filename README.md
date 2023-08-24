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

2. 