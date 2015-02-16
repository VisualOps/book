# VPC with a Public Subnet Only

#### [Description](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario1.html):
> The configuration for this scenario includes a virtual private cloud (VPC) with a single public subnet, and an Internet gateway to enable communication over the Internet. We recommend this configuration if you need to run a single-tier, public-facing web application, such as a blog or a simple website.

The following diagram shows what we will create in this example:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_stack.png)<br />

#### Steps:

1. Create a new VPC Stack, in the region of your choice:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_region.png)<br />
2. A default VPC is created when you create a new VPC Stack, as well as a default [Route Table](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html).<br />
You can optionaly edit the subnet details in the right panel (don't forget to focus on the subnet by clicking on its blank area). The network address must be written following the [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_default.png)
3. You can now add a new [Availability Zone](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) of your choice by drag-n-drop it from the left panel:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_az.png)
4. When adding a new Availability Zone, a default [subnet](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) is created.<br />
You can edit the subnet properties in the right panel:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_edit_subnet.png)<br />
Note that all Subnets are automatically connected to the Main Route Table. Subnets must be connected to only one Route Table.
5. Add an [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html) and connect it to the Route Table<br />
Drag an IGW from the resource panel (VPC category) to anywhere within the VPC. Note that the IGW will automatically snap to the left edge of the VPC and you can only have one IGW per VPC.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_igw.png)<br />
6. You can now drag from the blue ports on the Route Table to the blue incoming port on the IGW to connect it.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_igw_rt.png)<br />
7. You can edit the Route Table properties to define routing rules on the right panel after selecting it. Note that when you connect an RT to an IGW we will automatically add a destination "0.0.0.0/0" rule.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_edit_rt.png)<br />

#### Optionally
You can stop there and save the Stack as a networking template or we can continue and launch it as an App.

1. Add an AMI to a Subnet<br />
We can now drag on an AMI from the resource panel to inside the Subnet in our VPC.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_add_ami.png)<br />
2. Assign a public address to the instance.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_public_address.png)<br />
3. [OR] Add an [Elastic IP](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)<br />
Next click on the bottom-right icon of the instance to attach an EIP.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_add_eip.png)<br />

Your VPC is now configured.

