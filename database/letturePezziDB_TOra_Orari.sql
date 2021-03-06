CREATE DATABASE  IF NOT EXISTS `letturePezziDB` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `letturePezziDB`;
-- MySQL dump 10.13  Distrib 5.5.53, for debian-linux-gnu (x86_64)
--
-- Host: 192.168.1.10    Database: letturePezziDB
-- ------------------------------------------------------
-- Server version	5.5.52-0+deb8u1

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
-- Table structure for table `TOra_Orari`
--

DROP TABLE IF EXISTS `TOra_Orari`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TOra_Orari` (
  `iOraId` int(11) NOT NULL AUTO_INCREMENT,
  `tOraIni` time NOT NULL,
  `tOraFine` time NOT NULL,
  `fOraTotPezzi` float DEFAULT NULL,
  PRIMARY KEY (`iOraId`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TOra_Orari`
--

LOCK TABLES `TOra_Orari` WRITE;
/*!40000 ALTER TABLE `TOra_Orari` DISABLE KEYS */;
INSERT INTO `TOra_Orari` VALUES (1,'07:00:00','08:00:00',54),(2,'08:00:00','09:00:00',5),(3,'09:00:00','10:00:00',52),(4,'10:00:00','11:00:00',49),(5,'11:00:00','12:00:00',48),(6,'12:00:00','13:00:00',55),(7,'13:00:00','14:00:00',5),(8,'14:00:00','15:00:00',52),(9,'15:00:00','16:00:00',51),(10,'16:00:00','17:00:00',5),(11,'17:00:00','18:00:00',47),(12,'18:00:00','19:00:00',48),(13,'19:00:00','20:00:00',50),(14,'20:00:00','21:00:00',60),(28,'21:00:00','22:00:00',10);
/*!40000 ALTER TABLE `TOra_Orari` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-27 15:53:53
