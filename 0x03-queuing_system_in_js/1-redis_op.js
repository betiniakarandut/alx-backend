import redis from 'redis';

const client = redis.createClient()

client.on("connect", () => {
	console.log("Redis client connected to the server");
});

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error}`)
});

function setNewSchool(schoolName, value, callback){
	client.set(schoolName, value, (err, reply) => {
		if (err) {
			console.error(`Error setting ${schoolName}: ${err}`);
		} else {
			console.log(`Set ${schoolName}: ${value}`);
			client.get(schoolName, redis.print); // Use redis.print to display confirmation
			if (callback) {
				callback();
			}
		}
	});
}

function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, reply) => {
		if (err) {
			console.error(`Error getting ${schoolName}: ${err}`);
		} else {
			console.log(`${schoolName}: ${reply}`);
		}
	});
}

setNewSchool('Holberton', '50', () => {
	displaySchoolValue('Holberton');
});

setNewSchool('HolbertonSanFrancisco', '100', () => {
	displaySchoolValue('HolbertonSanFrancisco');
});
