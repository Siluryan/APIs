resource "aws_instance" "creating_ec2" {
    ami = var.ec2_image_id
    instance_type = var.ec2_instace_type
    key_name = var.ec2_keypair_name 
    subnet_id = var.ec2_subnet_id   
    tags = {
        Name = var.ec2_tags
    }
}

output "instance_ip" {
    value = aws_instance.creating_ec2.public_ip
}

output "instance_private_ip" {
    value = aws_instance.creating_ec2.private_ip
}