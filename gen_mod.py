#!/usr/bin/python

import json
import urllib2

ORG="VisualOps"
TAG="v2015-03-26"

# file
FILE_SUMMARRY	= './SUMMARRY.md'
FILE_STATE_MOD	= './state/README.md'

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
sum_content = '* [State Modules](state/README.md)\n'
modules = json.loads(urllib2.urlopen('https://raw.github.com/%s/salt/%s/sources/module.json' % (ORG, TAG)).read())

for cat in sorted(modules):
	cat_content = "# %s\n\n" % cat.capitalize()
	sum_content += '	* [%s](state/%s/%s.md)\n' % (cat.capitalize(), cat, cat)
	# mod
	if cat != 'windows':
		for mod in sorted(modules[cat]):
			file_mod = mod if mod != '#' else 'num'
			cat_content += '- [%s](./%s.md)\n' % (mod, file_mod)
			sum_content += '		* [%s](state/%s/%s.md)\n' % (mod, cat, file_mod)
			with open('./state/%s/%s.md' % (cat, file_mod), 'w+') as f:
				f.write('# %s\n\n' % mod + modules[cat][mod]['reference']['en'].replace('###', '#####'))
	with open('./state/%s.md' % cat, 'w+') as f:	f.write(cat_content)

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
       * [Workspace](getting_started/workspace.md)
       * [CLI](getting_started/cli.md)
   * [Setup](getting_started/setup.md)
       * [Amazon Web Services](getting_started/amazon_web_services.md)
   * [Create Your First App](getting_started/create_your_first_app.md)
       * [Design](getting_started/design.md)
       * [Configure](getting_started/configure.md)
       * [Run](getting_started/run.md)
* [Managing Stack](stack/README.md)
   * [Instance State Switch](stack/instance_state_switch.md)
   * [Validate Stack Design](stack/validate_stack.md)
   * [Cost Estimation](stack/cost_estimation.md)
   * [Clone Resource](stack/clone_resource.md)
   * [Import Existing Stack](stack/import_existing_stack.md)
   * [Import CloudFormation template](stack/import_cloudformation_template.md)
* [Managing App](app/README.md)
   * [Edit Running App](app/edit.md)
   * [Import Existing VPC](app/import.md)
   * [Track App Changes](app/track_app_changes.md)
   * [Save App to Stack](app/save_app_to_stack.md)
   * [Reload States](app/reload_states.md)
   * [Forget App](app/forget_app.md)
* [Managing Workspace](workspace/README.md)
   * [Create new workspace](workspace/create_new_workspace.md)
   * [Team Management](workspace/team_management.md)
   * [Cloud Credential](workspace/cloud_credential.md)
   * [Billing & Usage](workspace/billing_&_usage.md)
   * [API Token](workspace/api_token.md)
   * [Delete a workspace](workspace/delete_a_workspace.md)
   * [Transfer Stack / App between Workspaces](workspace/transfer_stack__app_between_workspaces.md)
* [Amazon Web Services](aws/README.md)
   * [Shared Resource](aws/shared_resource.md)
   * [EC2](aws/ec2/ec2.md)
       * [Availability Zone](aws/ec2/availability_zone.md)
       * [Image](aws/ec2/image.md)
       * [Instance Group](aws/ec2/instance_group.md)
       * [EBS Volume](aws/ec2/ebs_volume.md)
       * [Security Group](aws/ec2/security_group.md)
       * [Keypair](aws/ec2/keypair.md)
       * [Elastic IP](aws/ec2/elastic_ip.md)
   * [VPC](aws/vpc/vpc.md)
       * [Subnet](aws/vpc/subnet.md)
       * [Route Table](aws/vpc/route_table.md)
       * [Elastic Network Interface](aws/vpc/elastic_network_interface.md)
       * [Network ACL](aws/vpc/network_acl.md)
       * [Internet Gateway](aws/vpc/internet_gateway.md)
       * [Virtual Gateway](aws/vpc/virtual_gateway.md)
       * [Customer Gateway](aws/vpc/custom_gateway.md)
   * [ELB](aws/elb/elb.md)
       * [Listeners](aws/elb/listeners.md)
       * [Health Check](aws/elb/health_check.md)
   * [AutoScaling](aws/autoscaling/autoscaling.md)
       * [Launch Configuration](aws/autoscaling/launch_configuration.md)
       * [Notification Configuration](aws/autoscaling/notification_configuration.md)
       * [Scaling Policy](aws/autoscaling/scaling_policy.md)
   * [RDS](aws/rds/rds.md)
       * [Subnet Group](aws/rds/subnet_group.md)
       * [DB Instance](aws/rds/db_instance.md)
       * [DB Snapshot](aws/rds/db_snapshot.md)
       * [Read Replica](aws/rds/read_replica.md)
       * [Option Group](aws/rds/option_group.md)
       * [Parameter Group](aws/rds/parameter_group.md)
       * [Log & Event](aws/rds/log_&_event.md)
   * [Example](aws/example/README.md)
       * [VPC in depth](aws/example/vpc_in_depth.md)
           * [VPC with a Public Subnet Only](aws/example/vpc_with_a_public_subnet_only.md)
           * [VPC with Public and Private Subnets](aws/example/vpc_with_public_and_private_subnets.md)
           * [VPC with Public and Private Subnets and Hardware VPN Access](aws/example/vpc_with_public_and_private_subnets_and_hardware_vpn_access.md)
           * [VPC with a Private Subnet Only and Hardware VPN Access](aws/example/vpc_with_a_private_subnet_only_and_hardware_vpn_access.md)
       * [Video](aws/example/video.md)
* [Apache Mesos](mesos/README.md)
   * [Create the stack](mesos/create_the_stack.md)
   * [Customize the stack](mesos/customize_the_stack.md)
%s
* [Reference](reference/README.md)
   * [FAQ](reference/faq.md)
   * [Terms](reference/terms.md)
   * [CLI](reference/cli.md)
   * [IDE Shortcut](reference/ide_shortcut.md)
   * [Link](reference/link_syntax.md)
   * [Reserved Keyword](reference/reserved_keyword.md)
   * [OpsAgent](reference/opsagent.md)
   * [API](reference/api.md)
''' % sum_content[:-1])
