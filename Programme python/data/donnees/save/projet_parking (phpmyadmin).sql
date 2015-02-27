-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2+deb7u1
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Ven 20 Février 2015 à 01:19
-- Version du serveur: 5.5.40
-- Version de PHP: 5.4.4-14+deb7u14

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `projet_parking`
--

-- --------------------------------------------------------

--
-- Structure de la table `places`
--

CREATE TABLE IF NOT EXISTS `places` (
  `places_id` int(11) NOT NULL,
  `places_code` varchar(10) NOT NULL,
  `places_dispo` tinyint(1) NOT NULL,
  `places_predef` tinyint(1) NOT NULL,
  `places_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`places_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `places`
--

INSERT INTO `places` (`places_id`, `places_code`, `places_dispo`, `places_predef`, `places_active`) VALUES
(0, '0100b87a09', 0, 1, 1),
(1, '', 1, 0, 1),
(2, '0001f2f00', 0, 0, 1),
(3, '1111c3a56', 0, 0, 1),
(4, '', 1, 0, 1),
(5, '', 1, 0, 1),
(6, '', 1, 0, 1),
(7, '', 1, 0, 1),
(8, '', 1, 0, 1),
(9, '', 1, 0, 1),
(10, '', 1, 0, 1),
(11, '', 1, 0, 1),
(12, '', 1, 0, 0),
(13, '', 1, 0, 0),
(14, '', 1, 0, 1);

-- --------------------------------------------------------

--
-- Structure de la table `utilisation`
--

CREATE TABLE IF NOT EXISTS `utilisation` (
  `utilisation_id` int(11) NOT NULL AUTO_INCREMENT,
  `utilisation_code` varchar(10) NOT NULL,
  `utilisation_accept` tinyint(1) NOT NULL,
  `utilisation_entrantsortant` int(1) NOT NULL,
  `utilisation_place` int(2) NOT NULL,
  `utilisation_dateheure` varchar(18) NOT NULL,
  PRIMARY KEY (`utilisation_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Contenu de la table `utilisation`
--

INSERT INTO `utilisation` (`utilisation_id`, `utilisation_code`, `utilisation_accept`, `utilisation_entrantsortant`, `utilisation_place`, `utilisation_dateheure`) VALUES
(1, '0010e5b22', 0, 2, 15, '09/02/2015 - 20:24'),
(2, '0000c2f7ee', 1, 1, 1, '09/02/2015 - 20:20'),
(3, '1110f6f99', 0, 2, 15, '09/02/2015 - 19:13'),
(4, '0000f5b69', 0, 2, 15, '09/02/2015 - 15:04'),
(5, '0000c2f7ee', 1, 0, 1, '09/02/2015 - 08:24'),
(6, '1111c3a56', 1, 0, 3, '08/02/2015 - 23:55'),
(7, '0001f2f00', 1, 0, 2, '08/02/2015 - 22:25'),
(8, '0100b87a09', 1, 1, 0, '08/02/2015 - 18:14'),
(9, '0101a2c26', 0, 2, 15, '08/02/2015 - 17:26'),
(10, '0100b87a09', 1, 0, 0, '08/02/2015 - 16:59');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
