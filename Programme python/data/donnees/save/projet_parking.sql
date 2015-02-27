--
-- Base de données: `projet_parking`
--

-- --------------------------------------------------------

--
-- Structure de la table `places`
--

CREATE TABLE IF NOT EXISTS places (
  places_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  places_code TEXT,
  places_dispo INTEGER,
  places_predef INTEGER,
  places_active INTEGER
)

--
-- Contenu de la table `places`
--

INSERT INTO places (places_id, places_code, places_dispo, places_predef, places_active) VALUES
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

CREATE TABLE IF NOT EXISTS utilisation (
  utilisation_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
  utilisation_code INTEGER,
  utilisation_accept INTEGER,
  utilisation_entrantsortant INTEGER,
  utilisation_place INTEGER,
  utilisation_dateheure TEXT
)

--
-- Contenu de la table `utilisation`
--

INSERT INTO utilisation (utilisation_id, utilisation_code, utilisation_accept, utilisation_entrantsortant, utilisation_place, utilisation_dateheure) VALUES
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

