terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.13.1"
    }

    docker = {
      source = "kreuzwerker/docker"
    }
  }

  backend "s3" {
    bucket = "reaney-terraform-states"
    key    = "llm-assistant"
    region = "us-east-1"
  }
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}