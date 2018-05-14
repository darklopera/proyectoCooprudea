/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 10.1.28-MariaDB : Database - libreriamovil
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`libreriamovil` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */;

USE `libreriamovil`;

/*Table structure for table `categorias` */

DROP TABLE IF EXISTS `categorias`;

CREATE TABLE `categorias` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Imagen_Path` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `Estado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

/*Data for the table `categorias` */

insert  into `categorias`(`Codigo`,`Nombre`,`Imagen_Path`,`Estado`) values (1,'GENERAL','IMAGEN1',1),(2,'JUVENIL','IMAGEN2',1),(3,'DERECHO','IMAGEN3',1),(4,'NOVEDADES','IMAGEN4',1);

/*Table structure for table `compra` */

DROP TABLE IF EXISTS `compra`;

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

/*Data for the table `compra` */

insert  into `compra`(`Codigo`,`Id_Codigo_Usuario`,`Id_Estado_Compra`,`Fecha`) values (1,1,3,'2017-12-09'),(2,2,2,'2017-12-06'),(3,1,2,'2017-11-01'),(4,2,3,'2017-11-01'),(5,1,1,'2017-11-01'),(6,2,1,'2017-10-30'),(7,7,2,'2018-03-01'),(8,7,1,'2018-01-18'),(9,6,2,'2018-01-19'),(10,6,1,'2018-01-23');

/*Table structure for table `deseos` */

DROP TABLE IF EXISTS `deseos`;

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

/*Data for the table `deseos` */

insert  into `deseos`(`Codigo`,`Id_Codigo_Producto`,`Id_Codigo_Usuario`,`Fecha_Creado`,`Id_Estado_Deseos`,`Cantidad`) values (1,1,1,'2017-12-01',2,2),(2,2,2,'2017-12-05',1,2),(3,4,1,'2017-12-01',2,3),(4,6,2,'2017-12-06',1,7),(5,7,1,'2017-11-30',2,2),(6,8,2,'2017-11-27',1,4),(7,9,1,'2017-11-26',3,2),(8,12,1,'2017-12-09',1,1),(9,10,2,'2017-12-11',1,1),(19,8,1,'2017-12-21',1,3),(22,13,1,'2017-12-13',1,2),(23,8,1,'2017-12-13',1,1),(24,13,7,'2018-01-19',1,1),(25,10,7,'2018-01-23',1,3),(26,9,7,'2018-01-23',1,3);

/*Table structure for table `editorial` */

DROP TABLE IF EXISTS `editorial`;

CREATE TABLE `editorial` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

/*Data for the table `editorial` */

insert  into `editorial`(`Codigo`,`Nombre`) values (1,'No Disponible'),(2,'Legis'),(3,'Universidad de Antioquia');

/*Table structure for table `estado_compra` */

DROP TABLE IF EXISTS `estado_compra`;

CREATE TABLE `estado_compra` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `Descripcion` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

/*Data for the table `estado_compra` */

insert  into `estado_compra`(`Codigo`,`Nombre`,`Descripcion`) values (1,'Activa','En ejecuion'),(2,'Completada','Se confirmo el pago'),(3,'Cancelada','Bloqueo de usuario');

/*Table structure for table `estado_deseo` */

DROP TABLE IF EXISTS `estado_deseo`;

CREATE TABLE `estado_deseo` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Descripcion` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

/*Data for the table `estado_deseo` */

insert  into `estado_deseo`(`Codigo`,`Nombre`,`Descripcion`) values (1,'Activo','Agregado a la lista'),(2,'Inactivo','Retirado de la lista'),(3,'Cancelado','retirado por disponible');

/*Table structure for table `estado_libros` */

DROP TABLE IF EXISTS `estado_libros`;

CREATE TABLE `estado_libros` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `Descripcion` varchar(100) COLLATE utf8mb4_spanish_ci NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

/*Data for the table `estado_libros` */

insert  into `estado_libros`(`Codigo`,`Nombre`,`Descripcion`) values (1,'Activo','Vendible'),(2,'Inactivo','Descontinuado'),(3,'No Disponible','Agotado');

/*Table structure for table `estado_usuario` */

DROP TABLE IF EXISTS `estado_usuario`;

CREATE TABLE `estado_usuario` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Descripcion` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

