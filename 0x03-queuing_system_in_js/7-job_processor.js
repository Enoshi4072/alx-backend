import kue from 'kue';

// Define the array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // Track progress of the job
  job.progress(0, 100);

  // Check if phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    // Update progress to 50%
    job.progress(50, 100);
    // Log sending notification
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }

  // Notify job is done
  done();
}

// Create a queue with Kue
const queue = kue.createQueue({ name: 'push_notification_code_2' });

// Process two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract phone number and message from job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function
  sendNotification(phoneNumber, message, job, done);
});
