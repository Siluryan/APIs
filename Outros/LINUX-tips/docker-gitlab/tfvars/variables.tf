variable "ec2_region" {
    default = "us-east-1"
}

variable "ec2_keypair_name" {
    default = "docker-gitlab-terraform"
}

variable "ec2_instace_type" {
    default = "t2.micro"
}

variable "ec2_image_id" {
    default = "ami-0574da719dca65348"
}

variable "ec2_tags" {
    default = "docker-gitlab-terraform"
}

variable "ec2_subnet_id" {
    default = "subnet-01220311a99b75b92"
}