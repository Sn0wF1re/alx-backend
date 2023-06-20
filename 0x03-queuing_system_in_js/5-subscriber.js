import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ERROR MESSAGE');
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  client.subscribe('holberton school channel');
  client.on('message', (_err, msg) => {
    console.log(msg);
    if (msg === 'KILL_SERVER') {
      client.unsubscribe('holberton school channel');
      client.quit();
    }
  });
});
