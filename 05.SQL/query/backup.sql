-- MySQL dump 10.13  Distrib 9.3.0, for Win64 (x86_64)
--
-- Host: localhost    Database: zerobase
-- ------------------------------------------------------
-- Server version	9.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `celeb`
--

DROP TABLE IF EXISTS `celeb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `celeb` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NAME` varchar(32) NOT NULL DEFAULT '',
  `BIRTHDAY` date DEFAULT NULL,
  `AGE` int DEFAULT NULL,
  `SEX` char(1) DEFAULT NULL,
  `JOB_TITLE` varchar(32) DEFAULT NULL,
  `AGENCY` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `celeb`
--

LOCK TABLES `celeb` WRITE;
/*!40000 ALTER TABLE `celeb` DISABLE KEYS */;
INSERT INTO `celeb` VALUES (1,'윤서연','2003-08-06',21,'F','리더, 댄스','KRE'),(2,'정혜린','2007-04-12',18,'M','보컬, 댄스','KRE'),(3,'이지우','2005-10-24',19,'F','보컬','KRE'),(4,'김채연','2004-12-04',20,'M','보컬','AAA'),(5,'김유연','2001-02-09',24,'F','리더, 센터','AAA'),(6,'김수민','2007-10-03',17,'M','보컬','KRE'),(7,'김나경','2002-10-13',22,'F','보컬, 래퍼','AAA'),(8,'공유빈','2005-02-03',20,'M','보컬, 댄스','AAA'),(9,'카에데','2005-12-20',19,'F','보컬, 댄스','LOVE'),(10,'서다현','2003-01-08',22,'M','리더, 보컬','EVOL'),(11,'코토네','2004-03-10',21,'F','래퍼','EVOL'),(12,'곽연지','2008-01-08',17,'M','보컬','EVOL'),(13,'니엔','2003-06-02',22,'F','보컬','LOVE'),(14,'박소현','2002-10-13',22,'M','래퍼, 댄스','LOVE'),(15,'신위','2004-05-25',21,'F','래퍼, 댄스','EVOL'),(16,'마유','2002-05-12',23,'M','보컬, 댄스','EVOL'),(17,'린','2006-04-12',19,'F','보컬','NEXT'),(18,'주빈','2009-01-16',16,'M','댄스','NEXT'),(19,'하연','2007-08-01',17,'F','래퍼','NEXT'),(20,'박시온','2006-04-03',19,'M','보컬','NEXT'),(21,'김채원','2007-05-02',18,'F','보컬','GLOW'),(22,'설린','2007-12-13',17,'M','보컬','GLOW'),(23,'서아','2010-06-11',15,'F','보컬','GLOW'),(24,'지연','2008-02-13',17,'M','보컬, 댄스','GLOW');
/*!40000 ALTER TABLE `celeb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `id` int DEFAULT NULL,
  `name` varchar(16) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `sex` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (1,'윤서연',43,'F'),(2,'정혜린',48,'M'),(3,'이지우',37,'F'),(4,'김채연',33,'M');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `snl_show`
--

DROP TABLE IF EXISTS `snl_show`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `snl_show` (
  `id` int NOT NULL AUTO_INCREMENT,
  `season` int NOT NULL,
  `episode` int NOT NULL,
  `broadcast_date` date DEFAULT NULL,
  `host` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `snl_show`
--

LOCK TABLES `snl_show` WRITE;
/*!40000 ALTER TABLE `snl_show` DISABLE KEYS */;
INSERT INTO `snl_show` VALUES (1,8,7,'2020-09-05','윤서연'),(2,8,8,'2020-09-12','정혜린'),(3,8,9,'2020-09-19','이지우'),(4,8,10,'2020-09-26','김채연'),(5,9,1,'2021-09-04','김유연'),(6,9,2,'2021-09-11','윤아'),(7,9,3,'2021-09-18','민주'),(8,9,4,'2021-09-25','모카'),(9,9,5,'2021-10-02','원희'),(10,9,6,'2021-10-09','이로하');
/*!40000 ALTER TABLE `snl_show` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test1`
--

DROP TABLE IF EXISTS `test1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test1` (
  `no` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test1`
--

LOCK TABLES `test1` WRITE;
/*!40000 ALTER TABLE `test1` DISABLE KEYS */;
INSERT INTO `test1` VALUES (1),(2),(3);
/*!40000 ALTER TABLE `test1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test2`
--

DROP TABLE IF EXISTS `test2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test2` (
  `no` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test2`
--

LOCK TABLES `test2` WRITE;
/*!40000 ALTER TABLE `test2` DISABLE KEYS */;
INSERT INTO `test2` VALUES (4),(5),(6),(3);
/*!40000 ALTER TABLE `test2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-14 23:22:23
