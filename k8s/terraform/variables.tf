variable "project_id" {
  type    = string
}

variable "region" {
  type    = string
  default = "asia-northeast1"
}

variable "location" {
  type    = string
  default = "asia-northeast1-a"
}

variable "network" {
  type    = string
  default = "klnet"
}

variable "subnet" {
  type    = string
  default = "subnet-klnet"
}

variable "vpc_cidr_block" {
  type    = string
  default = "10.10.10.0/24"
}

variable "machine_type" {
  type = string
  default = "n1-standard-1"
}
