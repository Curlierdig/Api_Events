-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-03-2025 a las 05:39:49
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `events_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tevents`
--

CREATE TABLE `tevents` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `type_id` int(11) NOT NULL,
  `budget` decimal(10,2) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `location_id` int(11) NOT NULL,
  `organizer_id` int(11) NOT NULL,
  `featured` tinyint(1) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tevent_types`
--

CREATE TABLE `tevent_types` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tevent_types`
--

INSERT INTO `tevent_types` (`id`, `name`) VALUES
(1, 'Concert'),
(3, 'Conference'),
(8, 'Cultural'),
(10, 'Educational'),
(4, 'Exhibition'),
(2, 'Festival'),
(9, 'Gastronomic'),
(5, 'Party'),
(7, 'Sports'),
(6, 'Theater');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tlocations`
--

CREATE TABLE `tlocations` (
  `id` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `lat` decimal(10,8) NOT NULL,
  `lng` decimal(11,8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `torganizers`
--

CREATE TABLE `torganizers` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `logo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tevents`
--
ALTER TABLE `tevents`
  ADD PRIMARY KEY (`id`),
  ADD KEY `location_id` (`location_id`),
  ADD KEY `organizer_id` (`organizer_id`),
  ADD KEY `idx_date` (`date`),
  ADD KEY `idx_type` (`type_id`),
  ADD KEY `idx_featured` (`featured`);

--
-- Indices de la tabla `tevent_types`
--
ALTER TABLE `tevent_types`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `tlocations`
--
ALTER TABLE `tlocations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `torganizers`
--
ALTER TABLE `torganizers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tevents`
--
ALTER TABLE `tevents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tevent_types`
--
ALTER TABLE `tevent_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `tlocations`
--
ALTER TABLE `tlocations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `torganizers`
--
ALTER TABLE `torganizers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tevents`
--
ALTER TABLE `tevents`
  ADD CONSTRAINT `tevents_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `tevent_types` (`id`),
  ADD CONSTRAINT `tevents_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `tlocations` (`id`),
  ADD CONSTRAINT `tevents_ibfk_3` FOREIGN KEY (`organizer_id`) REFERENCES `torganizers` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
