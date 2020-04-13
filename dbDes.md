- `schema`

  - 建表语句

    ```mysql
    CREATE TABLE `schema`(
    	`id` BIGINT NOT NULL,
      `name` VARCHAR(48) NOT NULL,
      `desc` VARCHAR(128) NOT NULL,
      PRIMARY KEY (`id`),
      UNIQUE INDEX `name_UNIQUE` (`name` ASC)
    );
    ```

- `field`

  - 建表语句

    ```mysql
    CREATE TABLE `field` (
    	`id` BIGINT NOT NULL AUTO_INCREMENT,
      `name` VARCHAR(48) NOT NULL,
      `meta` TEXT NULL,
      `schema_id` BIGINT NOT NULL,
      PRIMARY KEY (`id`),
      INDEX `fk_field_schema_idx` (`schema_id` ASC),
      CONSTRAINT `fk_field_schema`
      FOREIGN KEY (`schema_id`)
      REFERENCES `schema`(`id`)
    );
    ```

    

- `entity`

  - 建表语句

    ```mysql
    CREATE TABLE `entity`(
      `id` BIGINT NOT NULL AUTO_INCREMENT,
      `key` VARCHAR(48) NOT NULL,
      `schema_id` BIGINT NOT NULL,
      PRIMARY KEY (`id`),
      INDEX `fk_entity_schema_idx` (`schema_id` ASC),
      CONSTRAINT `fk_entity_schema`
      FOREIGN KEY (`schema_id`)
      REFERENCES `schema`(`id`)
    );
    ```

    

- `value`

  - 建表语句

    ```mysql
    CREATE TABLE `value`(
      `id` BIGINT NOT NULL AUTO_INCREMENT,
      `value` TEXT NULL,
      `field_id` BIGINT NOT NULL,
      `entity_id` BIGINT NOT NULL,
        PRIMARY KEY (`id`),
      INDEX `fk_value_entity_idx`(`entity_id` ASC),
      INDEX `fk_value_field_idx`(`field_id` ASC),
      CONSTRAINT `fk_value_field`
      FOREIGN KEY (`field_id`)
      REFERENCES `field`(`id`),
      CONSTRAINT `fk_value_entity`
      FOREIGN KEY (`entity_id`)
      REFERENCES `entity`(`id`)
    );
    ```

    

#### 测试数据

```mysql
insert into `schema` (id,name,`desc`) values (1,'host','主机');
insert into `schema` (id,name,`desc`) values (2,'switch','交换机');



insert into `field` (`name`,schema_id) values('hostname',1);
insert into `field` (`name`,schema_id) values ('ip',1);

insert into `entity` (`key`,schema_id) values ('asdasdasdasdasdaaaaaa',1);

insert into `value` (entity_id,field_id,`value`) values (1,1,'WEBSERVER');
insert into `value` (entity_id,field_id,`value`) values (1,2,'192.168.10.3');



#查询

```

