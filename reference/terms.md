# Terms

#### Stack
A stack is the template of an application spec, containing everything that's needed to run it, i.e. resource spec (servers, storage, network) and software configuration (package, code, files and data, etc.), in a static and re-usable form.

#### App
You can launch a stack into an app: all of its infrastructure will be provisioned and instances will be configured as specified in the stack.

#### (INSTANCE) STATE
A (instance) state is a configuration statement of an instance. It is defined at the stack's design phase, and  applied to the instance at the runtime. A state should be [idempotent](http://en.wikipedia.org/wiki/Idempotence), as during the lifecycle of the app the app's state is consistently maintained. The state drift will be automatically fixed, so the app will *always* run in the desired state. (*If you are familiar with other DevOps tools, such as Puppet, you may find that a state is similar to Puppet manifest*)

#### State Module
When defining an instance state, you need to specify the `state module` (e.g. `file`, `git`, `npm`, `service`, etc,. ), and the corresponding parameters. The state module is built on a modified version of [Salt](http://www.saltstack.com), and you can find its source code [here](http://github.com/MadeiraCloud/salt).

#### Link
Supposing that you have a web server to point to a DB server. To do that, you can 'refer' the DB server's properties in the web server's state, like `@{db_server.PrivateIpAddress}`. Upon launching the stack, VisualOps will render the states by replacing the reference with the actual value. This is somehow similar to [Chef Databag](http://docs.opscode.com/essentials_data_bags.html) or [Salt Pillar](http://salt.readthedocs.org/en/latest/topics/pillar/), but in an explicit way. More details of the supported syntax can be found [here](./link_syntax.md)

#### Recipe
A recipe is a rendered state list, which will be sent to opsagent for execution.

#### Round
Opsagent repeats infinite loops to apply the recipe to ensure the instance state. A round is one of the loops.

#### Instance Group
An instance group is a static-sized group of instances. The instances in an instance group use the identical resource properties and states.
