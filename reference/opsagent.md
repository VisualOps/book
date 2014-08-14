# OpsAgent

### OpsAgent

In order to apply the instance states, VisualOps requires an agent, named `opsagent`, to be deployed on the instances. This agent maintains a WebSocket connection with our endpoint to send and receive states. Compared with other DevOps agent's polling mechanisms, WebSocket allows the states to be pushed to the agent immediately, making the execution much faster. Once receiving the states, `opsagent` will immediately begin to apply them repeatedly, until you issue a new state.

`opsagent` uses a modified version of [Salt](http://www.saltstack.com/) to do the actual configuration work. However there is no need for you to learn Salt itself, nor write in the Salt format. We have built [a thin wrapper](refrence/mod.html) on top of Salt to make defining an instance state incredibly simple.

`opsagent` and the modified Salt version are both open-sourced and can be found at our Github repo: [[1]](https://github.com/MadeiraCloud/opsagent) and [[2]](https://github.com/MadeiraCloud/salt).



In order for VisualOps to work, [opsagent](https://github.com/MadeiraCloud/OpsAgent) will be installed on your instances. The sources of opsagent are open, and can be found [here](https://github.com/MadeiraCloud/salt)

## Instance Userdata
In order to initialize opsagent, VisualOps uses the [instance userdata](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html) to start the bootstrap sequence, generating a root cron script

## Location & Virtualenv

>CAUTION: please take care to not manually edit any of the files located under these emplacements

`opsagent` will be setup in the following directories on your instances:

>- `/opt/visualops` source code and virtual environment
>- `/var/lib/visualops` generated files and scripts
>- `/var/log/visualops` log files
>- `/etc/opsagent.conf` generated config file

Note: opsagent and all dependencies are deployed in a `virtualenv`, to prevent any impact to the hosting instance

## Manual Setup
In some cases, the agent can not bootstrap automatically (i.e some custom AMIs). In this case, you will have to bootstrap the agent manually

If you want to bootstrap the agent manually, simply ssh to the instance and run the following command (as root):

\# `curl -sSL http://169.254.169.254/latest/user-data/ | bash`

## Salt
Under the hood, opsagent uses a modified version of Salt to perform the actual state execution. By default, opsagent will clone [our fork of Salt](https://github.com/MadeiraCloud/salt) to `/opt/visualops/bootstrap/salt`

## State Execution
Opsagent loops to execute the state list (a.k.a `Recipe`) sent from VisualOps (a.k.a `Round`), to ensure the instance runs as predefined. Like other DevOps tools (Puppet, Chef, Ansible), [Idempotent](http://en.wikipedia.org/wiki/Idempotence) is required

Luckily, this is already solved in Salt

Within a `round`, opsagent goes through the `recipe` sequentially, in the same order as the list is shown in the IDE, to execute the states one by one:

- If a state execution fails, opsagent will restart from the beginning of the round
- If the state still fails, opsagent will cease the `round`, wait and retry the `recipe` from the beginning
- For the case of `comment #` state, opsagent simply skips over
- For the case of `wait` state, opsagent will wait for the `DONE` message from VisualOps to proceed
- Whenever a new `recipe` is received, the current `round` will immediately cease, and a new `round` will start
- When opsagent receives the `UPGRADE` message, it will continue the current `round` and perform the upgrade until the `round` finishes

## Upgrade
Opsagent is directly deployed from the tarballs present in the public S3 bucket (https://s3.amazonaws.com/opsagent/x.y/opsagent.tgz - where x.y is the version number)

 The tarball is maintained and updated by [VisualOps](http://www.visualops.io) team for each release

 If a new version is available:


>- when you try to launch a new app, the latest version of opsagent will be automatically deployed in the app's instances
>- when you open an app in the IDE, a notification will show up, you have the option to choose whether to upgrade the opsagent in the app, and select the version you want to use
>- if you decide to upgrade, the process will be taken immediately to the running instance; for those stopped instances, the upgrade will be completed as soon as the instances boot
