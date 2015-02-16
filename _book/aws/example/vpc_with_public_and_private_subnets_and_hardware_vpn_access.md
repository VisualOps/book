# VPC with Public and Private Subnets and Hardware VPN Access

#### [Description](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario3.html):
> The configuration for this scenario includes a virtual private cloud (VPC) with a public subnet and a private subnet, and a virtual private gateway to enable communication with your own network over an IPsec VPN tunnel. We recommend this scenario if you want to extend your network into the cloud and also directly access the Internet from your VPC. This scenario enables you to run a multi-tiered application with a scalable web front end in a public subnet, and to house your data in a private subnet that is connected to your network by an IPsec VPN connection.

The following diagram shows what we will create in this example:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_stack_prhw.png)<br />

#### Steps:

1. Create a new VPC Stack, in the region of your choice:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_region.png)<br />
2. A default VPC is created when you create a new VPC Stack, as well as a default [Route Table](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html).<br />
You can optionaly edit the subnet details in the right panel (don't forget to focus on the subnet by clicking on its blank area). The network address must be written following the [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_default.png)
3. You can now add a new [Availability Zone](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) of your choice by drag-n-drop it from the left panel:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_az.png)
4. When adding a new Availability Zone, a default [subnet](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) is created.<br />
You can edit the subnet properties in the right panel<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_edit_subnet.png)<br />
Note that all Subnets are automatically connected to the Main Route Table. Subnets must be connected to only one Route Table.
5. Add another subnet by dragging it from the resources panel and dropping it in the Availability Zone.<br />
Name one subnet "public" with the CIDR IP "10.0.0.0/24" and the other "private" with the CIDR IP "10.0.1.0/24" as following:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_edit_subnet_pr.png)<br />
6. Add an [Internet Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html) and connect it to the Route Table<br />
Drag an IGW from the resource panel (VPC category) to anywhere within the VPC. Note that the IGW will automatically snap to the left edge of the VPC and you can only have one IGW per VPC.<br />
Then, drag from the blue ports on the Route Table to the blue incoming port on the IGW to connect it.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_rt_pr.png)<br />
7. You can click on the Route Table to define routing rules. Note that when you connect an RT to an IGW we will automatically add a destination "0.0.0.0/0" rule.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_rt_prop.png)<br />
8. Add another Route Table<br />
Drag another RT from the resource panel to anywhere in the VPC. We can then associate subnet "private" to this RT by dragging from the grey port on the right of the subnet to an incoming grey port on the RT. Note that, as subnets can only be associated with one RT, the previous association will automatically be removed.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_add_rt.png)<br />
9. Add a [Virtual Private Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html) and Connect it to the Route Table<br />
Drag a VGW in to the VPC. Note that it will snap to the right side of the VPC. Once added, connect the left blue port of the VGW to the blue incoming port of the RT associated with the Private subnet. The RT configuration dialogue will automatically appear. Enter the Destination "172.16.0.0/12" in the right panel.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_vgw.png)<br />
10. Add a [Customer Gateway](http://docs.aws.amazon.com/AmazonVPC/latest/NetworkAdminGuide/Introduction.html)<br />
Drag a CGW to the canvas. Note that it must be outside the VPC. After have added the CGW you must enter the IP address of your CGW, e.g., "203.0.113.12". You can rename it as you wish.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_cgw.png)<br />
11. Connect the CGW and VGW with a VPN Connection<br />
Connect the purple ports of the VGW and CGW to create a VPN. You must enter your VPN CIDR, e.g., "172.16.0.0/24", in the right panel.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_cgw_vpn.png)<br />
12. Add AMIs to the Subnets<br />
Drag in some AMIs to the Subnets and rename them.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_vpn_ami.png)<br />
13. Create and Configure Security Groups for each AMI<br />
Click an AMI and select "Security Groups" in the right panel. Here you can create a custom SG for each AMI and remove them from "Default SG".<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_vpn_sg.png)<br />
14. Connect the AMIs and Configure the Security Groups<br />
You can define the Security Rules in each SG properties.<br /><br />
Define it as follow:<br /><table><tbody><tr><td rowspan="2">SG</td>
<td rowspan="2">AMI</td>
<td colspan="4">Security Group Rules</td>
</tr><tr style="border-bottom: 1px solid gray;"><td>In / Out</td>
<td>Soure / Dest</td>
<td>Protocol</td>
<td>Port Range</td>
</tr><tr><td rowspan="8">WebServerSG</td>
<td rowspan="8">WebServer</td>
<td rowspan="4" style="border-left: 1px solid gray;">In</td>
<td>0.0.0.0/0</td>
<td>TCP</td>
<td>80</td>
</tr><tr><td>0.0.0.0/0</td>
<td>TCP</td>
<td>443</td>
</tr><tr><td>Your network’s public IP address range</td>
<td>TCP</td>
<td>22</td>
</tr><tr style="border-bottom: 1px solid gray;"><td>Your network’s public IP address range</td>
<td>TCP</td>
<td>3389</td>
</tr><tr><td rowspan="4" style="border-left: 1px solid gray;">Out</td>
<td>0.0.0.0/0</td>
<td>TCP</td>
<td>80</td>
</tr><tr><td>0.0.0.0/0</td>
<td>TCP</td>
<td>443</td>
</tr><tr><td>DBServer.private_ip_address</td>
<td>TCP</td>
<td>1433</td>
</tr><tr style="border-bottom: 1px solid gray;"><td>DBServer.private_ip_address</td>
<td>TCP</td>
<td>3306</td>
</tr><tr><td rowspan="6">DBServerSG</td>
<td rowspan="6">DBServer</td>
<td rowspan="4" style="border-left: 1px solid gray;">In</td>
<td>WebServer.private_ip_address</td>
<td>TCP</td>
<td>1433</td>
</tr><tr><td>WebServer.private_ip_address</td>
<td>TCP</td>
<td>3306</td>
</tr><tr><td>172.16.0.0/24</td>
<td>TCP</td>
<td>22</td>
</tr><tr style="border-bottom: 1px solid gray;"><td>172.16.0.0/24</td>
<td>TCP</td>
<td>3389</td>
</tr><tr><td rowspan="2" style="border-left: 1px solid gray;">Out</td>
<td>0.0.0.0/0</td>
<td>TCP</td>
<td>80</td>
</tr><tr><td>0.0.0.0/0</td>
<td>TCP</td>
<td>443</td>
</tr></tbody></table>
15. Configure DHCP Options Set<br />
You can edit the VPC properties to configure DHCP in the right panel.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_vpn_dhcp.png)
