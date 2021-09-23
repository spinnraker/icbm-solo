   
    
    
CREATE TABLE `icmb-tables`.`customer` (
`Customer_ID` INT NOT NULL,
`Customer_First_Name` VARCHAR(45) NULL DEFAULT NULL,
PRIMARY KEY (`Customer_ID`));
INSERT INTO `icmb-tables`.`customer`
(`Customer_ID`,
`Customer_First_Name`)
VALUES
(1, 'mike');
INSERT INTO `icmb-tables`.`customer`
(`Customer_ID`,
`Customer_First_Name`)
VALUES
(0, 'tom');

ALTER TABLE `icmb-tables`.`customer` 
ADD COLUMN `Customer_Last_Name` VARCHAR(45) NULL DEFAULT NULL AFTER `Customer_First_Name`,
ADD COLUMN `Customer_Total_Finances` DOUBLE NULL DEFAULT NULL AFTER `Customer_Last_Name`,
ADD COLUMN `Customer_Email` VARCHAR(45) NULL DEFAULT NULL AFTER `Customer_Total_Finances`,
ADD COLUMN `Customer_Age` INT NULL DEFAULT NULL AFTER `Customer_Email`,
ADD COLUMN `Customer_Gender` VARCHAR(45) NULL DEFAULT NULL AFTER `Customer_Age`,
ADD COLUMN `Customer_Risk` INT NULL DEFAULT NULL AFTER `Customer_Gender`;

CREATE TABLE `icmb-tables`.`result` (
  `Result_ID` INT NOT NULL,
  `Result_Description` VARCHAR(255) NULL,
  `Result_Risk` DOUBLE NULL,
  PRIMARY KEY (`Result_ID`),
  CONSTRAINT `Customer_ID`
    FOREIGN KEY (`Result_ID`)
    REFERENCES `icmb-tables`.`customer` (`Customer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Question_Risk_Modifier`
    FOREIGN KEY (`Result_ID`)
    REFERENCES `icmb-tables`.`questions` (`Question_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


CREATE TABLE `icmb-tables`.`login_history` (
  `Login_ID` INT NOT NULL,
  `Login_Date` DATETIME NULL,
  PRIMARY KEY (`Login_ID`));
  
CREATE TABLE `icmb-tables`.`lookup_risk` (
  `Risk_ID` INT NOT NULL,
  `Risk_Description` VARCHAR(255) NULL,
  PRIMARY KEY (`Risk_ID`));
  
  
CREATE TABLE `icmb-tables`.`questions` (
  `Question_ID` INT NOT NULL,
  `Question_Description` VARCHAR(45) NULL,
  `Question_Risk_Modifier` DOUBLE NULL,
  PRIMARY KEY (`Question_ID`));
  
ALTER TABLE `icmb-tables`.`questions` 
ADD CONSTRAINT `Customer_ID`
  FOREIGN KEY (`Question_ID`)
  REFERENCES `icmb-tables`.`customer` (`Customer_ID`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

INSERT INTO `icmb-tables`.`questions`
(`Question_ID`,
`Question_Description`,
`Question_Risk_Modifier`)
VALUES
(0,
"How many wood chucks could a wood chuck chuck if a wood chuck could chuck wood?",
10);
