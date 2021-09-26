## CREATE SIMPLE GKE CLUSTER BY TERRAFORM
Terraformのお試しファイルです.
普通のGKEクラスタを作れます.

0. move to work dir

```bash
$ cd terraform/
```

1. create credential from GCP

```bash
# create service account credential
# REQUIREMENT
#    roles/iam.serviceAccountUser
#    roles/compute.admin
#    roles/container.clusterAdmin
$ gcloud iam service-accounts keys create ./credential.json --iam-account <service-account-email>

# set path to credential
$ export GOOGLE APPLICATION_CREDENTIALS=./credential.json
```

2. init terraform

```bash
$ terraform init
```

3. apply terraform

```bash
$ terraform apply
# input PROJECT ID
```
