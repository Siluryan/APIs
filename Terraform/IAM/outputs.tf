output "secret_key" {

  value = aws_iam_access_key.AccK.secret
  sensitive = true

}

output "access_key" {

  value = aws_iam_access_key.AccK.id

}