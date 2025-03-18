-- Question #1:
-- SELECT
-- 	idLitCharacters,
-- 	Name,
-- 	CreatureSubType
-- FROM LitCharacters 
-- WHERE CreatureSubType IN ("Pirates", "Mermaid", "Fairy")
-- ORDER BY idLitCharacters ASC;
--------------------------------------------------
-- Question #2

-- SELECT
-- 	idLitCharacters,
-- 	Name,
-- 	CreatureSubType,
-- 	Weight
-- FROM LitCharacters 
-- WHERE CreatureSubType = "Mermaid"
-- AND Weight > 120
-- ORDER BY idLitCharacters ASC;

-- Question #3
-- SELECT
-- 	idLitCharacters,
-- 	Name,
-- 	CreatureSubType
-- FROM LitCharacters 
-- WHERE CreatureSubType LIKE "%Scientist%"
-- OR CreatureSubType LIKE "%villain%"
-- ORDER BY idLitCharacters ASC;

-- Question #4

-- SELECT
-- 	idLitCharacters,
-- 	Name,
-- 	CreatureSubType,
-- 	Gender
-- FROM LitCharacters 
-- WHERE Gender != "Male"
-- ORDER BY idLitCharacters ASC;

-- Question #5

-- SELECT
-- 	idLitCharacters,
-- 	Name,
-- 	Gender,
-- 	CreatureSubType
-- FROM LitCharacters 
-- WHERE (Gender = "Female" AND CreatureSubType LIKE "%Pirate%")
-- OR (Gender = "Male" AND Weight <= 10)
-- ORDER BY idLitCharacters ASC;

--  Question #6
-- SELECT
-- 	idLitCharacters,
-- 	Name,
-- 	Gender,
-- 	CreatureSubType,
-- 	Weight,
-- 	Height
-- FROM LitCharacters 
-- WHERE (Height >= 200)
-- ORDER BY Weight DESC, idLitCharacters ASC;

-- Question 7

-- SELECT
-- 	idLitCharacters,
-- 	Name,
-- 	Gender,
-- 	CreatureSubType,
-- 	Weight,
-- 	Height
-- FROM LitCharacters 
-- WHERE (Weight >= 2000) OR (Height>=200)
-- ORDER BY Name, idLitCharacters ASC;

-- Question 8

-- SELECT SUM(Weight)
-- FROM LitCharacters 
-- WHERE CreatureSubType in ("Pirate","Supervillain", "Mad Scientist")

-- Question 9
-- SELECT 
-- 	SUM(CASE WHEN CreatureSubType = "Dinosaur" THEN Weight ELSE 0 END)-
-- 	SUM(CASE WHEN CreatureSubType = "Basilisk" THEN Weight ELSE 0 END) As Tota_difference
-- FROM LitCharacters;

-- Question 10

-- 10.	[SQL Week 2 Question 100-010] Use the LIKE command to select the 
-- idLitCharacters, name, and creature subtype of all the creatures which
-- start with MER (i.e. mermen, mermaids, etc.).  Sort it alphabetically by name.

-- SELECT 
-- 	idLitCharacters,
-- 	Name,
-- 	CreatureSubType
-- FROM LitCharacters
-- whERE
-- 	CreatureSubType LIKE "%mer%"
-- ORDER BY Name;

-- Question 11
/*11.[SQL Week 2 Question 100-011] What is the average weight 
	of all creatures for which the name contains the string 
	‘the’ ?  The phrase can be anywhere in the name – so 
	“The Bronze Swan” would count, as would “Belet the Hero” 
	and “Moonbean Mistyweather.”  Note your answer to four 
	decimal places.*/


-- SELECT 
-- 	ROUND(AVG(CASE WHEN Name LIKE "%the%" THEN Weight ELSE 0 END),4) AS Average_Weight
-- FROM LitCharacters

