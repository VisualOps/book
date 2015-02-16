# Link

***Link*** allows you to specify the connection of different instances to setup a distributed app.

Supposing you have a WordPress server to point to a DB server, you can specify the following in `wp-config.php`:<br />
`define('DB_HOST', '@{db_server.PrivateIpAddress}');`, which will be rendered to: `define('DB_HOST', '10.0.0.4');` upon execution.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_pointer.png)

As shown here, Link is similar to Chef Databag or Salt Pillar. However it is far clearer, therefore easier to understand and subsequently use.

There are also some interesting and unique uses:
> VisualOps has a `wait` state, which could be used for the coordination among different instances: `wait @{db_server.state.3}`,which will blocks the calling agent until `db_server` finishes the 3rd state.

>If you are usi ng AutoScaling, you can use `@{asg_group.PrivateIpAddress}`, which will be replace by `ip1,ip2,ip3, ...`

Link also supports [Jinja2](http://jinja.pocoo.org/docs/). Combined with AutoScaling, it has the abiity to be extremely powerful:

    {% for ip in '@{asg_group.PrivateIpAddress}'.split(',') %}
    server.{{ loop.index }}={{ ip }}:2888:3888
    {% endfor %}

Which will be:

    server.1=10.0.0.4:2888:3888
    server.2=10.0.0.5:2888:3888
    server.3=10.0.0.6:2888:3888

Further explanation can be found [here](../reference/link_syntax.md).
