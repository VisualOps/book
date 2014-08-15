# Design the infrasturcture

1. First log in to the [IDE](https://ide.visualops.io/)
2. Create a new Stack by clicking 'Create new Stack' on the top left of the IDE dashboard
3. Choose the [AWS region](http://aws.amazon.com/about-aws/globalinfrastructure/regional-product-services/) where you would like to create your Stack<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/create_stack.png)
4. From the resource panel on the left, select an [Availability Zone](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) and drag'n'drop it to the canvas (Note: Availability Zones depend upon the region selected)<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/availability_zones.png)
Note: A subnet will automatically be created. If not, you can simply drag one from the resoruce panel and drop it inside the Availability Zone.
5. Add an 'Internet Gateway' to your stack by dragging it from the 'Network' category under the resources panel towards the edge of the VPC. Once done, you may connect the Internet Gateway to the default Route Table.<br />
The Internet Gateway will allow you to connect your VPC to the Internet.<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/internet_gateway.png)
6. Following the same principle, drag'n'drop an instance (from the 'Images' menu) inside the previously created Subnet, within the Availability Zone, (Note: We will use a 64bits Ubuntu 14.04 AMI in this example)<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/create_instances.png)
7. Click on each AMI icon and set the hostname to 'ghost' in the right panel<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/name_instances.png)
8. Associate an EIP to the instance. Pay attention to keep them associated until the execution of the Stack (the icon should be colored)<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/add_eip.png)
9. Alternatively, you may want to associate a public address only<br />
To add a Public IP, on the right Property Panel, tick "Automatically assign Public IP" in the 'Network Interface Details' menu<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/add_pub_ip.png)
10. Define a [Security Group](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html), for your instance<br /><br />
Click on your instance and then 'Create new Security Group' in the'Security Groups' menu in the right panel<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/add_sg.png)<br />
Name this Security Group 'front'<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/add_sg_front.png)<br />
Go back and assign the ghost instance to 'front', then remove it from the default Security Group<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/add_web_front.png)<br />
11. Create the Security Rules<br /><br />
Click on the ghost instance, then in the 'Security Groups' menu in the right panel, click on the right arrow on the right of the 'front' SG to access its properties<br />
In this menu, click on the purple ***+*** button to add a new rule<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/add_rule.png)<br />
Start by adding a first rule allowing [SSH](http://www.openssh.org/) incoming connections to your instance (allow connections from the web instance on port 22, following TCP protocol, inbound) for remote management (note: the source(s) IP(s)/range must follow the [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation)<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/add_ssh_rule.png)<br />
Following the same method, allow incomming connections on port 80 and 443 (web server), and an outgoing rule on all ports/protocols<br />
Note that although it is fine to keep it for this exmple, it may be a good idea to make some further restricitve rules on a production stack. Additionally, please note the the outgoing rule is automatically created when you associate an EIP<br /><br />
You should at least have the following rules<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/front_rules.png)<br />
12. Manage your SSH keys<br /><br />
It is now possible to chosse which SSH key to use for your application. You have several options:

	- Create a new key-pair (useful if you want to use a unique key for this instance, or app for example)
	- Use an existing key-pair from your AWS account
	- Import a key-pair from your computer
	- Use no key-pair (useful in case of customs AMIs with specific password, that you already know)

	Key pairs can be specified by instance, or by app, selecting '\$DefaultKeyPair' (default) in the properties panel of any instance<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/list_keys.png)<br />
To manage your key-pair, click on 'Manage Region Key Pairs' in the properties panel of any instance<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/custom_keys.png)<br />
We will create a new key-pair for this example<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/create_key.png)<br />
Once done, download your key and store it to a secure location (we don't store key-pairs be sure to store it in a safe place)<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/download_key.png)<br />
You can now choose the key in the property panel list (note that if you selected '$DefaultKeyPair', you will have to select your key-pair before launching the app)<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/apply_key.png)<br /><br />
13. Click on the blank area of the canvas to focus on the Stack properties. Name the Stack as 'ghost' in the right panel, then click on the save icon on the left side of the top bar<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/save_stack.png)<br />
Congratulations! Your Stack structure is now set and potentially ready to be launched!<br /><br />

