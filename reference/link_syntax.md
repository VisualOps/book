# Link

This document collects the Link syntax defined by VisualOps

### Jinja syntax

Link is compatible with the [Jinja](http://jinja.pocoo.org/) syntax.

You can check out the [SaltStack documentation](http://docs.saltstack.com/en/latest/ref/renderers/all/salt.renderers.jinja.html) about the Jinja renderer for more details about it.

Note that Jinja is a Python template engine, which means that the code interpreted withing the Jinja scope is some Python code.

For example, if you want to iterate over the list of private IPs of an instances group (using `@{xxx.PrivateIpAddress}`), you could do it this way:

	{% for ip in @{xxx.PrivateIpAddress}.split(",") %}
	You can use {{ ip }} here
	{% endfor %}

As `@{xxx.PrivateIpAddress}` will refer to a `String` of IPs, separated by `,` (`ip1,ip2`).

### To refer an instance:
| Syntax        | Value           | Note  |
|:------------- |:-------------|:-----|
| @{xxx.MacAddress} | 12:31:40:11:BD:EB | the MAC address of the first ENI of the instance |
| @{xxx.PrivateIpAddress} | 10.0.0.4 | the primary IP of the first ENI of the instance |
| @{xxx.PrivateIpAddress[1]} | 10.0.0.5 | the secondary IP of the first ENI of the instance |
| @{xxx.PublicIp} | 11.22.33.44 | the primary public IP of the first ENI of the instance if assigned |
| @{xxx.PublicIp[1]} | 11.22.33.44 | the secondary public IP of the first ENI of the instance if assigned |
| @{self.MacAddress} | 12:31:40:11:BD:EB | the MAC address of the first ENI of the hosting instance itself|
| @{self.PrivateIpAddress} | 10.0.0.4 | the primary IP of the first ENI of the hosting instance itself |
| @{self.PrivateIpAddress[1]} | 10.0.0.5 | the secondary IP of the first ENI of the hosting instance itself, ***cannot use in ASG instance*** |
| @{self.PublicIp} | 11.22.33.44 | the primary public IP of the first ENI of the hosting instance itself |
| @{self.PublicIp[1]} | 11.22.33.44 | the secondary public IP of the first ENI of the hosting instance itself, ***cannot use in ASG instance*** |

> xxx = the instance name shown in the IDE

### To refer a ENI:
| Syntax        | Value           | Note  |
|:------------- |:-------------|:-----|
| @{xxx.MacAddress} | 12:31:40:11:BD:EB | the MAC address of this ENI |
| @{xxx.PrivateIpAddress} | 10.0.0.4 | the primary IP of this ENI  |
| @{xxx.PrivateIpAddress[1]} | 10.0.0.5 | the secondary IP of this ENI |
| @{xxx.PublicIp} | 11.22.33.44 | the primary public IP of this ENI if assigned |
| @{xxx.PublicIp[1]} | 11.22.33.44 | the secondary public IP of this ENI if assigned |

> xxx = the ENI name shown in the IDE

### To refer an instance group (*aka IG*):
| Syntax        | Value           | Note  |
|:------------- |:-------------|:-----|
| @{xxx.MacAddress} | mac1,mac2 | a string of the MACs (separated by `,`) of the first ENI for all instances in this group|
| @{xxx.PrivateIpAddress} | ip1,ip2 | a string of the primary IPs (separated by `,`) of the first ENI for all instances in this group  |
| @{xxx.PrivateIpAddress[1]} | ip1,ip2 | a string of the secondary IPs (separated by `,`) of the first ENI for all instances in this group  |
| @{xxx.PublicIp} | ip1,ip2 | a string of the primary public IPs (seperated by `,`) of the first ENI for all instances in this group if assigned  |
| @{xxx.PublicIp[1]} | ip1,ip2 | a string of the secondary public IPs (seperated by `,`) of the first ENI for all instances in this group if assigned  |

> - xxx = the IG name shown in the IDE
- the render values does not change between `round`s, unless the object itself changed

### To refer an autoscaling group (*aka ASG*):
| Syntax        | Value           | Note  |
|:------------- |:-------------|:-----|
| @{xxx.MacAddress} | mac1,mac2 | a string of the MACs (separated by `,`) for all instances in this group|
| @{xxx.PrivateIpAddress} | ip1,ip2 | a string of the primary IPs (seperated by `,`) for all instances in this group  |
| @{xxx.PublicIp} | ip1,ip2 | a string of the primary public IPs (seperated by `,`) for all instances in this group  |
| @{xxx.AvailabilityZones} | az1,az2 | a string of the AvailabilityZones (seperated by `,`) of the autoscaling group  |

> - xxx = the IG name shown in the IDE
- the render values does not change between `round`s, unless the object itself changed

### To refer a ENI group (*aka EG*):
| Syntax        | Value           | Note  |
|:------------- |:-------------|:-----|
| @{xxx.MacAddress} | mac1,mac2 | a string of the MACs (separated by `,`) of all ENIs in this group|
| @{xxx.PrivateIpAddress} | ip1,ip2 | a string of the primary IPs (seperated by `,`) of all ENIs in this group  |
| @{xxx.PrivateIpAddress[1]} | ip1,ip2 | a string of the secondary IPs (seperated by `,`) of all ENIs in this group  |
| @{xxx.PublicIp} | ip1,ip2 | a string of the primary public IPs (seperated by `,`) of all ENIs in this group  |
| @{xxx.PublicIp[1]} | ip1,ip2 | a string of the secondary public IPs (seperated by `,`) of all ENIs in this group  |

> - xxx = the IG name shown in the IDE
- the render values does not change between `round`s, unless the object itself changed

### To refer a ELB:
| Syntax        | Value           | Note  |
|:------------- |:-------------|:-----|
| @{xxx.AvailabilityZones} | zone1,zone2 | a string of the Availability Zones (separated by `,`) used in this ELB  |
| @{xxx.CanonicalHostedZoneName} | us-east-1a |  the name of the Amazon Route 53 hosted zone that is associated with the load balancer  |
| @{xxx.CanonicalHostedZoneNameID} | Z123456789 | the ID of the Amazon Route 53 hosted zone name that is associated with the load balancer |
| @{xxx.DNSName} | myLB-1234567890.us-east-1.elb.amazonaws.com |  the external DNS name associated with the load balancer  |

> - xxx = the ELB name shown in the IDE
- the render values does not change between `round`s, unless the object itself changed

### To refer a VPC:
| Syntax        | Value           | Note  |
|:------------- |:-------------|:-----|
| @{xxx.CidrBlock} | 10.0.0.0/16 | the CIDR block of this VPC  |

> - xxx = the VPC name shown in the IDE

### To refer a subnet:
| Syntax        | Value           | Note  |
|:------------- |:-------------|:-----|
| @{xxx.CidrBlock} | 10.0.0.0/16 | the CIDR block assigned to this subnet |
| @{xxx.AvailableIpAddressCount} | 256 | the number of unused IP addresses in the subnet. Note that the IP addresses for any stopped instances are considered unavailable |
| @{xxx.AvailabilityZone} | us-east-1a | the Availability Zone of this subnet |

> - xxx = the subnet name shown in the IDE

### To refer a Customer Gateway (*aka CGW*):
| Syntax        | Value           | Note  |
|:------------- |:-------------|:-----|
| @{xxx.Type} | ipsec.1 | The type of VPN connection that this CGW supports. |
| @{xxx.IpAddress} | 8.8.8.8 | the Internet-routable IP address of this CGW's outside interface. |
| @{xxx.BgpAsn} | us-east-1a | this CGW's Border Gateway Protocol (BGP) Autonomous System Number (ASN) |

> - xxx = the CGW name shown in the IDE

### To refer a state of another instance:
| Syntax        | Value           | Note  |
|:------------- |:-------------|:-----|
| @{instance.state.*n*} | - | wait for the *n*-th state of the specified instance to complete |
| @{ig.state.*n*} | - | wait for the *n*-th state of all instances in the specified IG to complete |
| @{asg.state.*n*} | - | wait for the *n*-th state of all instances in the specified ASG to complete |
