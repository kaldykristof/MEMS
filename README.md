# Parkolóház

**Hallgatói projekt a Széchenyi István Egyetem Mikroelektromechanikai rendszerek (GKNB_INTM020) nevű tárgyához.**<br/>
Győr, 2019/20-as tanév, 1. félév.

### Készítették:  
Név | Neptun-kód|GitHub
:-|:-|:-
Káldy Kristóf|R9ZHPM| [@kaldykristof](https://github.com/kaldykristof)
Geiger Boldizsár Sándor|RP6OUG| [@gboldi19](https://github.com/gboldi19)

### Felhasznált technológiák:<br/>
- Python
- MySQL

### Felhasznált eszközök:<br/>
- Raspberry Pi 3 Model B/B+
- Sense HAT modul
- Slamtec RPLIDAR A1M8
- Genius FaceCam 321
- Xiaomi Mi Power Bank 2C 20000 mAh

### Függőségek:<br />
Név | Elérhetőség
:-|:-
OpenCV-Python|https://pypi.org/project/opencv-python/
RPLIDAR|https://pypi.org/project/rplidar/
MySQL-Connector-Python|https://pypi.org/project/mysql-connector-python/
Raspberry Pi Sense HAT|https://pythonhosted.org/sense-hat/

```sh
pip install opencv-python rplidar mysql-connector-python
```
Szükséges adatbázis létrehozása:
```MySQL
CREATE DATABASE parking_lot;
USE parking_lot;
CREATE TABLE cars (
  id SMALLINT(3) NOT NULL AUTO_INCREMENT,
  license_plate VARCHAR(7) NOT NULL,
  arrival_time DATETIME NOT NULL,
  PRIMARY KEY (id)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci;
```