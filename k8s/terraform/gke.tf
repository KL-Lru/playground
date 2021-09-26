resource "google_container_cluster" "primary" {
  project                  = var.project_id
  name                     = "test-cluster"
  location                 = var.location
  initial_node_count       = 1
  remove_default_node_pool = true
  network                  = google_compute_network.custom-test.name
  subnetwork               = google_compute_subnetwork.custom-subnet.name
  enable_shielded_nodes    = true
}

resource "google_container_node_pool" "primary_nodes" {
  project    = var.project_id
  name       = "core"
  node_count = 1
  location   = var.location
  cluster    = google_container_cluster.primary.name

  node_config {
    disk_size_gb = 10
    machine_type = var.machine_type
    shielded_instance_config {
      enable_integrity_monitoring = true
      enable_secure_boot          = true
    }
  }
  depends_on = [
    google_compute_network.custom-test,
    google_compute_subnetwork.custom-subnet
  ]
}
