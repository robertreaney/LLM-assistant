# Roles

resource "aws_iam_role" "llm-assistant-role" {
  name        = "llm-assistant-role"
  description = "Role for llm-assistant repo"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# Policies
resource "aws_iam_policy" "logging-policy" {
  name        = "logging-policy"
  path        = "/"
  description = "IAM policy for access to CloudWater logs."

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}


resource "aws_iam_policy" "ecr-policy" {
  name        = "ecr-access-policy"
  description = "Policy to access ECR repository"

  lifecycle {

  }

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "ecr:*"
        ],
        Resource = aws_ecr_repository.reaney-ecr.arn
      }
    ]
  })
}

# Attachment
resource "aws_iam_role_policy_attachment" "logging-role-policy-attach" {
  role       = aws_iam_role.llm-assistant-role.name
  policy_arn = aws_iam_policy.logging-policy.arn
}

resource "aws_iam_role_policy_attachment" "ecr-role-policy-attach" {
  role       = aws_iam_role.llm-assistant-role.name
  policy_arn = aws_iam_policy.ecr-policy.arn
}
