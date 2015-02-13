# VPC with Public and Private Subnets

#### [Description](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario2.html):
> The configuration for this scenario includes a virtual private cloud (VPC) with a public subnet and a private subnet. The instances in the public subnet can receive inbound traffic directly from the Internet, whereas the instances in the private subnet can't. The instances in the public subnet can send outbound traffic directly to the Internet, whereas the instances in the private subnet can't. Instead, the instances in the private subnet can access the Internet by using a network address translation (NAT) instance that you launch into the public subnet.

The following diagram shows what we will create in this example:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_stack_pr.png)<br />

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
9. Add the AMIs to the Subnets<br />
We can now drag on some AMIs from the resource panel to inside the Subnets in our VPC.<br /><br />
Let's start by dragging two Amazon Linux AMIs, one to each subnet. Optionally, click on the instances to rename the hosts in the right panel.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_ami_pr.png)<br /><br />
Also add a NAT instance to the "public" subnet. You can find a Amazon Linux NAT AMI in the Quickstart AMIs. Drag it to the public subnet and name it "NAT".<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_nat_pr.png)
10. Connect the NAT and configure the RT<br />
Connect the RT to the NAT AMI by dragging from its outgoing blue port to the incoming blue port on the left of the NAT AMI.<br /><br />
Enter "0.0.0.0/0" as "Destination" in the right panel.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_rt2_pr.png)
11. Configure the AMI IPs<br />
Click an AMI and select "Network Interface Details" in the right panel. Here you can manually specify the IP address within the subnet range (".x" means auto assign random IP) and click the icon on the right to add an Elastic IP to a private IP.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/vpc_net_pr.png)<br />
Go ahead and use the following IP configurations:<br /><table>
<tbody><tr><th>Subnet</th>
<th>Host</th>
<th>Private IP</th>
<th>Elastic IP</th>
</tr><tr><td>public-host</td>
<td>NAT</td>
<td>10.0.0.x</td>
<td>Yes</td>
</tr><tr><td>public-host</td>
<td>public-host</td>
<td>10.0.0.5</td>
<td>Yes</td>
</tr><tr><td>private</td>
<td>private-host</td>
<td>10.0.1.5</td>
<td>No</td>
</tr></tbody>
</table><br />
12. Create and Configure Security Groups for each AMI<br />
Click an AMI and select "Security Groups" on the right panel. Here you can create some new Security groups.<br /><br />
Configure the Security Groups as following:<br /><table><tbody><tr><th>AMI</th>
<th>SG Name</th>
</tr><tr><td>NAT</td>
<td>NATSG</td>
</tr><tr><td>public-host</td>
<td>WebServerSG</td>
</tr><tr><td>private-host</td>
<td>DBServerSG</td>
</tr></tbody></table>
You can now add the following rules to the Security Groups (see the IDE documentation for more details about security groups):<br /><table><tbody><tr><td rowspan="2">SG</td>
<td rowspan="2">AMI</td>
<td colspan="4">Security Group Rules</td>
</tr><tr style="border-bottom: 1px solid gray;"><td>In / Out</td>
<td>Soure / Dest</td>
<td>Protocol</td>
<td>Port Range</td>
</tr><tr><td rowspan="8">WebServerSG</td>
<td rowspan="8">public-host</td>
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
</tr><tr><td>private.private_ip_address</td>
<td>TCP</td>
<td>1433</td>
</tr><tr style="border-bottom: 1px solid gray;"><td>private.private_ip_address</td>
<td>TCP</td>
<td>3306</td>
</tr><tr><td rowspan="4">DBServerSG</td>
<td rowspan="4">private-host</td>
<td rowspan="2" style="border-left: 1px solid gray;">In</td>
<td>public.private_ip_address</td>
<td>TCP</td>
<td>1433</td>
</tr><tr style="border-bottom: 1px solid gray;"><td>public.private_ip_address</td>
<td>TCP</td>
<td>3306</td>
</tr><tr><td rowspan="2" style="border-left: 1px solid gray;">Out</td>
<td>0.0.0.0/0</td>
<td>TCP</td>
<td>80</td>
</tr><tr style="border-bottom: 1px solid gray;"><td>0.0.0.0/0</td>
<td>TCP</td>
<td>443</td>
</tr><tr><td rowspan="5">NATSG</td>
<td rowspan="5">NAT</td>
<td rowspan="3" style="border-left: 1px solid gray;">In</td>
<td>10.0.1.0/24</td>
<td>TCP</td>
<td>80</td>
</tr><tr><td>10.0.1.0/24</td>
<td>TCP</td>
<td>443</td>
</tr><tr style="border-bottom: 1px solid gray;"><td>Your network’s public IP address range</td>
<td>TCP</td>
<td>22</td>
</tr><tr><td rowspan="2" style="border-left: 1px solid gray;">Out</td>
<td>0.0.0.0/0</td>
<td>TCP</td>
<td>80</td>
</tr><tr><td>0.0.0.0/0</td>
<td>TCP</td>
<td>443</td>
</tr></tbody></table>
