import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue({ name: 'push_notification_code' });

// Function to send notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs from the queue
queue.process('push_notification_code', (job, done) => {
  // Extract phone number and message from job data
  const { phoneNumber, message } = job.data;
  
  // Call sendNotification function
  sendNotification(phoneNumber, message);
  
  // Mark job as completed
  done();
});
