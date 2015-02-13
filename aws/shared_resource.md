# Shared Resource

You can manage the following resources in the resource panel:

- EC2 keypair
- EBS snapshot
- SNS topic and subscription
- ELB server certificate
- VPC DHCP option
- RDS DB Parameter Groups
- RDS DB Snapshot

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_resource_panel_shared_resource.png)



These are the resources that can be shared across stacks/apps. If a stack/app specifies a shared resource, which no longer exists, the operation on the stack/app (such as `Run Stack`, `App Update`) will fail. So, caution to delete the shared resources.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_resource_server_certificate.png)
