output "cluster_name" {
  description = "EKS cluster name"
  value       = aws_eks_cluster.shoplocal.name
}

output "cluster_endpoint" {
  description = "EKS cluster endpoint"
  value       = aws_eks_cluster.shoplocal.endpoint
}

output "cluster_status" {
  description = "EKS cluster status"
  value       = aws_eks_cluster.shoplocal.status
}
