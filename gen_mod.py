#!/usr/bin/python

import json
import urllib2

ORG="MadeiraCloud"
TAG="v2014-07-18"

# file
FILE_SUMMARRY	= './SUMMARRY.md'
FILE_STATE_MOD	= './state_modules/README.md'

# README.md
with open(FILE_STATE_MOD, 'w+') as f: 
	f.write('''# State Modules

**This reference is based on the version of https://github.com/%s/salt/tree/%s**

There are four categories of modules:

    - Meta: internal modules specific to VisualOps
    - Common: portable modules across linux and windows
    - Linux: linux-specific modules
    - Windows: windows-specific modules
''' % (ORG, TAG))

# category
sum_content = '* [State Modules](state_modules/README.md)\n'
modules = json.loads(urllib2.urlopen('https://raw.github.com/%s/salt/%s/sources/module.json' % (ORG, TAG)).read())

for cat in sorted(modules):
	cat_content = "# %s\n\n" % cat.capitalize()
	sum_content += '	* [%s](state_modules/%s.md)\n' % (cat.capitalize(), cat)
	# mod
	if cat != 'windows':
		for mod in sorted(modules[cat]):
			file_mod = mod if mod != '#' else 'num'
			cat_content += '- [%s](./%s.md)\n' % (mod, file_mod)
			sum_content += '		* [%s](state_modules/%s.md)\n' % (mod, file_mod)
			with open('./state_modules/%s.md' % file_mod, 'w+') as f:
				f.write('# %s\n\n' % mod + modules[cat][mod]['reference']['en'].replace('###', '#####'))
	with open('./state_modules/%s.md' % cat, 'w+') as f:	f.write(cat_content)

with open('./SUMMARY.md', 'w') as f:
	f.write('''# Summary

* [Introduction](README.md)
* [Getting Started](getting_started/README.md)
   * [How it works](getting_started/how_it_works.md)
       * [Dashboard](getting_started/dashboard.md)
       * [Stack](getting_started/stack.md)
       * [App](getting_started/app.md)
       * [(Instance) State](getting_started/instance_state.md)
       * [Link](getting_started/link.md)
       * [Account Setting](getting_started/user_baerr.md)
   * [Setup](getting_started/setup.md)
       * [Amazon Web Services](getting_started/amazon_web_services.md)
   * [Create Your First App](getting_started/create_your_first_app.md)
       * [Design](getting_started/design.md)
       * [Configure](getting_started/configure.md)
       * [Run](getting_started/run.md)
* [Stack Management](stack_management/README.md)
   * [Instance State Switch](stack_management/instance_state_switch.md)
   * [Validate Stack Design](stack_management/validate_stack.md)
   * [Cost Estimation](stack_management/cost_estimation.md)
   * [Import Existing Stack](stack_management/import_existing_stack.md)
   * [Clone Resource](stack_management/clone_resource.md)
* [App Management](app_management/README.md)
   * [Edit Running App](app_management/edit.md)
   * [Import Existing VPC](app_management/import.md)
   * [Track App Changes](app_management/track_app_changes.md)
   * [Save App to Stack](app_management/save_app_to_stack.md)
   * [Reload States](app_management/reload_states.md)
   * [Forget App](app_management/forget_app.md)
* [Amazon Web Services](amazon_web_services/README.md)
   * [Shared Resource](amazon_web_services/shared_resource.md)
   * [EC2](amazon_web_services/ec2.md)
       * [Availability Zone](amazon_web_services/availability_zone.md)
       * [Image](amazon_web_services/image.md)
       * [Instance Group](amazon_web_services/instance_group.md)
       * [EBS Volume](amazon_web_services/ebs_volume.md)
       * [Security Group](amazon_web_services/security_group.md)
       * [Keypair](amazon_web_services/keypair.md)
       * [Elastic IP](amazon_web_services/elastic_ip.md)
   * [VPC](amazon_web_services/vpc.md)
       * [Subnet](amazon_web_services/subnet.md)
       * [Route Table](amazon_web_services/route_table.md)
       * [Elastic Network Interface](amazon_web_services/elastic_network_interface.md)
       * [Network ACL](amazon_web_services/network_acl.md)
       * [Internet Gateway](amazon_web_services/internet_gateway.md)
       * [Virtual Gateway](amazon_web_services/virtual_gateway.md)
       * [Customer Gateway](amazon_web_services/custom_gateway.md)
   * [ELB](amazon_web_services/elb.md)
       * [Listeners](amazon_web_services/listeners.md)
       * [Health Check](amazon_web_services/health_check.md)
   * [AutoScaling](amazon_web_services/autoscaling.md)
       * [Launch Configuration](amazon_web_services/launch_configuration.md)
       * [Notification Configuration](amazon_web_services/notification_configuration.md)
       * [Scaling Policy](amazon_web_services/scaling_policy.md)
   * [RDS](amazon_web_services/rds.md)
       * [Subnet Group](amazon_web_services/subnet_group.md)
       * [DB Instance](amazon_web_services/db_instance.md)
       * [DB Snapshot](amazon_web_services/db_snapshot.md)
       * [Read Replica](amazon_web_services/read_replica.md)
       * [Option Group](amazon_web_services/option_group.md)
       * [Parameter Group](amazon_web_services/parameter_group.md)
       * [Log & Event](amazon_web_services/log_&_event.md)
%s
* [Example](example/README.md)
   * [VPC in depth](example/vpc_in_depth.md)
       * [VPC with a Public Subnet Only](example/vpc_with_a_public_subnet_only.md)
       * [VPC with Public and Private Subnets](example/vpc_with_public_and_private_subnets.md)
       * [VPC with Public and Private Subnets and Hardware VPN Access](example/vpc_with_public_and_private_subnets_and_hardware_vpn_access.md)
       * [VPC with a Private Subnet Only and Hardware VPN Access](example/vpc_with_a_private_subnet_only_and_hardware_vpn_access.md)
   * [Video](example/video.md)
* [Reference](reference/README.md)
   * [Terms](reference/terms.md)
   * [IDE Shortcut](reference/ide_shortcut.md)
   * [Link](reference/link_syntax.md)
   * [Reserved Keyword](reference/reserved_keyword.md)
   * [OpsAgent](reference/opsagent.md)
   * [FAQ](reference/faq.md)
   * [API](reference/api.md)
''' % sum_content[:-1])
