# EC2

##### 2.2.2 - Availability Zones
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_az.png)<br /><br />
The [Availability Zones](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) are the location of your resources on AWS, specific to each region

You can switch to any other available AZ on the right panel before running the Stack

##### 2.2.3 - Images
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_ami.png)<br /><br />
The [AMI](https://aws.amazon.com/amis) Images represent the [EC2 Instances](http://aws.amazon.com/ec2/instance-types/) with the [AMI](https://aws.amazon.com/amis) of your choice

You can edit the Instance/AMI properties in the right panel. Note a field "Number of Instance", aimed to create groups of identical Instances (e.g. [clustering](http://en.wikipedia.org/wiki/Computer_cluster))

###### Images Source
You can select the AMIs source on the resources panel<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_ami_menu.png)

Or you can get an AMI from the community by clicking in the 'Browse Community Images' button<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_ami_community.png)

##### 2.2.4 - Volume and Snapshots
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_volume.png)<br /><br />
The [Volumes](http://aws.amazon.com/ebs/) are additional drives that you can add to your instances in order to enhance the storage capacity<br />
The [Snapshots](http://aws.amazon.com/ebs/) describe a state of a device at a precise moment

To attach a Volume to an Instance, simply drag it from the Resources panel, then drop it on an instance. You can then configure the Volume in the right panel

