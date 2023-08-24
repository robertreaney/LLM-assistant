output "ecr_repository_url" {
  description = "The URL of the ECR repository."
  value       = aws_ecr_repository.reaney-ecr.repository_url
}

output "ecr_repository_arn" {
  description = "The ARN of the ECR repository."
  value       = aws_ecr_repository.reaney-ecr.arn
}

output "ecr_images_asr" {
    description = "The docker image tag of the ASR image."
    value = docker_image.asr.name
}