/*Data for the table `estado_usuario` */

insert  into `estado_usuario`(`Codigo`,`Nombre`,`Descripcion`) values (1,'Activo','Puede acceder'),(2,'Bloqueado','Mala configuracion'),(3,'Retirado','retiro por administrador');

/*Table structure for table `productos` */

DROP TABLE IF EXISTS `productos`;

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

/*Data for the table `productos` */

insert  into `productos`(`Codigo`,`Referencia`,`Titulo`,`Autor`,`Id_Categoria`,`Id_Editorial`,`Costo`,`Precio`,`Cantidad`,`Id_Estado_Producto`,`Imagen_Path`) values (1,'9771657988003050','LE MONDE DIPLOMATIQUE # 164','NO DISPONIBLE',1,1,7000,9000,3,1,'Imagen1'),(2,'9770120712071600','EDUCACION Y CULTURA # 106','CRISTIAN',2,2,5000,10000,5,1,'IMAGEN 2'),(4,'9770120236009280','LA CASA','ANDRES',3,3,6000,12000,0,3,'IMAGEN3'),(6,'978958870911601','EL CARRO','CAMILO',3,3,8000,10000,2,1,'IMAGEN4'),(7,'978958870911602','EL TARRO','YEIFER',3,3,12000,12001,4,2,'IMAGEN5'),(8,'978958870911603','EL AVION','CASTRO',2,2,5000,30000,2,1,'IMAGEN6'),(9,'978958870911604','POSILLO','ANDRES',1,1,500,2000,1,1,'IMAGEN7'),(10,'978958870911604','MOUSE','CRISTIAN',1,1,2000,50000,2,1,'IMAGEN8'),(11,'1','CANDELA','YO',2,2,400,30000,3,1,'IMAGEN9'),(12,'2','VASO','RELOJ',3,3,20000,100000,2,1,'IMAGEN10'),(13,'3','SERVILLETA','ALEXANDER',2,2,100,500,1,1,'IMAGEN11');

/*Table structure for table `productoxcompra` */

DROP TABLE IF EXISTS `productoxcompra`;

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

/*Data for the table `productoxcompra` */

insert  into `productoxcompra`(`Id_Codigo_Compra`,`Id_Codigo_Producto`,`Cantidad`,`Estado`) values (5,1,2,0),(5,4,1,1),(6,2,4,1),(5,7,6,0),(5,8,4,0),(6,6,2,0),(5,9,3,1),(8,9,2,0),(5,12,3,1),(9,10,4,1),(5,13,3,1),(9,13,3,1),(10,13,3,1);

/*Table structure for table `tipo_documento` */

DROP TABLE IF EXISTS `tipo_documento`;

CREATE TABLE `tipo_documento` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Referencia` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `Nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

/*Data for the table `tipo_documento` */

insert  into `tipo_documento`(`Codigo`,`Referencia`,`Nombre`) values (1,'CC','Cedula de Ciudadania'),(2,'TI','Tarjeta de Identidad'),(3,'CE','Cedula de Extranjeria');

/*Table structure for table `usuarios` */

DROP TABLE IF EXISTS `usuarios`;

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

/*Data for the table `usuarios` */

insert  into `usuarios`(`Codigo`,`Usuario`,`Contrasena`,`Nombre`,`Id_Tipo_Documento`,`Numero_Documento`,`Email`,`Numero_Celular`,`Id_Estaso_Usuario`) values (1,'lopera','lopera','Oscar Lopera',1,'123','lopera@lopera','311',1),(2,'coste','coste','Yeifer Herrera',2,'321','coste@coste','312',1),(6,'sandra','sandra','Sandra Londoño',3,'145','sandra@sandra','324',3),(7,'camilo','camilo','Camilo Lopera',1,'789','camilo@camilo','543',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
