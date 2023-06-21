import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

// create express app listening on port 1245
const app = express();
const port = 1245;

// create redis client
const client = createClient();

const listProducts = [  
  {"itemId": 1, "itemName": 'Suitcase 250', "price": 50, "initialAvailableQuantity": 4},
  {"itemId": 2, "itemName": 'Suitcase 450', "price": 100, "initialAvailableQuantity": 10},
  {"itemId": 3, "itemName": 'Suitcase 650', "price": 350, "initialAvailableQuantity": 2},
  {"itemId": 4, "itemName": 'Suitcase 1050', "price": 550, "initialAvailableQuantity": 5}
];

const getItemById = (id) => {
  return listProducts.filter((item) => item.itemId === id)[0];
};

const reserveStockById = (itemId, stock) => {
  client.set(itemId, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  return await promisify(client.get).bind(client)(itemId);
};

// routes
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  if (!item) {
    res.json({"status":"Product not found"});
  } else {
    getCurrentReservedStockById(itemId)
      .then((result) => Number.parseInt(result || 0))
      .then((reservedStock) => {
        item.currentQuantity = item.initialAvailableQuantity - reservedStock;
        res.json(item);
    });
  }
});

app.get("reserve_product/:itemId", (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ "status": "Product not found" });
    return;
  }
  getCurrentReservedStockById(itemId)
    .then((result) => parseInt(result || 0))
    .then((reservedStock) => {
      if (reservedStock >= item.initialAvailableQuantity) {
        res.json({ "status": "Not enough stock available", itemId });
        return;
      }
      reserveStockById(itemId, reservedStock + 1).then(() => {
        res.json({ "status": "Reservation confirmed", itemId });
      });
    });
});

app.listen(port);
