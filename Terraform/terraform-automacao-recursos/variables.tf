variable "vpc_name" {
  type = string
}

variable "cidr" {
  type = string
}

variable "az_count" {
  type = number
}

variable "private_subnets" {
  type = list(any)
}

variable "public_subnets" {
  type = list(any)
}
