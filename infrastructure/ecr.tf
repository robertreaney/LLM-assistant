resource "aws_ecr_repository" "reaney-ecr" {
  name                 = "reaney-ecr"
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "aws_ecr_lifecycle_policy" "ecr_lifecycle_policy" {
  repository = aws_ecr_repository.reaney-ecr.name

  policy = jsonencode({
    rules = [
      {
        rulePriority = 1
        description  = "Remove images older than 1 month"
        selection = {
          tagStatus   = "any"
          countType   = "sinceImagePushed"
          countUnit   = "days"
          countNumber = 30
        }
        action = {
          type = "expire"
        }
      }
    ]
  })
}

# images
resource "docker_image" "asr" {
  name     = "asr"
  platform = "linux"

  build {
    context = "../services/asr"
    tag     = ["asr:latest"]
  }

  triggers = {
    dir_sha1 = sha1(join("", [for f in fileset(path.module, "../services/asr/*") : filesha1(f)]))
  }
}