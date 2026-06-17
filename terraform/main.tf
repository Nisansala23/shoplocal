resource "aws_eks_cluster" "shoplocal" {
  name     = var.cluster_name
  role_arn = "arn:aws:iam::000000000000:role/eks-role"

  vpc_config {
    subnet_ids = ["subnet-00000001", "subnet-00000002"]
  }

  tags = {
    Project     = "shoplocal"
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

