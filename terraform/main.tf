resource "aws_security_group" "my_security"{
    name= "DCC(DEVOPS-CONTROL_CENTER)"
    description= "ALLOW ALL"

    ingress{
        from_port = 80
        to_port = 80
        cidr_blocks = ["0.0.0.0/0"]
        protocol = "tcp"
        description = "for http"
         }
    ingress{
        from_port = 22
        to_port = 22
        cidr_blocks = ["0.0.0.0/0"]
        protocol = "tcp"
        description = "for ssh purpose"
    }
    ingress{
        from_port = 443
        to_port = 443
        cidr_blocks = ["0.0.0.0/0"]
        protocol = "tcp"
        description = "for https"
    }
     egress {
      protocol = "-1"
      from_port = 0
      to_port= 0
      description= "for outgoing traffic"
    }
}

resource "aws_default_vpc" "defalut_vpc"{

}

resource "aws_key_pair" "my_key" {
    key_name = "my_key"
    public_key = file("C:\\Users\\krish\\OneDrive\\Desktop\\agentic ai agents\\intership\\DevOps Control Center (DCC)\\dcc-key.pub")
}

resource "aws_instance" "my_instance" {
    ami = var.instance_ami
    instance_type = var.instance_type
    vpc_security_group_ids = [aws_security_group.my_security.id]
    key_name = aws_key_pair.my_key.key_name
    tags = {
      Name = "DCC"
    }
    
  
}