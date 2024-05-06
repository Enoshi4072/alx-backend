import redis from 'redis';

// Create a new Redis client
const client = redis.createClient();

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection error
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the 'holberton school' channel
client.subscribe('holberton school');

// Event handler for receiving messages
client.on('message', (channel, message) => {
  console.log(message);
  
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school');
    client.quit();
  }
});
