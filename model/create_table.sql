use boke;

drop table `users`;
drop table `articles`;
drop table `comments`;

CREATE TABLE IF NOT EXISTS `users`(
   `user_id` VARCHAR(32) NOT NULL,
   `name` VARCHAR(20) NOT NULL,
   `password` VARCHAR(32) NOT NULL,
   `created` VARCHAR(18) NOT NULL,
   `image_url` VARCHAR(32) NOT NULL,
   `description` TEXT,
   PRIMARY KEY ( `user_id` ),
   UNIQUE (`name`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `articles`(
   `article_id` VARCHAR(32) NOT NULL,
   `writor_id` VARCHAR(32) NOT NULL,
   `title` TINYTEXT NOT NULL,
   `description` TEXT,
   `content` TEXT,
   `created` VARCHAR(32) NOT NULL,
   `writor` VARCHAR(20) NOT NULL,
   PRIMARY KEY ( `article_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `comments`(
   `comment_id` VARCHAR(32) NOT NULL,
   `actor_id` VARCHAR(32) NOT NULL,
   `writor_id` VARCHAR(32) NOT NULL,
   `article_id` VARCHAR(32) NOT NULL,
   `created` VARCHAR(18) NOT NULL,
   `actor` VARCHAR(20) NOT NULL,
   `writor` VARCHAR(20) NOT NULL,
   `content` TEXT,
   PRIMARY KEY ( `comment_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
