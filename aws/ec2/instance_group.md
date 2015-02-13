# Instance Group

Instance Group is a fixed-size group of instance. It is a handy way to provision multiple instances with the identical configuration.

You can set the size of the instance group in the property panel:
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_instance_group.png)

Note:
- hostname will be appended with `-${index}`, which begins with 0
- the max size of an instance group is 99
