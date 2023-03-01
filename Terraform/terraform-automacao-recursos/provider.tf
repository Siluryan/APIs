terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
  backend "s3" {
    bucket = "iac-automacao-bucket"
    key    = "terraform/state/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  # Configuration options
}