/* Question 12 ---
	12.	[SQL Week 2 Question 100-012] Select all the fields for all 
	the creatures that contain the word “the” in their names, such as
	“Roderick the Brave.”  Do not include entries for which “The” is
	the first word, such as “The Fire Breather” or where “the” is
	inside of the name such as “Amethelia”.
	Order alphabetically by Name, then ascending by idLitCharacters.
*/
-- SELECT *
-- FROM LitCharacters
-- WHERE
-- 	Name LIKE "%_the %"
-- ORDER BY Name, idLitCharacters ASC;

-- -- Question 13:
-- SELECT *
-- FROM LitCharacters
-- WHERE
-- 	Name LIKE "%ll%"
-- AND
-- 	CreatureSubType != "Knight"
-- ORDER BY Appearances ASC, idLitCharacters ASC;

-- Question 14

-- SELECT *
-- FROM LitCharacters
-- WHERE
-- 	CreatureSubType IN (
-- 		"Knight",
-- 		"Pirate",
-- 		"Fairy",
-- 		"Cowboy",
-- 		"Cowgirl"
-- 	)
-- AND
-- 	Appearances >= 2
-- ORDER BY idLitCharacters DESC
-- LIMIT 10;

-- MOD 1
-- SELECT *
-- FROM LitCharacters
-- WHERE
-- 	CreatureSubType IN (
-- 		"Knight",
-- 		"Pirate",
-- 		"Fairy",
-- 		"Cowboy",
-- 		"Cowgirl"
-- 	)
-- AND
-- 	Appearances >= 2
-- ORDER BY idLitCharacters DESC
-- LIMIT 10;


-- MOD 2
-- SELECT CreatureSubType, COUNT(*) as Creature_sub_type_count
-- FROM 
-- 	(
-- 	SELECT CreatureSubType
-- 	FROM LitCharacters
-- 	WHERE
-- 		CreatureSubType IN (
-- 			"Knight",
-- 			"Pirate",
-- 			"Fairy",
-- 			"Cowboy",
-- 			"Cowgirl"
-- 		)
-- 	AND
-- 		Appearances >= 2
-- 	ORDER BY idLitCharacters DESC
-- 	LIMIT 10
-- 	) AS count_sub_query
-- GROUP BY CreatureSubType

-- QUESTION 15 ----------------------
-- SELECT COUNT(*) AS small_n_cute
-- FROM LitCharacters
-- WHERE 
-- 	(Height BETWEEN 10 AND 25)
-- AND
-- 	(Weight BETWEEN 5 AND 10);
-- _
-- QUESTION 16 ----------------------
-- SELECT COUNT(*) AS total_magical
-- FROM LitCharacters
-- WHERE
--  Realm = "Magical";

-- -- UPDATE
-- UPDATE 
-- 	LitCharacters
-- SET
-- 	Realm = "Magical"
-- WHERE CreatureSubType = "Knight";

-- -- Verify Magical Count
-- SELECT COUNT(*) AS total_magical
-- FROM LitCharacters
-- WHERE
--  Realm = "Magical";
-- -- _
-- QUESTION 17 ----------------------
-- a)
-- SELECT ((COUNT(*) * AVG(Weight)) % 99) as checksum from litcharacters;
-- DELETE FROM 
-- 	LitCharacters
-- WHERE
-- 	CreatureSubType = "Dinosaur"
-- AND 
-- 	Appearances > 0;
-- SELECT 
-- 	((COUNT(*) * AVG(Weight)) % 99) as checksum_after_delete
-- FROM litcharacters;
-- _
-- QUESTION 18 ----------------------
-- SELECT ((COUNT(*) * AVG(Weight)) % 99) as checksum from litcharacters;

-- INSERT INTO 
-- 	LitCharacters(Name, Realm, CreatureType, CreatureSubType, Gender, Height, Weight, Appearances)
-- VALUES 
-- 	('Mogwai', 'Magical', 'Other', 'Fairy', 'Female', '25', '158','2'),
-- 	('Menehune', 'Real', 'Human', 'Superhero', 'Male', '56', '195','5');
-- SELECT ((COUNT(*) * AVG(Weight)) % 99) as checksum_after_insert from litcharacters;

-- _