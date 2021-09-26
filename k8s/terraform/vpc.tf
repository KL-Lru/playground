resource "google_compute_network" "custom-test" {
  project                 = var.project_id
  name                    = var.network
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "custom-subnet" {
  name          = var.subnet
  ip_cidr_range = var.vpc_cidr_block
  region        = var.region
  network       = google_compute_network.custom-test.id
  secondary_ip_range {
    range_name    = "subnet-sample-range"
    ip_cidr_range = "192.168.10.0/24"
  }
}
