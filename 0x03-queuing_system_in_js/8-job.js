import { createQueue } from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }
  jobs.forEach(item => {
    const queue = createQueue();
    let job = queue.create('push_notification_code_3', item);
    job
      .on('enqueue', () => {
        console.log(`Notification job created: ${job.id}`);
      })
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      })
      .on('progress', (prog, data) => {
        console.log(`Notification job ${job.id} ${prog}% complete`);
      });

      job.save();
  });
};

module.exports = createPushNotificationsJobs;
