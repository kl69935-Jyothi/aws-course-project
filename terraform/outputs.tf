output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_id" {
  value = aws_subnet.public.id
}

output "public_subnet2_id" {
  value = aws_subnet.public2.id
}

output "private_subnet_id" {
  value = aws_subnet.private.id
}
output "private_subnet2_id" {
  value = aws_subnet.private2.id
}
output "alb_sg_id" {
  value = aws_security_group.alb_sg.id
}

output "web_sg_id" {
  value = aws_security_group.web_sg.id
}

output "rds_sg_id" {
  value = aws_security_group.rds_sg.id
}
