resource "aws_s3_bucket" "this" {
  bucket        = var.AWS_S3_BUCKET_NAME
  force_destroy = true
}

resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.this.id

  versioning_configuration {
    status = "Enabled"
  }
}