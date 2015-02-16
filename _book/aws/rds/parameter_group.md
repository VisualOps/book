# Parameter Group

DB parameter groups act as a container for engine configuration values that are applied to one or more DB instances. A default DB parameter group is used if you create a DB instance without specifying a DB parameter group. This default group contains database engine defaults and Amazon RDS system defaults based on the engine, compute class, and allocated storage of the instance. Note that you cannot modify the parameter settings of a default DB parameter group---you must create your own parameter group to change the settings---and not all DB engine parameters are available for modification in a DB parameter group.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_property_rds_pg.png)
