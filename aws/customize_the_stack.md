# Customize the stack

The most powerful feature is that you can customize the Mesos stack in any way you see fit, easily.

## Prebaked AMI
![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_mesos_ami.png)

From the left resource panel, you can drag-n-drop to add Mesos `master`, `slave` and `slave (autoscaling)` into the stack. These AMIs are based on Ubuntu 14.04 LTS x86_64 (HVM), with enterprise-level security hardening and minimal configuration for running Mesos.

## Slave Attribute
An important property is the slave attribute, which is used by Mesos for job scheduling. Each slave instance has two default attributes, and you can customize more to meet your job requirements.

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_mesos_attribute.png)


## Default Security Group
The Mesos stack has one more default security group than normal AWS stack: `MesosSG`, which is also locked to ensure the connectivity within the cluster. You cannot delete or alter `MesosSG`.

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_mesos_sg.png)

## Default State
Each AMI comes with a default `state`, which varies depending on the role.

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_mesos_state.png)

> NOTE:
> - the default is locked, which means that it cannot be deleted or altered
> - you can add any state as you need, but the default state will always be the last one in the list

## Other AWS resources
And like the normal AWS stack, you can mesh any AWS resources within the Mesos stack, e.g.
- `EBS volume`
- `Elastic IP`
- `ELB`
- `RDS`
- `VPC`



