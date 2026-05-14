CREATE DATABASE smart_home_energy;
USE smart_home_energy;
CREATE TABLE rooms (
    room_id INT PRIMARY KEY,
    room_name VARCHAR(100)
);

CREATE TABLE devices (
    device_id INT PRIMARY KEY,
    device_name VARCHAR(100),
    room_id INT,
    status VARCHAR(20),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE energy_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    device_id INT,
    energy_kwh DECIMAL(5,2),
    log_time DATETIME,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);
INSERT INTO rooms VALUES
(101,'Living Room'),
(102,'Kitchen');

INSERT INTO devices VALUES
(1,'AC',101,'ON'),
(2,'Refrigerator',102,'ON'),
(3,'TV',101,'OFF');

INSERT INTO energy_logs(device_id,energy_kwh,log_time) VALUES
(1,5.5,'2026-01-10 10:00:00'),
(2,2.0,'2026-01-10 11:00:00'),
(3,1.2,'2026-01-10 12:00:00');
SELECT * FROM rooms;
SELECT * FROM devices;
SELECT * FROM energy_logs;
UPDATE devices
SET status = 'OFF'
WHERE device_id = 1;

SELECT * FROM devices;
DELETE FROM energy_logs
WHERE log_id = 3;
SELECT * FROM energy_logs;
DELIMITER //

CREATE PROCEDURE RoomEnergySummary()
BEGIN
    SELECT 
        r.room_name,
        DATE(e.log_time) AS usage_date,
        SUM(e.energy_kwh) AS total_energy
    FROM energy_logs e
    JOIN devices d
        ON e.device_id = d.device_id
    JOIN rooms r
        ON d.room_id = r.room_id
    GROUP BY r.room_name, DATE(e.log_time);
END //

DELIMITER ;
CALL RoomEnergySummary();




