import createPushNotificationsJobs from './8-job';
import { createQueue } from 'kue';
import { expect } from 'chai';

const queue = createQueue();

describe('createPushNtificationJobs', function () {
  before(function () {
    queue.testMode.enter();
  });
      
  afterEach(function () {
    queue.testMode.clear();
  });
      
  after(function () {
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs(('job1', 'job2'), queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('create two new jobs to the queue', function () {
    const jobs = [
      {
        phoneNumber: '4153118782',
        message: 'This is the code 4321 to verify your account'
      },
      {
        phoneNumber: '4153718781',
        message: 'This is the code 4562 to verify your account'
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });
});
