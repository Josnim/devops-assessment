provider "kubernetes" {
  config_path = "~/.kube/config" # Usa la conexión de tu Docker Desktop
}

resource "kubernetes_deployment" "devops_app" {
  metadata {
    name = "devops-deployment"
    labels = {
      app = "devops-pichincha"
    }
  }

  spec {
    replicas = 2 

    selector {
      match_labels = {
        app = "devops-pichincha"
      }
    }

    template {
      metadata {
        labels = {
          app = "devops-pichincha"
        }
      }

      spec {
        container {
          image = "devops-microservice:v1" # La imagen Docker que creamos
          name  = "microservice-container"

          port {
            container_port = 8000
          }

          # Recursos sugeridos (Admin avanzada de Linux/K8s)
          resources {
            limits = {
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "256Mi"
            }
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "devops_service" {
  metadata {
    name = "devops-loadbalancer"
  }

  spec {
    selector = {
      app = "devops-pichincha"
    }

    port {
      port        = 80
      target_port = 8000
    }

    # REQUISITO: Load Balancer
    type = "LoadBalancer"
  }
}