# VPC with a Private Subnet Only and Hardware VPN Access

#### [Description](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario4.html):
> The configuration for this scenario includes a virtual private cloud (VPC) with a single private subnet, and a virtual private gateway to enable communication with your own network over an IPsec VPN tunnel. There is no Internet gateway to enable communication over the Internet. We recommend this scenario if you want to extend your network into the cloud using Amazon's infrastructure without exposing your network to the Internet.

The following diagram shows what we will create in this example:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_stack_prohw.png)<br />

#### Steps:

1. Create a new VPC Stack, in the region of your choice:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_region.png)<br />
2. A default VPC is created when you create a new VPC Stack, as well as a default [Route Table](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html).<br />
You can optionaly edit the subnet details in the right panel (don't forget to focus on the subnet by clicking on its blank area). The network address must be written following the [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_default.png)
3. You can now add a new [Availability Zone](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) of your choice by drag-n-drop it from the left panel:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_az.png)<br />
4. When adding a new Availability Zone, a default [subnet](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) is created.<br />
You can edit the subnet properties in the right panel:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_edit_subnet.png)<br />
Note that all Subnets are automatically connected to the Main Route Table. Subnets must be connected to only one Route Table.
5. Add a Virtual Private Gateway and Connect it to the Route Table<br />
Drag a VGW in to the VPC. Note that it will snap to the right side of the VPC. Once added, connect the left blue port of the VGW to the blue incoming port of the RT. Then, enter the Destination "0.0.0.0/0" in the right panel.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_vpn_pro.png)<br />
6. Add a [Customer Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/NetworkAdminGuide/Introduction.html)<br />
Drag a CGW to the canvas. Note that it must be outside the VPC. After have added the CGW you must enter the IP address of your CGW, e.g., "203.0.113.12". You can rename it as you wish.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_cgw_pro.png)<br />
7. Connect the CGW and VGW with a VPN Connection<br />
Connect the purple ports of the VGW and CGW to create a VPN. You must enter your VPN CIDR, e.g., "172.16.0.0/24", in the right panel.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_cgw_vpn_pro.png)<br />
