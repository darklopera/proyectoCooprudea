-- MySQL dump 10.16  Distrib 10.1.28-MariaDB, for Win32 (AMD64)
--
-- Host: localhost    Database: libreriamovil
-- ------------------------------------------------------
-- Server version	10.1.28-MariaDB

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
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categorias` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Imagen_Path` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Estado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (1,'GENERAL','IMAGEN1',1),(2,'JUVENIL','IMAGEN2',1),(3,'DERECHO','IMAGEN3',1),(4,'NOVEDADES','IMAGEN4',1);
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra`
--

DROP TABLE IF EXISTS `compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `compra` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Id_Codigo_Usuario` int(50) NOT NULL,
  `Id_Estado_Compra` int(50) NOT NULL,
  `Fecha` date NOT NULL,
  PRIMARY KEY (`Codigo`),
  KEY `Id_Estado_Compra` (`Id_Estado_Compra`),
  KEY `Id_Usuario` (`Id_Codigo_Usuario`),
  CONSTRAINT `compra_ibfk_2` FOREIGN KEY (`Id_Estado_Compra`) REFERENCES `estado_compra` (`Codigo`),
  CONSTRAINT `compra_ibfk_3` FOREIGN KEY (`Id_Codigo_Usuario`) REFERENCES `usuarios` (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra`
--

