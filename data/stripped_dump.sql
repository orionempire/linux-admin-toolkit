DROP TABLE IF EXISTS auth_permission;
CREATE TABLE IF NOT EXISTS `auth_permission` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` varchar(50) NOT NULL,
    `content_type_id` integer NOT NULL,
    `codename` varchar(100) NOT NULL,
    UNIQUE (`content_type_id`, `codename`)
);
INSERT INTO auth_permission VALUES(1,'Can add permission',1,'add_permission');
INSERT INTO auth_permission VALUES(2,'Can change permission',1,'change_permission');
INSERT INTO auth_permission VALUES(3,'Can delete permission',1,'delete_permission');
INSERT INTO auth_permission VALUES(4,'Can add group',2,'add_group');
INSERT INTO auth_permission VALUES(5,'Can change group',2,'change_group');
INSERT INTO auth_permission VALUES(6,'Can delete group',2,'delete_group');
INSERT INTO auth_permission VALUES(7,'Can add user',3,'add_user');
INSERT INTO auth_permission VALUES(8,'Can change user',3,'change_user');
INSERT INTO auth_permission VALUES(9,'Can delete user',3,'delete_user');
INSERT INTO auth_permission VALUES(10,'Can add content type',4,'add_contenttype');
INSERT INTO auth_permission VALUES(11,'Can change content type',4,'change_contenttype');
INSERT INTO auth_permission VALUES(12,'Can delete content type',4,'delete_contenttype');
INSERT INTO auth_permission VALUES(13,'Can add session',5,'add_session');
INSERT INTO auth_permission VALUES(14,'Can change session',5,'change_session');
INSERT INTO auth_permission VALUES(15,'Can delete session',5,'delete_session');
INSERT INTO auth_permission VALUES(16,'Can add site',6,'add_site');
INSERT INTO auth_permission VALUES(17,'Can change site',6,'change_site');
INSERT INTO auth_permission VALUES(18,'Can delete site',6,'delete_site');
INSERT INTO auth_permission VALUES(19,'Can add log entry',7,'add_logentry');
INSERT INTO auth_permission VALUES(20,'Can change log entry',7,'change_logentry');
INSERT INTO auth_permission VALUES(21,'Can delete log entry',7,'delete_logentry');
INSERT INTO auth_permission VALUES(22,'Can add enclosure',8,'add_enclosure');
INSERT INTO auth_permission VALUES(23,'Can change enclosure',8,'change_enclosure');
INSERT INTO auth_permission VALUES(24,'Can delete enclosure',8,'delete_enclosure');
INSERT INTO auth_permission VALUES(25,'Can add enclosure_ detail',9,'add_enclosure_detail');
INSERT INTO auth_permission VALUES(26,'Can change enclosure_ detail',9,'change_enclosure_detail');
INSERT INTO auth_permission VALUES(27,'Can delete enclosure_ detail',9,'delete_enclosure_detail');
INSERT INTO auth_permission VALUES(28,'Can add enclosure_ additional_ip',10,'add_enclosure_additional_ip');
INSERT INTO auth_permission VALUES(29,'Can change enclosure_ additional_ip',10,'change_enclosure_additional_ip');
INSERT INTO auth_permission VALUES(30,'Can delete enclosure_ additional_ip',10,'delete_enclosure_additional_ip');
INSERT INTO auth_permission VALUES(31,'Can add enclosure_ wire_ run',11,'add_enclosure_wire_run');
INSERT INTO auth_permission VALUES(32,'Can change enclosure_ wire_ run',11,'change_enclosure_wire_run');
INSERT INTO auth_permission VALUES(33,'Can delete enclosure_ wire_ run',11,'delete_enclosure_wire_run');
INSERT INTO auth_permission VALUES(34,'Can add physical',12,'add_physical');
INSERT INTO auth_permission VALUES(35,'Can change physical',12,'change_physical');
INSERT INTO auth_permission VALUES(36,'Can delete physical',12,'delete_physical');
INSERT INTO auth_permission VALUES(37,'Can add physical_ detail',13,'add_physical_detail');
INSERT INTO auth_permission VALUES(38,'Can change physical_ detail',13,'change_physical_detail');
INSERT INTO auth_permission VALUES(39,'Can delete physical_ detail',13,'delete_physical_detail');
INSERT INTO auth_permission VALUES(40,'Can add physical_ services',14,'add_physical_services');
INSERT INTO auth_permission VALUES(41,'Can change physical_ services',14,'change_physical_services');
INSERT INTO auth_permission VALUES(42,'Can delete physical_ services',14,'delete_physical_services');
INSERT INTO auth_permission VALUES(43,'Can add physical_ additional_ip',15,'add_physical_additional_ip');
INSERT INTO auth_permission VALUES(44,'Can change physical_ additional_ip',15,'change_physical_additional_ip');
INSERT INTO auth_permission VALUES(45,'Can delete physical_ additional_ip',15,'delete_physical_additional_ip');
INSERT INTO auth_permission VALUES(46,'Can add physical_ wire_ run',16,'add_physical_wire_run');
INSERT INTO auth_permission VALUES(47,'Can change physical_ wire_ run',16,'change_physical_wire_run');
INSERT INTO auth_permission VALUES(48,'Can delete physical_ wire_ run',16,'delete_physical_wire_run');
INSERT INTO auth_permission VALUES(49,'Can add virtual',17,'add_virtual');
INSERT INTO auth_permission VALUES(50,'Can change virtual',17,'change_virtual');
INSERT INTO auth_permission VALUES(51,'Can delete virtual',17,'delete_virtual');
INSERT INTO auth_permission VALUES(52,'Can add virtual_ detail',18,'add_virtual_detail');
INSERT INTO auth_permission VALUES(53,'Can change virtual_ detail',18,'change_virtual_detail');
INSERT INTO auth_permission VALUES(54,'Can delete virtual_ detail',18,'delete_virtual_detail');
INSERT INTO auth_permission VALUES(55,'Can add virtual_ services',19,'add_virtual_services');
INSERT INTO auth_permission VALUES(56,'Can change virtual_ services',19,'change_virtual_services');
INSERT INTO auth_permission VALUES(57,'Can delete virtual_ services',19,'delete_virtual_services');
INSERT INTO auth_permission VALUES(58,'Can add virtual_ additional_ip',20,'add_virtual_additional_ip');
INSERT INTO auth_permission VALUES(59,'Can change virtual_ additional_ip',20,'change_virtual_additional_ip');
INSERT INTO auth_permission VALUES(60,'Can delete virtual_ additional_ip',20,'delete_virtual_additional_ip');
INSERT INTO auth_permission VALUES(61,'Can add storage',21,'add_storage');
INSERT INTO auth_permission VALUES(62,'Can change storage',21,'change_storage');
INSERT INTO auth_permission VALUES(63,'Can delete storage',21,'delete_storage');
INSERT INTO auth_permission VALUES(64,'Can add storage_ additional_ip',22,'add_storage_additional_ip');
INSERT INTO auth_permission VALUES(65,'Can change storage_ additional_ip',22,'change_storage_additional_ip');
INSERT INTO auth_permission VALUES(66,'Can delete storage_ additional_ip',22,'delete_storage_additional_ip');
INSERT INTO auth_permission VALUES(67,'Can add storage_ wire_ run',23,'add_storage_wire_run');
INSERT INTO auth_permission VALUES(68,'Can change storage_ wire_ run',23,'change_storage_wire_run');
INSERT INTO auth_permission VALUES(69,'Can delete storage_ wire_ run',23,'delete_storage_wire_run');
DROP TABLE IF EXISTS auth_group_permissions;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `group_id` integer NOT NULL,
    `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`),
    UNIQUE (`group_id`, `permission_id`)
);
DROP TABLE IF EXISTS auth_group;
CREATE TABLE IF NOT EXISTS `auth_group` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` varchar(80) NOT NULL UNIQUE
);
DROP TABLE IF EXISTS auth_user_groups;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `user_id` integer NOT NULL,
    `group_id` integer NOT NULL REFERENCES `auth_group` (`id`),
    UNIQUE (`user_id`, `group_id`)
);
DROP TABLE IF EXISTS auth_user_user_permissions;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `user_id` integer NOT NULL,
    `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`),
    UNIQUE (`user_id`, `permission_id`)
);
INSERT INTO auth_user_user_permissions VALUES(1,2,35);
INSERT INTO auth_user_user_permissions VALUES(2,2,50);
DROP TABLE IF EXISTS auth_user;
CREATE TABLE IF NOT EXISTS `auth_user` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `password` varchar(128) NOT NULL,
    `last_login` datetime NOT NULL,
    `is_superuser` bool NOT NULL,
    `username` varchar(30) NOT NULL UNIQUE,
    `first_name` varchar(30) NOT NULL,
    `last_name` varchar(30) NOT NULL,
    `email` varchar(75) NOT NULL,
    `is_staff` bool NOT NULL,
    `is_active` bool NOT NULL,
    `date_joined` datetime NOT NULL
);
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$10000$Q6pHBZBRK3X2$AHfB8wkd/qKpTFagSZ00UaHSkXpSq73RHGxHUrqm77M=','2013-03-06 00:49:06.491186',1,'sysadmin','','','sysadmin@linux-admin-toolkit.com',1,1,'2013-03-06 00:48:53.398536');
INSERT INTO auth_user VALUES(2,'pbkdf2_sha256$10000$eH3hzr5Saqgr$zwvA91rhnU/6CyKdPmQClcxjgU2zSU39gKJIEqwL5jY=','2013-03-06 00:48:53.647801',0,'view','','','viewonly@nodomain.com',0,1,'2013-03-06 00:48:53.647801');
DROP TABLE IF EXISTS django_content_type;
CREATE TABLE IF NOT EXISTS `django_content_type` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    `app_label` varchar(100) NOT NULL,
    `model` varchar(100) NOT NULL,
    UNIQUE (`app_label`, `model`)
);
INSERT INTO django_content_type VALUES(1,'permission','auth','permission');
INSERT INTO django_content_type VALUES(2,'group','auth','group');
INSERT INTO django_content_type VALUES(3,'user','auth','user');
INSERT INTO django_content_type VALUES(4,'content type','contenttypes','contenttype');
INSERT INTO django_content_type VALUES(5,'session','sessions','session');
INSERT INTO django_content_type VALUES(6,'site','sites','site');
INSERT INTO django_content_type VALUES(7,'log entry','admin','logentry');
INSERT INTO django_content_type VALUES(8,'enclosure','admin_gui','enclosure');
INSERT INTO django_content_type VALUES(9,'enclosure_ detail','admin_gui','enclosure_detail');
INSERT INTO django_content_type VALUES(10,'enclosure_ additional_ip','admin_gui','enclosure_additional_ip');
INSERT INTO django_content_type VALUES(11,'enclosure_ wire_ run','admin_gui','enclosure_wire_run');
INSERT INTO django_content_type VALUES(12,'physical','admin_gui','physical');
INSERT INTO django_content_type VALUES(13,'physical_ detail','admin_gui','physical_detail');
INSERT INTO django_content_type VALUES(14,'physical_ services','admin_gui','physical_services');
INSERT INTO django_content_type VALUES(15,'physical_ additional_ip','admin_gui','physical_additional_ip');
INSERT INTO django_content_type VALUES(16,'physical_ wire_ run','admin_gui','physical_wire_run');
INSERT INTO django_content_type VALUES(17,'virtual','admin_gui','virtual');
INSERT INTO django_content_type VALUES(18,'virtual_ detail','admin_gui','virtual_detail');
INSERT INTO django_content_type VALUES(19,'virtual_ services','admin_gui','virtual_services');
INSERT INTO django_content_type VALUES(20,'virtual_ additional_ip','admin_gui','virtual_additional_ip');
INSERT INTO django_content_type VALUES(21,'storage','admin_gui','storage');
INSERT INTO django_content_type VALUES(22,'storage_ additional_ip','admin_gui','storage_additional_ip');
INSERT INTO django_content_type VALUES(23,'storage_ wire_ run','admin_gui','storage_wire_run');
DROP TABLE IF EXISTS django_session;
CREATE TABLE IF NOT EXISTS `django_session` (
    `session_key` varchar(40) NOT NULL PRIMARY KEY,
    `session_data` text NOT NULL,
    `expire_date` datetime NOT NULL
);
INSERT INTO django_session VALUES('0rks9508ry3nzayu5ce8i3a19yve029u','YWI1NjY4ZTgzYThiYmUzZWY4Mzc4ZWU5ZjA5MjkxZmYzODg5MDEyMTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu','2013-03-20 00:49:06.519984');
DROP TABLE IF EXISTS django_site;
CREATE TABLE IF NOT EXISTS `django_site` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `domain` varchar(100) NOT NULL,
    `name` varchar(50) NOT NULL
);
INSERT INTO django_site VALUES(1,'example.com','example.com');
DROP TABLE IF EXISTS django_admin_log;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `action_time` datetime NOT NULL,
    `user_id` integer NOT NULL REFERENCES `auth_user` (`id`),
    `content_type_id` integer REFERENCES `django_content_type` (`id`),
    `object_id` text,
    `object_repr` varchar(200) NOT NULL,
    `action_flag` smallint unsigned NOT NULL,
    `change_message` text NOT NULL
);
DROP TABLE IF EXISTS admin_gui_enclosure;
CREATE TABLE IF NOT EXISTS `admin_gui_enclosure` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `enclosure_name` varchar(255) NOT NULL UNIQUE,
    `primary_ip_address` char(39) UNIQUE,
    `status` varchar(255) NOT NULL,
    `location_code` varchar(255) NOT NULL,
    `point_of_contact` varchar(255) NOT NULL,
    `note` text NOT NULL,
    `ip_active` bool
);
INSERT INTO admin_gui_enclosure VALUES(1,'nwr-pre-adm-mng01','192.168.1.5','active','nwr01-1-1-10','Cat Stevens','test enc 1',NULL);
INSERT INTO admin_gui_enclosure VALUES(2,'nwr-pre-adm-mng02','192.168.1.6','active','nwr01-1-1-22','David Davidson','test enc 2',NULL);
INSERT INTO admin_gui_enclosure VALUES(3,'nwr-pre-adm-mng03','192.168.1.7','active','nwr01-1-2-07','David Davidson','test enc 3',NULL);
INSERT INTO admin_gui_enclosure VALUES(4,'nwr-pre-adm-mng04','192.168.1.8','active','nwr01-1-3-07','David Davidson','test enc 4',NULL);
INSERT INTO admin_gui_enclosure VALUES(5,'nwr-pre-adm-mng05','192.168.1.9','active','nwr01-2-2-07','David Davidson','test enc 5',NULL);
INSERT INTO admin_gui_enclosure VALUES(6,'nwr-pre-adm-mng06','192.168.1.10','active','nwr01-2-3-07','David Davidson','test enc 6',NULL);
DROP TABLE IF EXISTS admin_gui_enclosure_detail;
CREATE TABLE IF NOT EXISTS `admin_gui_enclosure_detail` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `enclosure_id` integer NOT NULL UNIQUE REFERENCES `admin_gui_enclosure` (`id`),
    `service_tag` varchar(255) NOT NULL,
    `model` varchar(255) NOT NULL
);
INSERT INTO admin_gui_enclosure_detail VALUES(1,1,'123G786F','HP C7000 Blade Chassis');
INSERT INTO admin_gui_enclosure_detail VALUES(2,2,'ASHN65D3','Cisco 5100 Blade chassis');
INSERT INTO admin_gui_enclosure_detail VALUES(3,3,'JGDF423A','HP C3000 Blade Chassis');
INSERT INTO admin_gui_enclosure_detail VALUES(4,4,'ASHN65D5','Cisco 5100 Blade chassis');
INSERT INTO admin_gui_enclosure_detail VALUES(5,5,'ASHN65D4','Cisco 5100 Blade chassis');
INSERT INTO admin_gui_enclosure_detail VALUES(6,6,'123G7836','HP C3000 Blade Chassis');
DROP TABLE IF EXISTS admin_gui_enclosure_additional_ip;
CREATE TABLE IF NOT EXISTS `admin_gui_enclosure_additional_ip` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `enclosure_id` integer NOT NULL REFERENCES `admin_gui_enclosure` (`id`),
    `additional_ip` char(39) NOT NULL UNIQUE,
    `ip_active` bool
);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(1,1,'192.168.150.5',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(2,2,'192.168.150.6',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(3,3,'192.168.150.7',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(4,4,'192.168.150.8',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(5,5,'192.168.150.9',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(6,6,'192.168.150.10',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(7,1,'192.168.150.50',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(8,2,'192.168.150.51',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(9,3,'192.168.150.52',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(10,4,'192.168.150.53',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(11,5,'192.168.150.54',NULL);
INSERT INTO admin_gui_enclosure_additional_ip VALUES(12,6,'192.168.150.55',NULL);
DROP TABLE IF EXISTS admin_gui_enclosure_wire_run;
CREATE TABLE IF NOT EXISTS `admin_gui_enclosure_wire_run` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `enclosure_id` integer NOT NULL REFERENCES `admin_gui_enclosure` (`id`),
    `source_port` varchar(255) NOT NULL,
    `destination_name` varchar(255) NOT NULL,
    `destination_port` varchar(255) NOT NULL
);
INSERT INTO admin_gui_enclosure_wire_run VALUES(1,1,'3','network 01','5');
INSERT INTO admin_gui_enclosure_wire_run VALUES(2,2,'4','network 02','6');
INSERT INTO admin_gui_enclosure_wire_run VALUES(3,3,'5','network 03','7');
INSERT INTO admin_gui_enclosure_wire_run VALUES(4,4,'6','network 04','8');
INSERT INTO admin_gui_enclosure_wire_run VALUES(5,5,'7','network 05','9');
INSERT INTO admin_gui_enclosure_wire_run VALUES(6,6,'8','network 06','10');
DROP TABLE IF EXISTS admin_gui_physical;
CREATE TABLE IF NOT EXISTS `admin_gui_physical` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `physical_name` varchar(255) NOT NULL UNIQUE,
    `primary_ip_address` char(39) UNIQUE,
    `role` varchar(255) NOT NULL,
    `purpose` varchar(255) NOT NULL,
    `point_of_contact` varchar(255) NOT NULL,
    `host_enclosure_name_id` integer REFERENCES `admin_gui_enclosure` (`id`),
    `status` varchar(255) NOT NULL,
    `note` text NOT NULL,
    `selected` bool,
    `ip_active` bool
);
INSERT INTO admin_gui_physical VALUES(1,'seq-prd-adm-vir01','192.168.1.20','Virtualization Host','Hosts Customer facing Images','David Davidson',1,'active','test physical 1',NULL,NULL);
INSERT INTO admin_gui_physical VALUES(2,'seq-prd-adm-vir02','192.168.1.21','Virtualization Host','Hosts Customer facing Images','David Davidson',2,'active','test physical 2',NULL,NULL);
INSERT INTO admin_gui_physical VALUES(3,'seq-prd-adm-vir03','192.168.1.25','Virtualization Host','Hosts Corporate Images','David Davidson',2,'active','test physical 3',NULL,NULL);
INSERT INTO admin_gui_physical VALUES(4,'seq-prd-adm-vir04','192.168.1.75','Virtualization Host','Hosts Development Images','David Davidson',4,'active','test physical 4',NULL,NULL);
INSERT INTO admin_gui_physical VALUES(5,'seq-prd-adm-vir05','192.168.1.76','Virtualization Host','Hosts Development Images','David Davidson',1,'active','test physical 5',NULL,NULL);
INSERT INTO admin_gui_physical VALUES(6,'seq-prd-adm-vir06','192.168.1.26','Virtualization Host','Hosts Corporate and Support Images','David Davidson',6,'active','test physical 6',NULL,NULL);
INSERT INTO admin_gui_physical VALUES(7,'seq-prd-adm-vir07','192.168.1.37','Virtualization Host','Hosts Performance Engineering Images','David Davidson',2,'active','test physical 7',NULL,NULL);
INSERT INTO admin_gui_physical VALUES(8,'seq-prd-adm-vir08','192.168.1.36','Virtualization Host','Hosts Performance Engineering Images','David Davidson',5,'active','test physical 8',NULL,NULL);
INSERT INTO admin_gui_physical VALUES(9,'seq-prd-adm-vir09','192.168.1.35','Virtualization Host','Hosts Performance Engineering Images','David Davidson',3,'active','test physical 9',NULL,NULL);
DROP TABLE IF EXISTS admin_gui_physical_detail;
CREATE TABLE IF NOT EXISTS `admin_gui_physical_detail` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `physical_id` integer NOT NULL UNIQUE REFERENCES `admin_gui_physical` (`id`),
    `location_code` varchar(255) NOT NULL,
    `service_tag` varchar(255) NOT NULL,
    `console_address` char(39) UNIQUE,
    `os` varchar(255) NOT NULL,
    `model` varchar(255) NOT NULL,
    `size` varchar(255) NOT NULL,
    `console_ip_active` bool
);
INSERT INTO admin_gui_physical_detail VALUES(1,1,'nwr01-1-1-10','234H2J3K13JH1','192.168.100.20','Redhat EL 6.1','HP DL380 G7','2 X 6 X 3.33GHz | 24GB',NULL);
INSERT INTO admin_gui_physical_detail VALUES(2,2,'nwr01-1-1-22','234H2J3K13JH2','192.168.100.21','Redhat EL 6.1','HP DL380 G7','2 X 6 X 3.33GHz | 24GB',NULL);
INSERT INTO admin_gui_physical_detail VALUES(3,3,'nwr01-1-1-22','234H2J3K13JH3','192.168.100.25','Redhat EL 5.6','HP DL360 G5','2 X 4 X 2.5GHz | 16GB',NULL);
INSERT INTO admin_gui_physical_detail VALUES(4,4,'nwr01-1-3-07','234H2J3K13JH4','192.168.100.30','Redhat EL 6.1','HP BL680 G5','4 X 6 X 2.33 GHz | 64GB',NULL);
INSERT INTO admin_gui_physical_detail VALUES(5,5,'nwr01-1-1-10','234H2J3K13JH5','192.168.100.31','Redhat EL 6.1','HP BL680 G5','4 X 6 X 2.33 GHz | 64GB',NULL);
INSERT INTO admin_gui_physical_detail VALUES(6,6,'nwr01-2-3-07','234H2J3K13JH6','192.168.100.26','Redhat EL 6.1','HP DL380 G7','2 X 6 X 3.33GHz | 24GB',NULL);
INSERT INTO admin_gui_physical_detail VALUES(7,7,'nwr01-1-1-22','234H2J3K13JH7','192.168.100.37','VMWare 5.0','CISCO B200 M2','2 X 6 X 3.06 GHz | 48GB',NULL);
INSERT INTO admin_gui_physical_detail VALUES(8,8,'nwr01-2-2-07','234H2J3K13JH8','192.168.100.36','VMWare 5.0','CISCO B200 M2','2 X 6 X 3.06 GHz | 48GB',NULL);
INSERT INTO admin_gui_physical_detail VALUES(9,9,'nwr01-1-2-07','234H2J3K13JH9','192.168.100.35','VMWare 5.0','CISCO B200 M2','2 X 6 X 3.06 GHz | 48GB',NULL);
DROP TABLE IF EXISTS admin_gui_physical_services;
CREATE TABLE IF NOT EXISTS `admin_gui_physical_services` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `physical_id` integer NOT NULL UNIQUE REFERENCES `admin_gui_physical` (`id`),
    `admin_cluster_group_01` varchar(255) NOT NULL,
    `admin_cluster_group_02` varchar(255) NOT NULL,
    `script_profile` varchar(255) NOT NULL
);
INSERT INTO admin_gui_physical_services VALUES(1,1,'customer','vm_host','none');
INSERT INTO admin_gui_physical_services VALUES(2,2,'customer','vm_host','none');
INSERT INTO admin_gui_physical_services VALUES(3,3,'internal','vm_host','none');
INSERT INTO admin_gui_physical_services VALUES(4,4,'internal','vm_host','none');
INSERT INTO admin_gui_physical_services VALUES(5,5,'internal','vm_host','none');
INSERT INTO admin_gui_physical_services VALUES(6,6,'internal','vm_host','none');
INSERT INTO admin_gui_physical_services VALUES(7,7,'internal','vm_host','none');
INSERT INTO admin_gui_physical_services VALUES(8,8,'internal','vm_host','none');
INSERT INTO admin_gui_physical_services VALUES(9,9,'internal','vm_host','none');
DROP TABLE IF EXISTS admin_gui_physical_additional_ip;
CREATE TABLE IF NOT EXISTS `admin_gui_physical_additional_ip` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `physical_id` integer NOT NULL REFERENCES `admin_gui_physical` (`id`),
    `additional_ip` char(39) NOT NULL UNIQUE,
    `ip_active` bool
);
INSERT INTO admin_gui_physical_additional_ip VALUES(1,1,'192.168.150.56',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(2,2,'192.168.150.57',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(3,3,'192.168.150.58',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(4,4,'192.168.150.59',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(5,5,'192.168.150.60',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(6,6,'192.168.150.61',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(7,7,'192.168.150.62',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(8,8,'192.168.150.63',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(9,9,'192.168.150.64',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(10,1,'192.168.150.65',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(11,2,'192.168.150.66',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(12,3,'192.168.150.67',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(13,4,'192.168.150.68',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(14,5,'192.168.150.69',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(15,6,'192.168.150.70',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(16,7,'192.168.150.71',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(17,8,'192.168.150.72',NULL);
INSERT INTO admin_gui_physical_additional_ip VALUES(18,9,'192.168.150.73',NULL);
DROP TABLE IF EXISTS admin_gui_physical_wire_run;
CREATE TABLE IF NOT EXISTS `admin_gui_physical_wire_run` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `physical_id` integer NOT NULL REFERENCES `admin_gui_physical` (`id`),
    `source_port` varchar(255) NOT NULL,
    `destination_name` varchar(255) NOT NULL,
    `destination_port` varchar(255) NOT NULL
);
INSERT INTO admin_gui_physical_wire_run VALUES(1,2,'5','network 01','7');
INSERT INTO admin_gui_physical_wire_run VALUES(2,2,'6','network 02','8');
INSERT INTO admin_gui_physical_wire_run VALUES(3,2,'7','network 03','9');
INSERT INTO admin_gui_physical_wire_run VALUES(4,2,'8','network 04','10');
INSERT INTO admin_gui_physical_wire_run VALUES(5,2,'9','network 05','11');
INSERT INTO admin_gui_physical_wire_run VALUES(6,2,'10','network 06','12');
INSERT INTO admin_gui_physical_wire_run VALUES(7,2,'11','network 07','13');
DROP TABLE IF EXISTS admin_gui_virtual;
CREATE TABLE IF NOT EXISTS `admin_gui_virtual` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `virtual_name` varchar(255) NOT NULL UNIQUE,
    `primary_ip_address` char(39) UNIQUE,
    `role` varchar(255) NOT NULL,
    `purpose` varchar(255) NOT NULL,
    `point_of_contact` varchar(255) NOT NULL,
    `host_physical_name_id` integer REFERENCES `admin_gui_physical` (`id`),
    `status` varchar(255) NOT NULL,
    `selected` bool,
    `ip_active` bool,
    `note` text NOT NULL
);
INSERT INTO admin_gui_virtual VALUES(1,'seq-dev-cds-app02','192.168.1.113','Jboss Application Server','Customer Trading','Scottie Feave',4,'active',NULL,NULL,'test vir 1');
INSERT INTO admin_gui_virtual VALUES(2,'seq-dev-cds-app03','192.168.1.115','Jboss development application server','Customer Trading','Scottie Feave',4,'active',NULL,NULL,'test vir 2');
INSERT INTO admin_gui_virtual VALUES(3,'seq-dev-cds-app04','192.168.1.118','Jboss Application Server','Customer Trading','Scottie Feave',4,'active',NULL,NULL,'test vir 3');
INSERT INTO admin_gui_virtual VALUES(4,'seq-dev-cds-app05','192.168.1.119','Jboss Application Server','Customer Trading','Scottie Feave',5,'active',NULL,NULL,'test vir 4');
INSERT INTO admin_gui_virtual VALUES(5,'seq-dev-cds-app06','192.168.1.120','Jboss Application Server','Customer Trading','Bart Realson',5,'active',NULL,NULL,'test vir 5');
INSERT INTO admin_gui_virtual VALUES(6,'seq-dev-cds-app07','192.168.1.122','Jboss Application Server','Customer Trading','Bart Realson',NULL,'active',NULL,NULL,'test vir 6');
INSERT INTO admin_gui_virtual VALUES(7,'seq-dev-cds-app09','192.168.1.133','Jboss Application Server','Database Gateway','Bart Realson',NULL,'active',NULL,NULL,'test vir 7');
INSERT INTO admin_gui_virtual VALUES(8,'seq-dev-dat-orc01','192.168.1.121','Oracle database server','Database','Bart Realson',NULL,'active',NULL,NULL,'test vir 8');
INSERT INTO admin_gui_virtual VALUES(9,'seq-dev-stp-app01','192.168.1.130','Jboss Application Server','Customer Onboarding','Bart Realson',NULL,'active',NULL,NULL,'test vir 9');
INSERT INTO admin_gui_virtual VALUES(10,'seq-dev-utl-off01','192.168.1.140','Corporate Application Server','Analytic Report Generation','David Davidson',NULL,'active',NULL,NULL,'test vir 10');
INSERT INTO admin_gui_virtual VALUES(11,'seq-int-cds-app02','192.168.1.131','Jboss Application Server','Customer Trading','Bart Realson',NULL,'active',NULL,NULL,'test vir 11');
INSERT INTO admin_gui_virtual VALUES(12,'seq-int-cds-app03','192.168.1.124','Jboss Application Server','Customer Trading','Raj Bobahj',NULL,'active',NULL,NULL,'test vir 12');
INSERT INTO admin_gui_virtual VALUES(13,'seq-int-cds-app04','192.168.1.125','Jboss Application Server','Customer Trading','Raj Bobahj',NULL,'active',NULL,NULL,'test vir 13');
INSERT INTO admin_gui_virtual VALUES(14,'seq-int-cds-app08','192.168.1.155','Jboss Application Server','Customer Trading','Lisa Realson',NULL,'active',NULL,NULL,'test vir 14');
INSERT INTO admin_gui_virtual VALUES(15,'seq-int-cds-pxy01','192.168.2.112','Customer Gateway','Customer Trading','Raj Bobahj',NULL,'active',NULL,NULL,'test vir 15');
INSERT INTO admin_gui_virtual VALUES(16,'seq-int-mrg-api01','192.168.1.147','MRG Compute Cluster','Market Maker Access','Lisa Realson',NULL,'active',NULL,NULL,'test vir 16');
INSERT INTO admin_gui_virtual VALUES(17,'seq-int-mrg-api02','192.168.1.148','MRG Compute Cluster','Market Maker Access','Lisa Realson',NULL,'active',NULL,NULL,'test vir 17');
INSERT INTO admin_gui_virtual VALUES(18,'seq-int-mrg-api03','192.168.1.149','MRG Compute Cluster','Market Maker Access','Lisa Realson',NULL,'active',NULL,NULL,'test vir 18');
INSERT INTO admin_gui_virtual VALUES(19,'seq-int-mrg-csl01','192.168.1.154','MRG Compute Cluster','Market Maker Access','Lisa Realson',NULL,'active',NULL,NULL,'test vir 19');
INSERT INTO admin_gui_virtual VALUES(20,'seq-int-mrg-gui01','192.168.1.150','MRG Compute Cluster','Market Maker Access','Lisa Realson',NULL,'active',NULL,NULL,'test vir 20');
INSERT INTO admin_gui_virtual VALUES(21,'seq-int-mrg-gui02','192.168.1.151','MRG Compute Cluster','Market Maker Access','Lisa Realson',5,'active',NULL,NULL,'test vir 21');
INSERT INTO admin_gui_virtual VALUES(22,'seq-int-mrg-gui03','192.168.1.152','MRG Compute Cluster','Market Maker Access','Lisa Realson',5,'active',NULL,NULL,'test vir 22');
INSERT INTO admin_gui_virtual VALUES(23,'seq-int-mrg-jbs01','192.168.1.135','MRG Compute Cluster','Market Maker Access','Scottie Feave',9,'active',NULL,NULL,'test vir 23');
INSERT INTO admin_gui_virtual VALUES(24,'seq-int-mrg-jbs02','192.168.1.136','MRG Compute Cluster','Market Maker Access','David Davidson',9,'active',NULL,NULL,'test vir 24');
INSERT INTO admin_gui_virtual VALUES(25,'seq-int-mrg-jbs03','192.168.1.137','MRG Compute Cluster','Market Maker Access','David Davidson',9,'active',NULL,NULL,'test vir 25');
INSERT INTO admin_gui_virtual VALUES(26,'seq-prd-adm-crp01','192.168.1.114','Corporate Application Server','Corporate Bug tracking','Scottie Feave',5,'active',NULL,NULL,'test vir 26');
INSERT INTO admin_gui_virtual VALUES(27,'seq-prd-adm-str01','192.168.1.134','Corporate Application Server','System Administration','Scottie Feave',6,'active',NULL,NULL,'test vir 27');
INSERT INTO admin_gui_virtual VALUES(28,'seq-prd-adm-utl01','192.168.1.117','Corporate Application Server','System Administration','Scottie Feave',6,'active',NULL,NULL,'test vir 28');
INSERT INTO admin_gui_virtual VALUES(29,'seq-prd-adm-utl03','192.168.1.144','Corporate Application Server','System Administration','David Davidson',6,'active',NULL,NULL,'test vir 29');
INSERT INTO admin_gui_virtual VALUES(30,'seq-prd-irs-app01','192.168.35.50','Jboss Application Server','Database Gateway','Scottie Feave',4,'active',NULL,NULL,'test vir 30');
INSERT INTO admin_gui_virtual VALUES(31,'seq-prd-stp-app01','192.168.35.52','Jboss Application Server','Database Gateway','Scottie Feave',4,'active',NULL,NULL,'test vir 31');
INSERT INTO admin_gui_virtual VALUES(32,'seq-qat-cds-app01','192.168.1.126','Jboss Application Server','Customer Onboarding','Raj Bobahj',2,'active',NULL,NULL,'test vir 32');
INSERT INTO admin_gui_virtual VALUES(33,'seq-qat-cds-app02','192.168.1.127','Jboss Application Server','Customer Onboarding','Raj Bobahj',1,'active',NULL,NULL,'test vir 33');
INSERT INTO admin_gui_virtual VALUES(34,'seq-qat-cds-pxy01','172.2.0.14','Jboss Application Server','Customer Gateway','Raj Bobahj',2,'active',NULL,NULL,'test vir 34');
INSERT INTO admin_gui_virtual VALUES(35,'seq-qat-cds-pxy04','172.2.0.11','Jboss Application Server','Customer Gateway','Bart Realson',2,'active',NULL,NULL,'test vir 35');
INSERT INTO admin_gui_virtual VALUES(36,'seq-qat-irs-app01','192.168.1.132','Jboss Application Server','Customer Onboarding','Bart Realson',4,'active',NULL,NULL,'test vir 36');
INSERT INTO admin_gui_virtual VALUES(37,'seq-qat-irs-sta01','192.168.1.128','Jboss Application Server','Customer Onboarding','Raj Bobahj',4,'active',NULL,NULL,'test vir 37');
INSERT INTO admin_gui_virtual VALUES(38,'seq-qat-irs-sta02','192.168.1.129','Jboss Application Server','Customer Onboarding','Raj Bobahj',2,'active',NULL,NULL,'test vir 38');
INSERT INTO admin_gui_virtual VALUES(39,'seq-qat-utl-off01','192.168.1.141','Corporate Application Server','Analytic Report Generation','David Davidson',1,'active',NULL,NULL,'test vir 39');
INSERT INTO admin_gui_virtual VALUES(40,'seq-qat-utl-off02','192.168.1.142','Corporate Application Server','Analytic Report Generation','David Davidson',2,'active',NULL,NULL,'test vir 40');
DROP TABLE IF EXISTS admin_gui_virtual_detail;
CREATE TABLE IF NOT EXISTS `admin_gui_virtual_detail` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `virtual_id` integer NOT NULL UNIQUE REFERENCES `admin_gui_virtual` (`id`),
    `size` varchar(255) NOT NULL,
    `os` varchar(255) NOT NULL,
    `base_image` varchar(255) NOT NULL
);
INSERT INTO admin_gui_virtual_detail VALUES(1,1,'192.168.1.113','Jboss Application Server','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(2,2,'192.168.1.115','Jboss development application server','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(3,3,'192.168.1.118','Jboss Application Server','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(4,4,'192.168.1.119','Jboss Application Server','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(5,5,'192.168.1.120','Jboss Application Server','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(6,6,'192.168.1.122','Jboss Application Server','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(7,7,'192.168.1.133','Jboss Application Server','Database Gateway');
INSERT INTO admin_gui_virtual_detail VALUES(8,8,'192.168.1.121','Oracle database server','Database');
INSERT INTO admin_gui_virtual_detail VALUES(9,9,'192.168.1.130','Jboss Application Server','Customer Onboarding');
INSERT INTO admin_gui_virtual_detail VALUES(10,10,'192.168.1.140','Corporate Application Server','Analytic Report Generation');
INSERT INTO admin_gui_virtual_detail VALUES(11,11,'192.168.1.131','Jboss Application Server','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(12,12,'192.168.1.124','Jboss Application Server','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(13,13,'192.168.1.125','Jboss Application Server','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(14,14,'192.168.1.155','Jboss Application Server','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(15,15,'192.168.2.112','Customer Gateway','Customer Trading');
INSERT INTO admin_gui_virtual_detail VALUES(16,16,'192.168.1.147','MRG Compute Cluster','Market Maker Access');
INSERT INTO admin_gui_virtual_detail VALUES(17,17,'192.168.1.148','MRG Compute Cluster','Market Maker Access');
INSERT INTO admin_gui_virtual_detail VALUES(18,18,'192.168.1.149','MRG Compute Cluster','Market Maker Access');
INSERT INTO admin_gui_virtual_detail VALUES(19,19,'192.168.1.154','MRG Compute Cluster','Market Maker Access');
INSERT INTO admin_gui_virtual_detail VALUES(20,20,'192.168.1.150','MRG Compute Cluster','Market Maker Access');
INSERT INTO admin_gui_virtual_detail VALUES(21,21,'192.168.1.151','MRG Compute Cluster','Market Maker Access');
INSERT INTO admin_gui_virtual_detail VALUES(22,22,'192.168.1.152','MRG Compute Cluster','Market Maker Access');
INSERT INTO admin_gui_virtual_detail VALUES(23,23,'192.168.1.135','MRG Compute Cluster','Market Maker Access');
INSERT INTO admin_gui_virtual_detail VALUES(24,24,'192.168.1.136','MRG Compute Cluster','Market Maker Access');
INSERT INTO admin_gui_virtual_detail VALUES(25,25,'192.168.1.137','MRG Compute Cluster','Market Maker Access');
INSERT INTO admin_gui_virtual_detail VALUES(26,26,'192.168.1.114','Corporate Application Server','Corporate Bug tracking');
INSERT INTO admin_gui_virtual_detail VALUES(27,27,'192.168.1.134','Corporate Application Server','System Administration');
INSERT INTO admin_gui_virtual_detail VALUES(28,28,'192.168.1.117','Corporate Application Server','System Administration');
INSERT INTO admin_gui_virtual_detail VALUES(29,29,'192.168.1.144','Corporate Application Server','System Administration');
INSERT INTO admin_gui_virtual_detail VALUES(30,30,'192.168.35.50','Jboss Application Server','Database Gateway');
INSERT INTO admin_gui_virtual_detail VALUES(31,31,'192.168.35.52','Jboss Application Server','Database Gateway');
INSERT INTO admin_gui_virtual_detail VALUES(32,32,'192.168.1.126','Jboss Application Server','Customer Onboarding');
INSERT INTO admin_gui_virtual_detail VALUES(33,33,'192.168.1.127','Jboss Application Server','Customer Onboarding');
INSERT INTO admin_gui_virtual_detail VALUES(34,34,'172.2.0.14','Jboss Application Server','Customer Gateway');
INSERT INTO admin_gui_virtual_detail VALUES(35,35,'172.2.0.11','Jboss Application Server','Customer Gateway');
INSERT INTO admin_gui_virtual_detail VALUES(36,36,'192.168.1.132','Jboss Application Server','Customer Onboarding');
INSERT INTO admin_gui_virtual_detail VALUES(37,37,'192.168.1.128','Jboss Application Server','Customer Onboarding');
INSERT INTO admin_gui_virtual_detail VALUES(38,38,'192.168.1.129','Jboss Application Server','Customer Onboarding');
INSERT INTO admin_gui_virtual_detail VALUES(39,39,'192.168.1.141','Corporate Application Server','Analytic Report Generation');
INSERT INTO admin_gui_virtual_detail VALUES(40,40,'192.168.1.142','Corporate Application Server','Analytic Report Generation');
DROP TABLE IF EXISTS admin_gui_virtual_services;
CREATE TABLE IF NOT EXISTS `admin_gui_virtual_services` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `virtual_id` integer NOT NULL UNIQUE REFERENCES `admin_gui_virtual` (`id`),
    `admin_cluster_group_01` varchar(255) NOT NULL,
    `admin_cluster_group_02` varchar(255) NOT NULL,
    `script_profile` varchar(255) NOT NULL
);
INSERT INTO admin_gui_virtual_services VALUES(1,1,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(2,2,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(3,3,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(4,4,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(5,5,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(6,6,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(7,7,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(8,8,'internal','admin','none');
INSERT INTO admin_gui_virtual_services VALUES(9,9,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(10,10,'system','application','none');
INSERT INTO admin_gui_virtual_services VALUES(11,11,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(12,12,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(13,13,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(14,14,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(15,15,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(16,16,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(17,17,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(18,18,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(19,19,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(20,20,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(21,21,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(22,22,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(23,23,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(24,24,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(25,25,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(26,26,'internal','admin','none');
INSERT INTO admin_gui_virtual_services VALUES(27,27,'internal','admin','none');
INSERT INTO admin_gui_virtual_services VALUES(28,28,'system','admin','none');
INSERT INTO admin_gui_virtual_services VALUES(29,29,'internal','admin','none');
INSERT INTO admin_gui_virtual_services VALUES(30,30,'customer','application','none');
INSERT INTO admin_gui_virtual_services VALUES(31,31,'customer','application','none');
INSERT INTO admin_gui_virtual_services VALUES(32,32,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(33,33,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(34,34,'internal','proxy','none');
INSERT INTO admin_gui_virtual_services VALUES(35,35,'customer','proxy','none');
INSERT INTO admin_gui_virtual_services VALUES(36,36,'internal','application','none');
INSERT INTO admin_gui_virtual_services VALUES(37,37,'customer','application','none');
INSERT INTO admin_gui_virtual_services VALUES(38,38,'customer','application','none');
INSERT INTO admin_gui_virtual_services VALUES(39,39,'system','application','none');
INSERT INTO admin_gui_virtual_services VALUES(40,40,'system','application','none');
DROP TABLE IF EXISTS admin_gui_virtual_additional_ip;
CREATE TABLE IF NOT EXISTS `admin_gui_virtual_additional_ip` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `virtual_id` integer NOT NULL REFERENCES `admin_gui_virtual` (`id`),
    `additional_ip` char(39) NOT NULL UNIQUE,
    `ip_active` bool
);
INSERT INTO admin_gui_virtual_additional_ip VALUES(1,1,'192.168.150.74',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(2,26,'192.168.150.75',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(3,2,'192.168.150.76',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(4,28,'192.168.150.77',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(5,3,'192.168.150.78',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(6,4,'192.168.150.79',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(7,5,'192.168.150.80',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(8,8,'192.168.150.81',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(9,6,'192.168.150.82',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(10,11,'192.168.150.83',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(11,12,'192.168.150.84',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(12,13,'192.168.150.85',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(13,15,'192.168.150.86',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(14,32,'192.168.150.87',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(15,33,'192.168.150.88',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(16,37,'192.168.150.89',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(17,38,'192.168.150.90',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(18,34,'192.168.150.91',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(19,35,'192.168.150.92',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(20,9,'192.168.150.93',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(21,36,'192.168.150.94',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(22,7,'192.168.150.95',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(23,27,'192.168.150.96',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(24,30,'192.168.150.97',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(25,31,'192.168.150.98',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(26,23,'192.168.150.99',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(27,24,'192.168.150.100',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(28,25,'192.168.150.101',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(29,10,'192.168.150.102',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(30,39,'192.168.150.103',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(31,40,'192.168.150.104',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(32,29,'192.168.150.105',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(33,16,'192.168.150.106',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(34,17,'192.168.150.107',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(35,18,'192.168.150.108',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(36,20,'192.168.150.109',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(37,21,'192.168.150.110',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(38,22,'192.168.150.111',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(39,19,'192.168.150.112',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(40,14,'192.168.150.113',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(41,1,'192.168.150.114',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(42,26,'192.168.150.115',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(43,2,'192.168.150.116',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(44,28,'192.168.150.117',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(45,3,'192.168.150.118',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(46,4,'192.168.150.119',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(47,5,'192.168.150.120',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(48,8,'192.168.150.121',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(49,6,'192.168.150.122',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(50,11,'192.168.150.123',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(51,12,'192.168.150.124',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(52,13,'192.168.150.125',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(53,15,'192.168.150.126',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(54,32,'192.168.150.127',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(55,33,'192.168.150.128',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(56,37,'192.168.150.129',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(57,38,'192.168.150.130',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(58,34,'192.168.150.131',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(59,35,'192.168.150.132',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(60,9,'192.168.150.133',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(61,36,'192.168.150.134',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(62,7,'192.168.150.135',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(63,27,'192.168.150.136',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(64,30,'192.168.150.137',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(65,31,'192.168.150.138',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(66,23,'192.168.150.139',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(67,24,'192.168.150.140',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(68,25,'192.168.150.141',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(69,10,'192.168.150.142',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(70,39,'192.168.150.143',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(71,40,'192.168.150.144',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(72,29,'192.168.150.145',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(73,16,'192.168.150.146',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(74,17,'192.168.150.147',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(75,18,'192.168.150.148',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(76,20,'192.168.150.149',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(77,21,'192.168.150.150',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(78,22,'192.168.150.151',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(79,19,'192.168.150.152',NULL);
INSERT INTO admin_gui_virtual_additional_ip VALUES(80,14,'192.168.150.153',NULL);
DROP TABLE IF EXISTS admin_gui_storage;
CREATE TABLE IF NOT EXISTS `admin_gui_storage` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `storage_name` varchar(255) NOT NULL UNIQUE,
    `primary_ip_address` char(39) UNIQUE,
    `purpose` varchar(255) NOT NULL,
    `point_of_contact` varchar(255) NOT NULL,
    `location_code` varchar(255) NOT NULL,
    `service_tag` varchar(255) NOT NULL,
    `model` varchar(255) NOT NULL,
    `status` varchar(255) NOT NULL,
    `ip_active` bool,
    `note` text NOT NULL
);
INSERT INTO admin_gui_storage VALUES(1,'seq-prd-san-ary01','192.168.100.33','SAN Storage','David Davidson','Nwr01-1-4-10','76D7AF6A7D6F1','XioTech Emprise 5000','active',NULL,'test str 1');
INSERT INTO admin_gui_storage VALUES(2,'seq-prd-san-mds01','192.168.100.50','San Fabric A','David Davidson','Nwr01-1-4-10','76D7AF6A7D6F2','Cisco MDS 9148','active',NULL,'test str 2');
INSERT INTO admin_gui_storage VALUES(3,'seq-prd-san-mds02','192.168.100.51','San Fabric B','David Davidson','Nwr01-1-4-10','76D7AF6A7D6F3','Cisco MDS 9148','active',NULL,'test str 3');
DROP TABLE IF EXISTS admin_gui_storage_additional_ip;
CREATE TABLE IF NOT EXISTS `admin_gui_storage_additional_ip` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `storage_id` integer NOT NULL REFERENCES `admin_gui_storage` (`id`),
    `additional_ip` char(39) NOT NULL UNIQUE,
    `ip_active` bool
);
INSERT INTO admin_gui_storage_additional_ip VALUES(1,1,'192.168.100.34',NULL);
INSERT INTO admin_gui_storage_additional_ip VALUES(2,2,'192.168.100.35',NULL);
INSERT INTO admin_gui_storage_additional_ip VALUES(3,3,'192.168.100.36',NULL);
INSERT INTO admin_gui_storage_additional_ip VALUES(4,1,'192.168.100.37',NULL);
INSERT INTO admin_gui_storage_additional_ip VALUES(5,2,'192.168.100.38',NULL);
INSERT INTO admin_gui_storage_additional_ip VALUES(6,3,'192.168.100.39',NULL);
DROP TABLE IF EXISTS admin_gui_storage_wire_run;
CREATE TABLE IF NOT EXISTS `admin_gui_storage_wire_run` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `storage_id` integer NOT NULL REFERENCES `admin_gui_storage` (`id`),
    `source_port` varchar(255) NOT NULL,
    `destination_name` varchar(255) NOT NULL,
    `destination_port` varchar(255) NOT NULL
);
INSERT INTO admin_gui_storage_wire_run VALUES(1,1,'7','network 01','8');
INSERT INTO admin_gui_storage_wire_run VALUES(2,1,'8','network 02','9');
INSERT INTO admin_gui_storage_wire_run VALUES(3,1,'9','network 03','10');
INSERT INTO admin_gui_storage_wire_run VALUES(4,1,'10','network 04','11');
CREATE INDEX `auth_permission_37ef4eb4` ON `auth_permission` (`content_type_id`);
CREATE INDEX `auth_group_permissions_5f412f9a` ON `auth_group_permissions` (`group_id`);
CREATE INDEX `auth_group_permissions_83d7f98b` ON `auth_group_permissions` (`permission_id`);
CREATE INDEX `auth_user_groups_6340c63c` ON `auth_user_groups` (`user_id`);
CREATE INDEX `auth_user_groups_5f412f9a` ON `auth_user_groups` (`group_id`);
CREATE INDEX `auth_user_user_permissions_6340c63c` ON `auth_user_user_permissions` (`user_id`);
CREATE INDEX `auth_user_user_permissions_83d7f98b` ON `auth_user_user_permissions` (`permission_id`);
CREATE INDEX `django_session_b7b81f0c` ON `django_session` (`expire_date`);
CREATE INDEX `django_admin_log_6340c63c` ON `django_admin_log` (`user_id`);
CREATE INDEX `django_admin_log_37ef4eb4` ON `django_admin_log` (`content_type_id`);
CREATE INDEX `admin_gui_enclosure_additional_ip_050c7fa5` ON `admin_gui_enclosure_additional_ip` (`enclosure_id`);
CREATE INDEX `admin_gui_enclosure_wire_run_050c7fa5` ON `admin_gui_enclosure_wire_run` (`enclosure_id`);
CREATE INDEX `admin_gui_physical_ce994686` ON `admin_gui_physical` (`host_enclosure_name_id`);
CREATE INDEX `admin_gui_physical_additional_ip_53c01fa8` ON `admin_gui_physical_additional_ip` (`physical_id`);
CREATE INDEX `admin_gui_physical_wire_run_53c01fa8` ON `admin_gui_physical_wire_run` (`physical_id`);
CREATE INDEX `admin_gui_virtual_41f681ce` ON `admin_gui_virtual` (`host_physical_name_id`);
CREATE INDEX `admin_gui_virtual_additional_ip_a7394ed7` ON `admin_gui_virtual_additional_ip` (`virtual_id`);
CREATE INDEX `admin_gui_storage_additional_ip_616f040b` ON `admin_gui_storage_additional_ip` (`storage_id`);
CREATE INDEX `admin_gui_storage_wire_run_616f040b` ON `admin_gui_storage_wire_run` (`storage_id`);
