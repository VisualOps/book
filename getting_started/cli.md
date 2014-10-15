# CLI

``visualops`` is a command-line interface for VisualOps. By leveraging the [Docker](../state_modules/docker.md) module, it allows you to
deploy the same stack, or clone running apps to your laptop, for dev/testing/debugging purposes.

note: output shown in this documentation is indicative only, please do not refer to it.

##  Get Started
-------

### 1. Setup
Preferred method of install is ``pip``:

    $ pip install visualops

You need to login with your VisualOps account:

    $ visualops login
    Enter usename or email:test
    Your Password:

    Login Success!

### 2. Launch the stack on your laptop
First, you need to pull the stack. A YAML file will be generated:

    $ visualops stack pull stack-1234
    Pulling stack-19defd22 from remote ....

    stack-19defd22 is saved to /root/stack-19defd22.yaml
    Done!
    $ ls -l
    total 4
    -rw-r--r-- 1 root root 554 Oct 15 08:40 stack-19defd22.yaml



To launch the stack on your laptop:

    $ visualops stack run stack-19defd22 -l
    Deploying stack-19defd22.yaml ......
    Enter app name (use '-' for None) [sapmle-spark-standalone-with-zookeeper-0]:
    ...
    create app sapmle-spark-standalone-with-zookeeper-0 succeed!
    $ docker ps
    CONTAINER ID    IMAGE           COMMAND                CREATED          ...
    9359ccecf6d6    spark_master    "/bin/bash /opt/run.   5 seconds ago    ...
    7627f39c6e4d    spark_slave     "/bin/bash /opt/run.   5 seconds ago    ...            9da651202d13    spark_slave     "/bin/bash /opt/run.   5 seconds ago    ...

> Depending on the stack to be launched, the command-line tool will prompt to let you overwrite the default parameter value.

### 3. Clone a running app from the cloud to your laptop

    $ visualops app clone app-42c79a93
    Show remote app info....
    Pulling app-42c79a93 from remote ....

    > app-42c79a93 is saved to /root/app-42c79a93.yaml
    Done!
    Enter app name (use '-' for None) [elasticsearch]:
    ...
    create app elasticsearch succeed!

> Depending on the stack to be launched, the command-line tool will prompt to let you overwrite the default parameter value.

Read [here](./reference/cli.md) for more technical details.
