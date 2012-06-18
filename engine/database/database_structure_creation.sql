DROP DATABASE IF EXISTS `linux-admin-toolkit`;

CREATE DATABASE IF NOT EXISTS `linux-admin-toolkit` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `linux-admin-toolkit`;
-- MySQL dump 10.13  Distrib 5.5.16, for Win32 (x86)
--
-- Host: localhost    Database: linux_admin_toolkit
-- ------------------------------------------------------
-- Server version	5.5.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `storage_devices`
--

DROP TABLE IF EXISTS `storage_devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storage_devices` (
  `device_name` varchar(256) NOT NULL,
  `role` varchar(256) DEFAULT NULL,
  `purpose` varchar(256) DEFAULT NULL,
  `point_of_contact` varchar(256) DEFAULT NULL,
  `primary_ip` varchar(256) DEFAULT NULL,
  `additional_ip_addresses` varchar(256) DEFAULT NULL,
  `location_code` varchar(256) DEFAULT NULL,
  `service_tag` varchar(256) DEFAULT NULL,
  `model` varchar(256) DEFAULT NULL,
  `console_link` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`device_name`),
  UNIQUE KEY `device_name_UNIQUE` (`device_name`),
  UNIQUE KEY `primary_ip_UNIQUE` (`primary_ip`),
  KEY `location_id_storage` (`location_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `physical_machine_list`
--

DROP TABLE IF EXISTS `physical_machine_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `physical_machine_list` (
  `server_name` varchar(256) NOT NULL,
  `role` varchar(256) DEFAULT NULL,
  `purpose` varchar(256) DEFAULT NULL,
  `point_of_contact` varchar(256) DEFAULT NULL,
  `primary_ip` varchar(256) DEFAULT NULL,
  `location_code` varchar(255) DEFAULT NULL,
  `enclosure_name` varchar(256) DEFAULT NULL,
  `ilo_ip` varchar(256) DEFAULT NULL,
  `console_link` varchar(256) DEFAULT NULL,
  `admin_cluster_grouping_1` varchar(256) DEFAULT NULL,
  `admin_cluster_grouping_2` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`server_name`),
  UNIQUE KEY `server_name_UNIQUE` (`server_name`),
  UNIQUE KEY `primary_ip_UNIQUE` (`primary_ip`),
  KEY `location_id` (`location_code`),
  KEY `enclosure_name` (`enclosure_name`),
  KEY `enclosure_name_physi` (`enclosure_name`),
  CONSTRAINT `enclosure_name_physi` FOREIGN KEY (`enclosure_name`) REFERENCES `physical_enclosures` (`enclosure_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `physical_enclosures`
--

DROP TABLE IF EXISTS `physical_enclosures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `physical_enclosures` (
  `enclosure_name` varchar(256) NOT NULL,
  `point_of_contact` varchar(256) DEFAULT NULL,
  `primary_ip_address` varchar(256) DEFAULT NULL,
  `additional_ip_addresses` varchar(256) DEFAULT NULL,
  `model` varchar(256) DEFAULT NULL,
  `service_tag` varchar(256) DEFAULT NULL,
  `location_code` varchar(256) DEFAULT NULL,
  `console_link` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`enclosure_name`),
  UNIQUE KEY `device_name_UNIQUE` (`enclosure_name`),
  UNIQUE KEY `primary_ip_address_UNIQUE` (`primary_ip_address`),
  KEY `location_id_enclosure` (`location_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `virtual_machine_additional_ips`
--

DROP TABLE IF EXISTS `virtual_machine_additional_ips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `virtual_machine_additional_ips` (
  `server_name` varchar(256) NOT NULL,
  `ip_address` varchar(256) DEFAULT NULL,
  `additional_hostname` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`server_name`),
  KEY `server_name_vir_add_ips` (`server_name`),
  CONSTRAINT `server_name_vir_add_ips` FOREIGN KEY (`server_name`) REFERENCES `virtual_machine_list` (`server_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `virtual_machine_details`
--

DROP TABLE IF EXISTS `virtual_machine_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `virtual_machine_details` (
  `server_name` varchar(256) NOT NULL,
  `os` varchar(256) DEFAULT NULL,
  `core_count` varchar(256) DEFAULT NULL,
  `ram` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`server_name`),
  UNIQUE KEY `server_name_UNIQUE` (`server_name`),
  KEY `server_name` (`server_name`),
  CONSTRAINT `server_name_vir_details` FOREIGN KEY (`server_name`) REFERENCES `virtual_machine_list` (`server_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `physical_machine_services`
--

DROP TABLE IF EXISTS `physical_machine_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `physical_machine_services` (
  `server_name` varchar(256) NOT NULL,
  `monitoring` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`server_name`),
  UNIQUE KEY `server_name_UNIQUE` (`server_name`),
  KEY `server_name_services` (`server_name`),
  CONSTRAINT `server_name_services` FOREIGN KEY (`server_name`) REFERENCES `physical_machine_list` (`server_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `physical_machine_details`
--

DROP TABLE IF EXISTS `physical_machine_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `physical_machine_details` (
  `server_name` varchar(256) NOT NULL,
  `service_tag` varchar(256) DEFAULT NULL,
  `model` varchar(256) DEFAULT NULL,
  `os` varchar(256) DEFAULT NULL,
  `cpu` varchar(256) DEFAULT NULL,
  `ram` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`server_name`),
  UNIQUE KEY `server_name_UNIQUE` (`server_name`),
  KEY `server_name_phy_det` (`server_name`),
  CONSTRAINT `server_name_phy_det` FOREIGN KEY (`server_name`) REFERENCES `physical_machine_list` (`server_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `physical_machine_additional_ips`
--

DROP TABLE IF EXISTS `physical_machine_additional_ips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `physical_machine_additional_ips` (
  `server_name` varchar(256) NOT NULL,
  `ip_address` varchar(256) DEFAULT NULL,
  `additional_hostname` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`server_name`),
  KEY `server_name_add_ips` (`server_name`),
  CONSTRAINT `server_name_add_ips` FOREIGN KEY (`server_name`) REFERENCES `physical_machine_list` (`server_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `virtual_machine_list`
--

DROP TABLE IF EXISTS `virtual_machine_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `virtual_machine_list` (
  `server_name` varchar(256) NOT NULL,
  `role` varchar(256) DEFAULT NULL,
  `purpose` varchar(256) DEFAULT NULL,
  `point_of_contact` varchar(256) DEFAULT NULL,
  `primary_ip` varchar(256) DEFAULT NULL,
  `host_server` varchar(256) DEFAULT NULL,
  `admin_cluster_grouping_1` varchar(256) DEFAULT NULL,
  `admin_cluster_grouping_2` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`server_name`),
  UNIQUE KEY `server_name_UNIQUE` (`server_name`),
  UNIQUE KEY `primary_ip_UNIQUE` (`primary_ip`),
  KEY `host_server_vir_list` (`host_server`),
  CONSTRAINT `host_server_vir_list` FOREIGN KEY (`host_server`) REFERENCES `physical_machine_list` (`server_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `virtual_machine_services`
--

DROP TABLE IF EXISTS `virtual_machine_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `virtual_machine_services` (
  `server_name` varchar(256) NOT NULL,
  `monitoring` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`server_name`),
  UNIQUE KEY `server_name_UNIQUE` (`server_name`),
  KEY `server_name_vir_services` (`server_name`),
  CONSTRAINT `server_name_vir_services` FOREIGN KEY (`server_name`) REFERENCES `virtual_machine_list` (`server_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-05-30 11:35:42
