terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  required_version = ">= 1.9.0"
}

resource "aws_s3_bucket" "static_files" {
  bucket = "static-files"
  force_destroy = true
}