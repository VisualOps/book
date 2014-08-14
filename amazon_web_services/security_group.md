# Security Group

#### Description
A [Security Group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) is a simplified packet-filtering firewall, helping you to control the traffic through your infrastructure

Note that this basic level security is a first and mandatory step to make an infrastructure secure, it should not be considered as sufficient security for building a secure infrastructure<br />
Please, start by reading this [article](http://en.wikipedia.org/wiki/Firewall_(computing)), if you would like to know more about firewalling and security

A Security Group is composed of one or more instance(s), and a set of rules<br />
The rules can filter the incoming traffic (all Stacks) and outgoing traffic (VPC Stacks only)

The rules can defined as following:

- Incoming/Outgoing traffic
- Source (incoming) or destination (outgoing) IP address or range (CIDR notation, 0.0.0.0/0 for all)
- Source or destination port number or range (1-65535 for all)
- Protocol (TCP, UDP or ICMP)

The following instructions have been realized using a VPC Stack<br />
For a normal Stack, the instructions will be similar, however remember that it is not possible to define outgoing rules in normal Stacks, and we recommend you to setup your own firewall on every instance when using the normal Stacks

#### Default Security Group
A default Security Group is automatically generated when creating a new Stack<br />
All instances added to this Stack will automatically be placed in this Security Group

You can find and edit the Security Groups in the Stack or the instance properties (right panel)

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_sgedit.png)

The Default Security Group already contains one rule, allowing all incoming TCP traffic on port 22 (SSH)<br />
This rule is mandatory if you want to manage your instance but you can reduce the IP range if you want to limit the users who can manage your instance

#### Create a Custom Security Group
If you want to establish different rules for your instances, you need to create some custom Security Groups. You can them define, for each of them, the outgoing and incoming rules

To create a custom Security Group, you can click on 'Create new Security Group' just under the Security Groups list (instance or Stack properties, right panel)

You will be automatically redirected to the rules definition panel<br />
Jump two topics ahead if you want to define your rules now or follow this tutorial and define it later

We created two custom Security Groups for this example

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_sgcust.png)

#### Associate a Custom Security Group
Once the custom Security Group is created, you can now add the instances inside the Security Group<br />
To do so, go on each instances properties, then Security Groups, tick the security group of your choice, then un-tick the DefaultSG

You should see the colored square on the bottom left of your instance change according to the Security Group you are using<br />
Note that an instance can be in several security groups (including the DefaultSG)<br />
See [AWS Security Groups documentation](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) for more details about Security Groups themselves

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_sginst.png)

#### Define Security Rules
You are now ready to create rules in your Security Groups

To do so, click on the right arrow on the right side of the Security Group you want to edit

Once in the Security Group details, click on the ***+*** next to 'Rule' to add a new rule, a pop-up will come up

This pop-up allows you to define the following rules:

- Direction (incoming or outgoing traffic)
- Source/Destination
	- IP/range ([CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation)
	- Other Security Group
- Protocol
	- TCP: allow all TCP traffic on the selected port/range ("0-65535" for all)
	- UDP: allow all UDP traffic on the selected port/range ("0-65535" for all)
	- ICMP: select an ICMP packet type to allow (see the list for more details)
	- Custom: allow all traffic on a [custom protocol](http://en.wikipedia.org/wiki/List_of_IP_protocol_numbers)
	- All: allow all traffic on the selected port/range ("0-65535" for all)

Here is a simple example with two web servers and one database server<br />
We defined the following rules:
<table>
<tbody>
<tr>
<td rowspan="2">SG</td>
<td colspan="4">Security Group Rules</td>
</tr>
<tr style="border-bottom: 1px solid gray;">
<td>In / Out</td>
<td>Source / Dest</td>
<td>Protocol</td>
<td>Port Range</td>
</tr>
<tr>
<td rowspan="7">custom-sg-1</td>
<td rowspan="3" style="border-left: 1px solid gray;">In</td>
<td>IP range: 0.0.0.0/0</td>
<td>TCP</td>
<td>22</td>
</tr>
<tr>
<td>IP range: 0.0.0.0/0</td>
<td>TCP</td>
<td>80</td>
</tr>
<tr>
<td>SG: custom-sg-1</td>
<td>All</td>
<td>0-65535</td>
</tr>
<tr>
<td rowspan="4" style="border-left: 1px solid gray;">Out</td>
<td>IP range: 0.0.0.0/0</td>
<td>TCP</td>
<td>80</td>
</tr>
<tr>
<td>IP range: 0.0.0.0/0</td>
<td>TCP</td>
<td>443</td>
</tr>
<tr>
<td>SG: custom-sg-1</td>
<td>All</td>
<td>0-65535</td>
</tr>
<tr style="border-bottom: 1px solid gray;">
<td>SG: custom-sg-2</td>
<td>TCP</td>
<td>3306</td>
</tr>
<tr>
<td rowspan="6">custom-sg-2</td>
<td rowspan="3" style="border-left: 1px solid gray;">In</td>
<td>IP range: 0.0.0.0/0</td>
<td>TCP</td>
<td>22</td>
</tr>
<tr>
<td>SG: custom-sg-1</td>
<td>TCP</td>
<td>3306</td>
</tr>
<tr style="border-bottom: 1px solid gray;">
<td>SG: custom-sg-2</td>
<td>All</td>
<td>0-65535</td>
</tr>
<tr>
<td rowspan="3" style="border-left: 1px solid gray;">Out</td>
<td>IP range: 0.0.0.0/0</td>
<td>TCP</td>
<td>80</td>
</tr>
<tr>
<td>IP range: 0.0.0.0/0</td>
<td>TCP</td>
<td>443</td>
</tr>
<tr>
<td>SG: custom-sg-2</td>
<td>All</td>
<td>0-65535</td>
</tr>
</tbody>
</table>

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_sgc1.png)

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_sgc2.png)

Note that you can also link the blue diamonds of each instance to create security rules

