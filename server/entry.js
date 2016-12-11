import setupBrowserPolicy from './config/security.js';
import loadFixtures from './loaders/fixtures.js';
import loadUsers from './loaders/users.js';

import FICheckInOutQueue from '/universal/models/CheckInOutQueue';
import FICheckInOut from '/universal/models/CheckInOut';
import FIAttendee from '/universal/models/Attendee';

setupBrowserPolicy(BrowserPolicy);

Meteor.startup(() => {
  loadUsers();
  Meteor.setInterval(function() {
    var checkInOutQueue = FICheckInOutQueue.find().fetch();
    console.log(checkInOutQueue);
    checkInOutQueue.forEach(checkInOut => {

      var attendee = FIAttendee.findOne({
        userId: checkInOut.userId,
        eventId: checkInOut.eventId
      });

      if ((checkInOut.type === 'in' && attendee.checkedIn) ||
        (checkInOut.type === 'out' && !attendee.checkedIn)) {
        FICheckInOutQueue.remove(checkInOut);
        return;
      }

      attendee.checkedIn = checkInOut.type === 'in';
      FIAttendee.update(attendee._id, {
        $set: attendee
      });
      FICheckInOut.insert({
        attendeeId: attendee._id,
        eventId: checkInOut.eventId,
        userId: checkInOut.userId,
        type: checkInOut.type,
        createdAt: checkInOut.createdAt
      });
      FICheckInOutQueue.remove(checkInOut);
    });
  }, 1000);
});
