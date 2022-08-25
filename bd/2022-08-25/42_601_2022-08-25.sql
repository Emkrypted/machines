-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: electronic_ticket_system
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `folios`
--

DROP TABLE IF EXISTS `folios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `folios` (
  `folio_id` int NOT NULL AUTO_INCREMENT,
  `used_id` int DEFAULT NULL,
  `folio` int NOT NULL,
  `superior_range` int DEFAULT NULL,
  `inferior_range` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `rsapk_m` text,
  `rsapk_e` text,
  `idk` int DEFAULT NULL,
  `frma` text,
  `caf` text NOT NULL,
  PRIMARY KEY (`folio_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `folios`
--

LOCK TABLES `folios` WRITE;
/*!40000 ALTER TABLE `folios` DISABLE KEYS */;
/*!40000 ALTER TABLE `folios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `processed_tickets`
--

DROP TABLE IF EXISTS `processed_tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `processed_tickets` (
  `processed_ticket_id` int NOT NULL AUTO_INCREMENT,
  `branch_office_id` int DEFAULT NULL,
  `cashier_id` int DEFAULT NULL,
  `track_id` int DEFAULT NULL,
  `dte_code` int DEFAULT NULL,
  `folio` int DEFAULT NULL,
  `cash_gross_amount` int DEFAULT NULL,
  `cash_net_amount` int DEFAULT NULL,
  `card_gross_amount` int DEFAULT NULL,
  `card_net_amount` int DEFAULT NULL,
  `ticket_serial_number` varchar(150) DEFAULT NULL,
  `ticket_hour` varchar(150) DEFAULT NULL,
  `ticket_transaction_number` varchar(150) DEFAULT NULL,
  `ticket_dispenser_number` varchar(150) DEFAULT NULL,
  `ticket_number` varchar(150) DEFAULT NULL,
  `ticket_station_number` varchar(150) DEFAULT NULL,
  `ticket_sa` varchar(150) DEFAULT NULL,
  `ticket_correlative` varchar(150) DEFAULT NULL,
  `entrance_hour` varchar(150) DEFAULT NULL,
  `exit_hour` varchar(150) DEFAULT NULL,
  `item_quantity` int DEFAULT NULL,
  `sii_status` varchar(150) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`processed_ticket_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `processed_tickets`
--

LOCK TABLES `processed_tickets` WRITE;
/*!40000 ALTER TABLE `processed_tickets` DISABLE KEYS */;
/*!40000 ALTER TABLE `processed_tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `settings`
--

DROP TABLE IF EXISTS `settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `settings` (
  `setting_id` int NOT NULL,
  `branch_office_id` int DEFAULT NULL,
  `cashier_id` int DEFAULT NULL,
  `dte_code` int DEFAULT NULL,
  `description` text NOT NULL,
  `api_token` text NOT NULL,
  `libredte_hash` text NOT NULL,
  `url_company_rut` varchar(100) NOT NULL,
  `username_credential` varchar(50) NOT NULL,
  `password_credential` varchar(50) NOT NULL,
  `rut` varchar(100) NOT NULL,
  `cert_data` text NOT NULL,
  `pkey_data` text NOT NULL,
  `resolution_date` date DEFAULT NULL,
  `resolution_number` varchar(100) NOT NULL,
  `sequence` varchar(100) NOT NULL,
  `document_type` varchar(100) NOT NULL,
  `document_tax` varchar(100) NOT NULL,
  `bearer` text NOT NULL,
  `CAFRE` varchar(100) NOT NULL,
  `CAFRS` varchar(100) NOT NULL,
  `CAFTD` varchar(39) NOT NULL,
  `RSAPKM` varchar(200) NOT NULL,
  `RSAPKE` varchar(100) NOT NULL,
  `IDK` varchar(100) NOT NULL,
  `FRMA` varchar(200) NOT NULL,
  `RSASK` text NOT NULL,
  `RSAPUBK` text NOT NULL,
  `GiroEmis` varchar(200) NOT NULL,
  `Acteco` varchar(100) NOT NULL,
  `DirOrigen` varchar(100) NOT NULL,
  `CmnaOrigen` varchar(100) NOT NULL,
  `RUTRecep` varchar(100) NOT NULL,
  `RznSocRecep` varchar(100) NOT NULL,
  `GiroRecep` varchar(100) NOT NULL,
  `DirRecep` varchar(100) NOT NULL,
  `CmnaRecep` varchar(100) NOT NULL,
  `NmbItem` varchar(100) NOT NULL,
  `folio_quantity` bigint NOT NULL,
  `tax_value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `settings`
--

LOCK TABLES `settings` WRITE;
/*!40000 ALTER TABLE `settings` DISABLE KEYS */;
INSERT INTO `settings` VALUES (1,42,601,76063822,'2Pago de Estacionamiento - Tottus Catedral','AtWYamNvDOfgDOEY6UbXgvGqDiRPR7QOt9Si1hbeMmat4g2Qfxzg7LlT5yzNz5LOozQbcA9uibaSTu4t','JXou3uyrc7sNnP2ewOCX38tWZ6BTm4D1','76063822','rcabezas','Jisparking2018','76063822-6','-----BEGIN CERTIFICATE-----\\nMIIGjjCCBXagAwIBAgIDAR4jMA0GCSqGSIb3DQEBCwUAMIGmMQswCQYDVQQGEwJD\\nTDEYMBYGA1UEChMPQWNlcHRhLmNvbSBTLkEuMUgwRgYDVQQDEz9BY2VwdGEuY29t\\nIEF1dG9yaWRhZCBDZXJ0aWZpY2Fkb3JhIENsYXNlIDMgUGVyc29uYSBOYXR1cmFs\\nIC0gRzQxHjAcBgkqhkiG9w0BCQEWD2luZm9AYWNlcHRhLmNvbTETMBEGA1UEBRMK\\nOTY5MTkwNTAtODAeFw0yMTA3MDgyMzQwMjZaFw0yNDA3MDgyMzQwMjZaMIGXMQsw\\nCQYDVQQGEwJDTDEYMBYGA1UEDBMPUEVSU09OQSBOQVRVUkFMMSswKQYDVQQDEyJN\\nQVJDRUxPIEFMRUpBTkRSTyBJTlpVTlpBIEdPTlpBTEVaMSwwKgYJKoZIhvcNAQkB\\nFh1DUklTVElBTklOWlVOWkFASklTUEFSS0lORy5DTDETMBEGA1UEBRMKMTAwMzM3\\nNDEtSzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK/zoDtqd7+qB7aX\\njS/kiBnLOf62orrMMdL3G22l0NJBziWVv/DezIgoFONUEF2XNXBWNAKTbLABvGIZ\\nNFLyE4QuevdLd5AXuOt0q4+Y2msZemrP3zIkuT1dkNo/djj5gmFY3hC1i9DEj2ZQ\\nF3kwcN9rrhQrzg3I0ixrRfdozMIypvCY4pWoJOvaNc8Z1a2Brq09QXQ3zUB3jXW7\\nezxQlOCqv6G37UB9FzInnwAmicz5/92YtvFAXXJd4dtuaoPQt7Hn8XzhP8wmtj9j\\nE9uHUbzK4CmQm4bYb1hmceg4crTHybTLUHngSlfI7QbDsLroaUlNgq8Kte8qDNxg\\nqAhLkW0CAwEAAaOCAtAwggLMMB8GA1UdIwQYMBaAFKr9vcXpN032mU1XjsFxGvnr\\nwwbjMB0GA1UdDgQWBBQYpMku0lGJKNQdxadkxl0mirm7uTALBgNVHQ8EBAMCBPAw\\nHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMEMBEGCWCGSAGG+EIBAQQEAwIF\\noDCB+gYDVR0gBIHyMIHvMIHsBggrBgEEAbVrAjCB3zAxBggrBgEFBQcCARYlaHR0\\ncHM6Ly9hY2c0LmFjZXB0YS5jb20vQ1BTLUFjZXB0YWNvbTCBqQYIKwYBBQUHAgIw\\ngZwwFhYPQWNlcHRhLmNvbSBTLkEuMAMCAQIagYFFbCB0aXR1bGFyIGhhIHNpZG8g\\ndmFsaWRhZG8gZW4gZm9ybWEgcHJlc2VuY2lhbCwgcXVlZGFuZG8gaGFiaWxpdGFk\\nbyBlbCBDZXJ0aWZpY2FkbyBwYXJhIHVzbyB0cmlidXRhcmlvLCBwYWdvcywgY29t\\nZXJjaW8geSBvdHJvcy4wWgYDVR0SBFMwUaAYBggrBgEEAcEBAqAMFgo5NjkxOTA1\\nMC04oCQGCCsGAQUFBwgDoBgwFgwKOTY5MTkwNTAtOAYIKwYBBAHBAQKBD2luZm9A\\nYWNlcHRhLmNvbTBoBgNVHREEYTBfoBgGCCsGAQQBwQEBoAwWCjEwMDMzNzQxLUug\\nJAYIKwYBBQUHCAOgGDAWDAoxMDAzMzc0MS1LBggrBgEEAcEBAoEdQ1JJU1RJQU5J\\nTlpVTlpBQEpJU1BBUktJTkcuQ0wwRwYIKwYBBQUHAQEEOzA5MDcGCCsGAQUFBzAB\\nhitodHRwczovL2FjZzQuYWNlcHRhLmNvbS9hY2c0L29jc3AvQ2xhc2UzLUc0MD8G\\nA1UdHwQ4MDYwNKAyoDCGLmh0dHBzOi8vYWNnNC5hY2VwdGEuY29tL2FjZzQvY3Js\\nL0NsYXNlMy1HNC5jcmwwDQYJKoZIhvcNAQELBQADggEBAAyvyBRFLpuF947AuBDm\\nllTVh2Txrn2TK8bCl0iljnaCOdG3idmE5x9Ta7anzV0fL+ujQrUsSd7fa1n4PN9a\\nn5rBmC/HR1DhBm4WIoVbVy3oz1GT2bmnfLOBqNKMvFNX0MJoOwYIkPxUcwRZXoPe\\n6qe4tp4LAQiIUSxIbtVflXrctqX9m8PYf5wNA8gkiKK4qp8h+d+ZySAEHVFlHWb8\\nY6TznjIwY05T46ATEyOVagDSijwW1Nj8m/8eJTF0vDKIzW6Uaa7YIPzVnkV0IHyE\\nTyRne1CdJvynaEgs/BX84I1ovtsH2iEDX83xmKxtrdtPgO+Qin0kqHEu1EaEj9Qt\\n6L0=\\n-----END CERTIFICATE-----','-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCv86A7ane/qge2\\nl40v5IgZyzn+tqK6zDHS9xttpdDSQc4llb/w3syIKBTjVBBdlzVwVjQCk2ywAbxi\\nGTRS8hOELnr3S3eQF7jrdKuPmNprGXpqz98yJLk9XZDaP3Y4+YJhWN4QtYvQxI9m\\nUBd5MHDfa64UK84NyNIsa0X3aMzCMqbwmOKVqCTr2jXPGdWtga6tPUF0N81Ad411\\nu3s8UJTgqr+ht+1AfRcyJ58AJonM+f/dmLbxQF1yXeHbbmqD0Lex5/F84T/MJrY/\\nYxPbh1G8yuApkJuG2G9YZnHoOHK0x8m0y1B54EpXyO0Gw7C66GlJTYKvCrXvKgzc\\nYKgIS5FtAgMBAAECggEBAJpWKwCzHSMD9AwX14JhBXkKqG5iqU8M+c9Bbc+6GPe1\\nPSv+tQSFigcMkXXuMQTHM9q74pc31ah1fVbXIOx45uGVG8t7aP79r/jot+wXec9j\\n49t5RyBm0g2f2wV1kS/cvJ7DItapSGDxaY+nRU/KS9fOTj3nRrEUrDbGSfMA/EqC\\nRQT8BaHNDE9HwxsPOG66CCj9Bk40lZJD1XbWTey0NdhzcFDJya9gWvNQeKnXMo20\\n9dltDvHhob2ULnbyUV3CNPsNFw/vCvqrb839ZUrBCh+IqCMrU/nrLuqmCpBIG+2/\\naiNHgE7pIhfF/QpCbDwlbIH0HxQUTdPnJvAmmwZWGIkCgYEA/xF0WM4pQCRQF+Og\\nCNdKjWkF/ZXS/tnpjxr2DmvMKwZX2nXMBHC7aHpfUCzj/Td69uK+AG4LnRkP1L3U\\nyV0kXbMGUFcofVhYTDnPPNdlNyL5n2LKEmnYAYaJyYitEGoJN2hwplDMGH8kSKBH\\nuymYN5ry5FfQfJGh17cjb/vP1s8CgYEAsJguDDB0uNC/oCEi1tSDG4RopV8tk/PH\\nbtK1Fk0Qu7NliHr+PKb9w69wiw8BZ7dDU+igqJrywXl+Tnm8CvpbOAL8qQZqMzXM\\nGvGBelWSq2HzxrIURD4X1yqzPvRKCTEbAPn4cgnmUBIpOtkdDJjrwuMD8dIT6J4y\\nqmlpYZEWYwMCgYAEw4awwejzUbpNN+sdPygdTADYo5u1Nsyt54sA6fJ+OzgY1Gpj\\nCtf1M5PkI3J+oDKjuchiqat926H4DzOSLzMmrNlJVtdiv+umQM4mDL/PL9AJsgak\\nIWXvYVvhb7QLwm85obG46XlmW7mJwbSVQkmdgD9ZFGrIaM/k/36h8MoI8QKBgD8R\\nChjmUTkTq+vXCacpW+0+21R76j4VaJrmey+MtDYkelVEf3lPtf7lr86pvDm7FDtq\\nL74nIB0Cc545EXPmNx+IyYzfspu5UbwplbEH0IqOP84tGNnKRx9bq4oHGk2wENHH\\nc/feGzdrVPgkQ6CVGFWQV39MJDoGDVgYrz7d3t3bAoGBAK+UnIFrRJ5UMsIM5Ao2\\nryKtwPemdHypIVK3WOV1yRpa5aBqemrTQkijbLx8lVxoeID8Lw4zHybK6V9mAHsf\\nRhfHsmBz3f4mYoKVoyVDelxpx+IGkGibvzNQB5BFWuu8kZeDPkhcPbk4pHFUf/jm\\nCvLdtcSmumV5hxnVdtwjdlQD\\n-----END PRIVATE KEY-----','2014-06-17','57','1','39','19','eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYWIyYWUwOGVmYjI1Y2MwMWU5ODUzOWViMDRhNjJkYzEzN2UxMDQyODRmNjY5MTNjMTAxMWM3Yzg1N2Q0NmZmNzY1NGM4NGQzYzM0YzRhMTAiLCJpYXQiOjE2NDk1Mjg4ODMsIm5iZiI6MTY0OTUyODg4MywiZXhwIjo0ODA1MjAyNDgzLCJzdWIiOiI1NzYiLCJzY29wZXMiOltdfQ.K03TeHk5geCY4NARl9UiV8SeeR6Pe4YT1E_Z_z5VLhTJwI36_780NiwxlBIE58hlX9XdjBZiVgpW3FSEYvGQo-6pv6tp9r6Yh9LB6Hi1j5YirwWQgOgPE_2kXBjtXVS84r97unEhpCGA0mGpbIJH0YNNFLYgZauoLzGjmooOYbAT6buhOG5_xTX25VhgscoaPeh_-KnbJVxpMf0YxMkDC7nE5VsI8mMloR3pOyfXpLUH5f3yjl2F8QNPtjRB25MJZnhetMozPUoDX8h5Lh5gcbYItQYtzZrU-3Cs8JMG7bu3fH74a5bej_HmLfdAP-3HP0CxOOhAY4Oppamf8zGwkvzPSeXZdPW79pZ9JEkfRFOfwuYbJA79-nawo_UiKc73HIHgGMFoR9wvfla5JDKrzTh3xoa2JsZUbMZ93iYqsurVMJt-suaqM1Lqcqa1nGZ8HovGgYeVf6RbQH1TJT-ckeGwgfor0Pi_vhhUc9Coxd9qQOAyiY_jHUVy16CQ4BlFkgsOQ9mwBuL5k4xHwNd3VBa_ktLeW36rrXSsaGXwoVLO9Bi19_-fijvrNRmAez3NTiODrMLNNLqXIk9MbUy0PWYAV1Ylq_gdJhJXEED0_iTe6MwA_OrAwVN18U0DQopKwIDLqQoRTAPlcWR1PEO5sBs3jHFclc_BaoHqfG5_W2U','76063822-6','J I S PARKING SPA','39','vVTFeioe9dBy5K59tSpr83T2pLurgbVHC9Ev1zexm7jes/KH0UqdT8KDKUoHMdYB02ws8MgQ06sCTS0nf8kFIw==','Aw==','300','L28qitCxjrvhiGviydiARvaNbwiJnsT0olqva3a3knTmKerlSYXhNUp6P51Ng48aXxF69GnGgi2lQEJ8+suqgg==','-----BEGIN RSA PRIVATE KEY-----MIIBOQIBAAJBAL1UxXoqHvXQcuSufbUqa/N09qS7q4G1RwvRL9c3sZu43rPyh9FKnU/CgylKBzHWAdNsLPDIENOrAk0tJ3/JBSMCAQMCQH44g6bGv06K90Me/njG8qJN+cMnx6vOL102H+TPy70kw43X/ja+1vX2kAQQBmMb8JSFcjhr/uhN5WWB9937sMsCIQDr92rvT7liqDXI3IuKK6tUbnQjgzkc6G+PcZdanZmnewIhAM1nw5svcvg2muJGpnNxgMSGL94Y7PWOxprDUtkVNdR5AiEAnU+cn4p7lxrOhehdBsfHjZ74F6zQvfBKX6EPkb5mb6cCIQCI79e8ykylebyW2cRM9lXYWXU+u0ijtIRnLOHmDiPi+wIgdQDW/bfVkp0e1PVThJR0eqv9iaOKsTs1Ui5D6hQz7Cs=-----END RSA PRIVATE KEY-----','-----BEGIN PUBLIC KEY-----MFowDQYJKoZIhvcNAQEBBQADSQAwRgJBAL1UxXoqHvXQcuSufbUqa/N09qS7q4G1RwvRL9c3sZu43rPyh9FKnU/CgylKBzHWAdNsLPDIENOrAk0tJ3/JBSMCAQM=-----END PUBLIC KEY-----','EXPLOTACION DE ESTACIONAMIENTOS DE VEHICULOS AUTOMOTORES Y PARQUIMETRO','522120','Matucana 40','Estacion Central','66666666-6','Cliente Generico','Particular','Santiago','Estacion Central','Venta',2,1.19);
/*!40000 ALTER TABLE `settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stored_tickets`
--

DROP TABLE IF EXISTS `stored_tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stored_tickets` (
  `stored_ticket_id` int NOT NULL AUTO_INCREMENT,
  `branch_office_id` int DEFAULT NULL,
  `cashier_id` int DEFAULT NULL,
  `dte_code` int DEFAULT NULL,
  `folio` int DEFAULT NULL,
  `cash_gross_amount` int DEFAULT NULL,
  `cash_net_amount` int DEFAULT NULL,
  `card_gross_amount` int DEFAULT NULL,
  `card_net_amount` int DEFAULT NULL,
  `ticket_serial_number` varchar(150) DEFAULT NULL,
  `ticket_hour` varchar(150) DEFAULT NULL,
  `ticket_transaction_number` varchar(150) DEFAULT NULL,
  `ticket_dispenser_number` varchar(150) DEFAULT NULL,
  `ticket_number` varchar(150) DEFAULT NULL,
  `ticket_station_number` varchar(150) DEFAULT NULL,
  `ticket_sa` varchar(150) DEFAULT NULL,
  `ticket_correlative` varchar(150) DEFAULT NULL,
  `entrance_hour` varchar(150) DEFAULT NULL,
  `exit_hour` varchar(150) DEFAULT NULL,
  `item_quantity` int DEFAULT NULL,
  `sii_status` varchar(150) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`stored_ticket_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stored_tickets`
--

LOCK TABLES `stored_tickets` WRITE;
/*!40000 ALTER TABLE `stored_tickets` DISABLE KEYS */;
/*!40000 ALTER TABLE `stored_tickets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-25 13:28:58
