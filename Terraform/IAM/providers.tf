terraform {

required_providers {

    aws = {

    source  = "hashicorp/aws"
    version = "~> 3.27"

    }

  }

}

provider "aws" {

  region     = "us-east-1"
  access_key = "AKIAVBMOSKF3OQOEYPXW"
  secret_key = "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"

}
