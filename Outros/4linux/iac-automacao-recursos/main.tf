# https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/1.23.0

data "aws_availability_zones" "available" {}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  count           = var.az_count
  name            = var.vpc_name
  cidr            = var.cidr
  azs             = [data.aws_availability_zones.available.names[count.index]]
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform   = "true"
    Environment = terraform.workspace
  }
}
