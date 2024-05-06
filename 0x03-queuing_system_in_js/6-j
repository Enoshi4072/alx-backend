import kue from 'kue';
//import redis from 'redis';

// Create a Redis client for Kue
// const redisClient = redis.createClient();

// Create a Kue queue
const queue = kue.createQueue({ name: 'push_notification_code' });

// Define the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test message',
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData);

// Event handler for successful job creation
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

// Event handler for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event handler for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();
