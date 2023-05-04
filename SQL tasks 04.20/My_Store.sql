-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 27, 2023 at 09:41 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python course`
--

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `Category_ID` int(11) NOT NULL,
  `Category` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`Category_ID`, `Category`) VALUES
(1, 'portable computers'),
(2, 'PCs'),
(3, 'software'),
(4, 'accessories');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `Customer_ID` int(11) NOT NULL,
  `Customer_Name` text NOT NULL,
  `Customer_Surname` text NOT NULL,
  `Customer_Email` text NOT NULL,
  `Customer_Tel_no` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`Customer_ID`, `Customer_Name`, `Customer_Surname`, `Customer_Email`, `Customer_Tel_no`) VALUES
(1, 'Linda', 'Krope', 'lindak@gmaill.com', '+3706577778'),
(2, 'Julija Marija', 'Garne', 'jmarijabara@gmaill.com', '+3706888333'),
(3, 'Juozas', 'Kaselis', 'juozas.kaselis@hottmail.com', '+3706003554'),
(4, 'Mira', 'Gures', 'm.gures@gmail.com', '+3706886612'),
(5, 'Marek', 'Marton', 'mmarton@gmail.com', '+3706744352'),
(6, 'Joshua', 'Pabiedas', 'J.pabiedas@gmail.com', '+3706434321');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `Order_ID` int(11) NOT NULL,
  `Customer_ID` int(11) NOT NULL,
  `Product_ID` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL,
  `order_status_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`Order_ID`, `Customer_ID`, `Product_ID`, `Quantity`, `order_status_ID`) VALUES
(1, 3, 2, 5, 3),
(2, 1, 1, 1, 5),
(3, 2, 3, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `order_status`
--

CREATE TABLE `order_status` (
  `Order_status_ID` int(11) NOT NULL,
  `Order_Status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_status`
--

INSERT INTO `order_status` (`Order_status_ID`, `Order_Status`) VALUES
(1, 'entered'),
(2, 'in processing'),
(3, 'canceled'),
(4, 'delivered'),
(5, 'paid(done)');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `Product_ID` int(11) NOT NULL,
  `P_Name` text NOT NULL,
  `Description` text NOT NULL,
  `Price` decimal(10,0) NOT NULL,
  `Warranty` int(10) NOT NULL,
  `Supplier_ID` int(11) NOT NULL,
  `Category_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`Product_ID`, `P_Name`, `Description`, `Price`, `Warranty`, `Supplier_ID`, `Category_ID`) VALUES
(1, 'LENOVO THINKBOOK 14 G3 ACL 14 FHD AMD R5 5500U', 'Lenovo ThinkBook 14 G3 ACL Grey, 14 \", IPS, FHD, 1920 x 1080, Anti-glare, AMD Ryzen 5, 5500U, 8 GB, SSD', 800, 2, 1, 1),
(2, 'KLAVIATŪRA DELL 580-18366 EN, LAIDINĖ', 'Įrenginio sąsaja: USB |Žaidimo leidimas: Ne |Šviesos diodų indikatoriai: Taip |Klaviatūros stilius: Straight |Rekomenduojamas naudojimas: Universal |Gaminio spalva:Juoda |Foninis apšvietimas: Ne', 40, 1, 4, 4),
(3, 'KOMPIUTERIS APPLE IMAC DESKTOP PC, AIO, APPLE M1', 'Apple iMac Desktop PC, AIO, Apple M1, 24\", Internal memory 8GB, SSD 256GB, Apple M1 7-core GPU, No optical drive, Keyboard language Swedish, MacOS Big Sur, Silver, 4.5K, Retina', 1500, 2, 2, 2),
(4, 'OPERACINĖ SISTEMA MICROSOFT WINDOWS 10 PRO', 'Ruošinio tipas: DVD|Minimalūs „DirectX“ reikalavimai: 9.0|Minimali procesoriaus sparta: 1 GHz|Licencijos rūšis: OEM|Kalbos versija: English|Minimalus operatyviosios atminties kiekis: 2 GB|Minimalios ekrano raiškos reikalavimai: 800 x 600', 200, 2, 3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `Supplier_ID` int(11) NOT NULL,
  `Supplier_Name` text NOT NULL,
  `Supplie_Contact` text NOT NULL,
  `Supplier_email` text NOT NULL,
  `Supplier_tel_no` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`Supplier_ID`, `Supplier_Name`, `Supplie_Contact`, `Supplier_email`, `Supplier_tel_no`) VALUES
(1, 'NAME_IT', 'Sera Pinas', 'name_it@.com', '+3706111222'),
(2, 'HANA', 'Marius Bara', 'HANA@.com', '+3706555432'),
(3, 'MAX', 'Robe Petra', 'MAX@.com', '+3706779934'),
(4, 'YOO', 'Julius Naunas', 'YOO@com', '+3706758499');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`Category_ID`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`Customer_ID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD KEY `Customer_ID` (`Customer_ID`,`Product_ID`),
  ADD KEY `order_status_ID` (`order_status_ID`),
  ADD KEY `Product_ID` (`Product_ID`);

--
-- Indexes for table `order_status`
--
ALTER TABLE `order_status`
  ADD PRIMARY KEY (`Order_status_ID`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`Product_ID`),
  ADD KEY `Supplier_ID` (`Supplier_ID`),
  ADD KEY `Category_ID` (`Category_ID`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`Supplier_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `Category_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `Customer_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `order_status`
--
ALTER TABLE `order_status`
  MODIFY `Order_status_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `Product_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `Supplier_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `customers` (`Customer_ID`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`order_status_ID`) REFERENCES `order_status` (`Order_status_ID`),
  ADD CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`Product_ID`) REFERENCES `products` (`Product_ID`);

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`Supplier_ID`) REFERENCES `suppliers` (`Supplier_ID`),
  ADD CONSTRAINT `products_ibfk_2` FOREIGN KEY (`Category_ID`) REFERENCES `categories` (`Category_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
