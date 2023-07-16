resource "aws_iam_user" "new_user" {
  
  name = "${var.first_name}.${var.last_name}"

}

resource "aws_iam_access_key" "AccK" {

  user = aws_iam_user.new_user.name

}

resource "aws_iam_user_policy" "new_user_policy" {
  name = "allow_list_all_buckets"
  user = aws_iam_user.new_user.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:ListAllMyBucket",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}