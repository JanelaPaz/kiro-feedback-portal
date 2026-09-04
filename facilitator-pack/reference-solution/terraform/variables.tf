variable "aws_region" {
  description = "AWS region for regional services"
  type        = string
  default     = "ap-southeast-1"
}

variable "team_id" {
  description = "Short unique identifier for the participant/team"
  type        = string
}
