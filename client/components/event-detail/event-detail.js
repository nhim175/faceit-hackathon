import FIEvent from '/universal/models/Event';
import FICheckIn from '/universal/models/CheckIn';
import moment from 'moment';

export default function (Template) {

  Template['event-detail'].helpers({
    'event': function() {
      return FIEvent.findOne(this.params.id);
    },

    'getUser': function(userId) {
      return Meteor.users.findOne(userId);
    },

    'checkIns': function() {
      return FICheckIn.find({
        eventId: this.params.id
      });
    },

    'formatTime': function(time) {
      return moment(time).format('HH:mmA');
    },

    'formatDate': function(time) {
      return moment(time).format('MM/DD HH:mmA');
    }
  });

  Template['event-detail'].events({
  });

  Template['event-detail'].onCreated(function() {
    Session.set('viewTitle', 'Event detail');
  });
}
