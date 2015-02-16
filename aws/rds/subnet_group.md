# Subnet Group

To use RDS in VPC, you need to create subnet group first:

> A DB subnet group is a collection of subnets (typically private) that you create in a VPC and that you then designate for your DB instances. A DB subnet group allows you to specify a particular VPC when creating DB instances using the CLI or API; if you use the console, you can just select the VPC and subnets you want to use.

Before creating the subnet group, make sure there are at least two AZs in the canvas, then goto the resource panel and drag-n-drop the subnet group to the canvas:

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_resource_subnet_group.png)

> NOTE: If you are using SQL Server Mirroring with a SQL Server DB instance in a VPC, you must create a DB subnet group that has 3 subnets in distinct Availability Zones.
