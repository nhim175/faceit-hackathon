import moment from 'moment';

import FIEvent from '/universal/models/Event';
import FICheckInOut from '/universal/models/CheckInOut';

// TODO: call this in entry file
export default function (Template) {
  Template['userDetail'].helpers({
    'checkInOuts': function() {
      return FICheckInOut.find({
        userId: this.params.id
      });
    },

    'user': function() {
      return Meteor.users.findOne(this.params.id);
    },

    'getUser': function(id) {
      return Meteor.users.findOne(id);
    },

    'getEvent': function(id) {
      return FIEvent.findOne(id);
    },

    'timeAgo': function(time) {
      return moment(time).fromNow();
    },

    'isCheckIn': function(checkInOut) {
      return checkInOut.type === 'in';
    }
  });

  Template['userDetail'].events({
    'click #back-btn': function() {
      history.back();
    }
  });
}
