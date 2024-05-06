import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

const reserveSeatAsync = promisify(client.set).bind(client);
const getCurrentAvailableSeatsAsync = promisify(client.get).bind(client);

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeatsAsync('available_seats');
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats || 0 });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }
  
  const job = queue.create('reserve_seat').save(err => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeatsAsync('available_seats');
    const numberOfSeats = parseInt(currentAvailableSeats) || 0;

    if (numberOfSeats === 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
      console.log(`Seat reservation job ${job.id} failed: Not enough seats available`);
    } else {
      await reserveSeatAsync('available_seats', numberOfSeats - 1);
      console.log(`Seat reservation job ${job.id} completed`);
      done();
    }
  });
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Initialize available seats to 50
reserveSeatAsync('available_seats', 50);
