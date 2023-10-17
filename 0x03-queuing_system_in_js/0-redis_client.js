import redis from 'redis';

const client = redis.createClient()

// Event listener for successful connection
client.on("connect", () => {
	console.log("Redis client connected to the server");
});

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error}`)
});

client.quit()