LOCK TABLES `compra` WRITE;
/*!40000 ALTER TABLE `compra` DISABLE KEYS */;
INSERT INTO `compra` VALUES (1,1,3,'2017-12-09'),(2,2,2,'2017-12-06'),(3,1,2,'2017-11-01'),(4,2,3,'2017-11-01'),(5,1,1,'2017-11-01'),(6,2,1,'2017-10-30'),(7,7,2,'2018-03-01'),(8,7,1,'2018-01-18'),(9,6,2,'2018-01-19'),(10,6,1,'2018-01-23');
/*!40000 ALTER TABLE `compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deseos`
--

DROP TABLE IF EXISTS `deseos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deseos` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Id_Codigo_Producto` int(50) NOT NULL,
  `Id_Codigo_Usuario` int(50) NOT NULL,
  `Fecha_Creado` date NOT NULL,
  `Id_Estado_Deseos` int(50) NOT NULL,
  `Cantidad` int(50) NOT NULL,
  PRIMARY KEY (`Codigo`),
  KEY `Id_Estado_Deseos` (`Id_Estado_Deseos`),
  KEY `Id_Codigo_Producto` (`Id_Codigo_Producto`),
  KEY `Id_Codigo_Usuario` (`Id_Codigo_Usuario`),
  CONSTRAINT `deseos_ibfk_3` FOREIGN KEY (`Id_Estado_Deseos`) REFERENCES `estado_deseo` (`Codigo`),
  CONSTRAINT `deseos_ibfk_4` FOREIGN KEY (`Id_Codigo_Producto`) REFERENCES `productos` (`Codigo`),
  CONSTRAINT `deseos_ibfk_5` FOREIGN KEY (`Id_Codigo_Usuario`) REFERENCES `usuarios` (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deseos`
--

LOCK TABLES `deseos` WRITE;
/*!40000 ALTER TABLE `deseos` DISABLE KEYS */;
INSERT INTO `deseos` VALUES (1,1,1,'2017-12-01',2,2),(2,2,2,'2017-12-05',1,2),(3,4,1,'2017-12-01',2,3),(4,6,2,'2017-12-06',1,7),(5,7,1,'2017-11-30',2,2),(6,8,2,'2017-11-27',1,4),(7,9,1,'2017-11-26',3,2),(8,12,1,'2017-12-09',1,1),(9,10,2,'2017-12-11',1,1),(19,8,1,'2017-12-21',1,3),(22,13,1,'2017-12-13',1,2),(23,8,1,'2017-12-13',1,1),(24,13,7,'2018-01-19',1,1),(25,10,7,'2018-01-23',1,3),(26,9,7,'2018-01-23',1,3);
/*!40000 ALTER TABLE `deseos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editorial`
--

DROP TABLE IF EXISTS `editorial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `editorial` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editorial`
--

LOCK TABLES `editorial` WRITE;
/*!40000 ALTER TABLE `editorial` DISABLE KEYS */;
INSERT INTO `editorial` VALUES (1,'No Disponible'),(2,'Legis'),(3,'Universidad de Antioquia');
/*!40000 ALTER TABLE `editorial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_compra`
--

DROP TABLE IF EXISTS `estado_compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estado_compra` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `Descripcion` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_compra`
--

LOCK TABLES `estado_compra` WRITE;
/*!40000 ALTER TABLE `estado_compra` DISABLE KEYS */;
INSERT INTO `estado_compra` VALUES (1,'Activa','En ejecuion'),(2,'Completada','Se confirmo el pago'),(3,'Cancelada','Bloqueo de usuario');
/*!40000 ALTER TABLE `estado_compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_deseo`
--

DROP TABLE IF EXISTS `estado_deseo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estado_deseo` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Descripcion` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_deseo`
--

LOCK TABLES `estado_deseo` WRITE;
/*!40000 ALTER TABLE `estado_deseo` DISABLE KEYS */;
INSERT INTO `estado_deseo` VALUES (1,'Activo','Agregado a la lista'),(2,'Inactivo','Retirado de la lista'),(3,'Cancelado','retirado por disponible');
/*!40000 ALTER TABLE `estado_deseo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_libros`
--

DROP TABLE IF EXISTS `estado_libros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estado_libros` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `Descripcion` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_libros`
--

LOCK TABLES `estado_libros` WRITE;
/*!40000 ALTER TABLE `estado_libros` DISABLE KEYS */;
INSERT INTO `estado_libros` VALUES (1,'Activo','Vendible'),(2,'Inactivo','Descontinuado'),(3,'No Disponible','Agotado');
/*!40000 ALTER TABLE `estado_libros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_usuario`
--

DROP TABLE IF EXISTS `estado_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estado_usuario` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Descripcion` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_usuario`
--

LOCK TABLES `estado_usuario` WRITE;
/*!40000 ALTER TABLE `estado_usuario` DISABLE KEYS */;
INSERT INTO `estado_usuario` VALUES (1,'Activo','Puede acceder'),(2,'Bloqueado','Mala configuracion'),(3,'Retirado','retiro por administrador');
/*!40000 ALTER TABLE `estado_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Referencia` varchar(20) CHARACTER SET armscii8 COLLATE armscii8_bin NOT NULL,
  `Titulo` varchar(50) CHARACTER SET armscii8 COLLATE armscii8_bin NOT NULL,
  `Autor` varchar(50) CHARACTER SET armscii8 COLLATE armscii8_bin NOT NULL,
  `Id_Categoria` int(20) NOT NULL,
  `Id_Editorial` int(20) NOT NULL,
  `Costo` int(20) NOT NULL,
  `Precio` int(20) NOT NULL,
  `Cantidad` int(10) NOT NULL,
  `Id_Estado_Producto` int(20) NOT NULL,
  `Imagen_Path` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`Codigo`),
  KEY `Id_Categoria` (`Id_Categoria`),
  KEY `Id_Estado_Libro` (`Id_Estado_Producto`),
  KEY `Id_Editorial` (`Id_Editorial`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`Id_Categoria`) REFERENCES `categorias` (`Codigo`),
  CONSTRAINT `productos_ibfk_3` FOREIGN KEY (`Id_Estado_Producto`) REFERENCES `estado_libros` (`Codigo`),
  CONSTRAINT `productos_ibfk_4` FOREIGN KEY (`Id_Editorial`) REFERENCES `editorial` (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'9771657988003050','LE MONDE DIPLOMATIQUE # 164','NO DISPONIBLE',1,1,7000,9000,3,1,'Imagen1'),(2,'9770120712071600','EDUCACION Y CULTURA # 106','CRISTIAN',2,2,5000,10000,5,1,'IMAGEN 2'),(4,'9770120236009280','LA CASA','ANDRES',3,3,6000,12000,0,3,'IMAGEN3'),(6,'978958870911601','EL CARRO','CAMILO',3,3,8000,10000,2,1,'IMAGEN4'),(7,'978958870911602','EL TARRO','YEIFER',3,3,12000,12001,4,2,'IMAGEN5'),(8,'978958870911603','EL AVION','CASTRO',2,2,5000,30000,2,1,'IMAGEN6'),(9,'978958870911604','POSILLO','ANDRES',1,1,500,2000,1,1,'IMAGEN7'),(10,'978958870911604','MOUSE','CRISTIAN',1,1,2000,50000,2,1,'IMAGEN8'),(11,'1','CANDELA','YO',2,2,400,30000,3,1,'IMAGEN9'),(12,'2','VASO','RELOJ',3,3,20000,100000,2,1,'IMAGEN10'),(13,'3','SERVILLETA','ALEXANDER',2,2,100,500,1,1,'IMAGEN11');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productoxcompra`
--

DROP TABLE IF EXISTS `productoxcompra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productoxcompra` (
  `Id_Codigo_Compra` int(50) NOT NULL,
  `Id_Codigo_Producto` int(50) NOT NULL,
  `Cantidad` int(50) NOT NULL,
  `Estado` tinyint(1) DEFAULT NULL,
  KEY `Id_Codigo_Compra` (`Id_Codigo_Compra`),
  KEY `Id_Codigo_Producto` (`Id_Codigo_Producto`),
  CONSTRAINT `productoxcompra_ibfk_1` FOREIGN KEY (`Id_Codigo_Compra`) REFERENCES `compra` (`Codigo`),
  CONSTRAINT `productoxcompra_ibfk_2` FOREIGN KEY (`Id_Codigo_Producto`) REFERENCES `productos` (`Codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productoxcompra`
--

LOCK TABLES `productoxcompra` WRITE;
/*!40000 ALTER TABLE `productoxcompra` DISABLE KEYS */;
INSERT INTO `productoxcompra` VALUES (5,1,2,0),(5,4,1,1),(6,2,4,1),(5,7,6,0),(5,8,4,0),(6,6,2,0),(5,9,3,1),(8,9,2,0),(5,12,3,1),(9,10,4,1),(5,13,3,1),(9,13,3,1),(10,13,3,1);
/*!40000 ALTER TABLE `productoxcompra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_documento`
--

DROP TABLE IF EXISTS `tipo_documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_documento` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Referencia` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_documento`
--

LOCK TABLES `tipo_documento` WRITE;
/*!40000 ALTER TABLE `tipo_documento` DISABLE KEYS */;
INSERT INTO `tipo_documento` VALUES (1,'CC','Cedula de Ciudadania'),(2,'TI','Tarjeta de Identidad'),(3,'CE','Cedula de Extranjeria');
/*!40000 ALTER TABLE `tipo_documento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `Codigo` int(20) NOT NULL AUTO_INCREMENT,
  `Usuario` varchar(50) COLLATE utf8_bin NOT NULL,
  `Contrasena` varchar(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `Nombre` varchar(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `Id_Tipo_Documento` int(50) NOT NULL,
  `Numero_Documento` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `Email` varchar(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `Numero_Celular` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `Id_Estaso_Usuario` int(50) NOT NULL,
  PRIMARY KEY (`Codigo`),
  KEY `Id_Tipo_Documento` (`Id_Tipo_Documento`),
  KEY `Id_Estaso_Usuario` (`Id_Estaso_Usuario`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`Id_Tipo_Documento`) REFERENCES `tipo_documento` (`Codigo`),
  CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`Id_Estaso_Usuario`) REFERENCES `estado_usuario` (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'lopera','lopera','Oscar Lopera',1,'123','lopera@lopera','311',1),(2,'coste','coste','Yeifer Herrera',2,'321','coste@coste','312',1),(6,'sandra','sandra','Sandra Londoño',3,'145','sandra@sandra','324',3),(7,'camilo','camilo','Camilo Lopera',1,'789','camilo@camilo','543',1);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-28 14:01:12
