use smart_home_energy_db

db.sensor_logs.insertOne({
  device_id: 1,
  device_name: "AC",
  room_id: 101,
  timestamp: "2026-01-10 10:00:00",
  energy_kwh: 5.5,
  status: "ON"
})

db.sensor_logs.createIndex({ device_id: 1 })

db.sensor_logs.createIndex({ timestamp: 1 })