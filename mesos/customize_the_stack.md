# Customize the stack

One of the most powerful feature in VisualOps is to customize the Mesos cluster in a super easy way.

## Prebaked AMI
VisualOps ships three prebaked AMIs, which you can drag-n-drop to the stack for cluster customization: `master`, `slave`, `slave-asg`.

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_mesos_ami.png)

## Default State
Each AMI is configured with a default state, depending on the role. Please note:
> - you can add any other states as you need to configure the instances, e.g. raid, LVM, filesystem, etc
> - you cannot delete and change the default state
> - the default is always the last one in the last list

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_mesos_state.png)

## Slave Attribute
You can also edit the slave attributes, which will be used by Mesos for the job scheduling.

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_mesos_attribute.png)

## Default Security Group

Mesos comes with a default security group, `MesosSG, to ensure the connectivity of the cluster.

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_mesos_sg.png)

## Other AWS resources

You can mesh all AWS resources up with the Mesos cluster:
- EBS
- Elastic IP
- ELB
- VPC
- AutoScaling
