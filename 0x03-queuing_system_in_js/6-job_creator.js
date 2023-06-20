import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});
const data = {
  phoneNumber: '+254712098567',
  message: 'Notifications enabled!',
};

const job = queue.create('push_notification_code', data);

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
}).on('complete', () => {
  console.log('Notification job completed');
}).on('failed attempt', () => {
  console.log('Notification job failed');
}).on('failed', () => {
  console.log('Notiication job failed');
});

job.save();
