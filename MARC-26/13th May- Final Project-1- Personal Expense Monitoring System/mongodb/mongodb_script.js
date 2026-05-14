use expense_monitoring_db

db.receipts.insertOne({
  user_id: 1,
  receipt_id: 101,
  store: "Amazon",
  amount: 2500,
  category: "Shopping",
  date: "2026-01-15",
  notes: "Bought headphones"
})

db.receipts.createIndex({ user_id: 1 })