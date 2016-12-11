import FIEvent from '/universal/models/Event';
import FIAttendee from '/universal/models/Attendee';
import FICheckInOut from '/universal/models/CheckInOut';
import moment from 'moment';

export default function (Template) {

  Template['eventDetail'].helpers({
    'event': function() {
      return FIEvent.findOne(this.params.id);
    },

    'getUser': function(userId) {
      return Meteor.users.findOne(userId);
    },

    'getAttendee': function(attendeeId) {
      return FIAttendee.findOne(attendeeId);
    },

    'isCheckIn': function(checkInOut) {
      return checkInOut.type === 'in';
    },

    'checkedIns': function() {
      return FIAttendee.find({
        eventId: this.params.id,
        checkedIn: true
      });
    },

    'checkInOuts': function() {
      return FICheckInOut.find({
        eventId: this.params.id
      }, {
        sort: {
          createdAt: -1
        }
      });
    },

    'count': function(collection) {
      return collection.count();
    },

    'attendees': function() {
      return FIAttendee.find({
        eventId: this.params.id
      });
    },

    'formatTime': function(time) {
      return moment(time).format('H:mmA');
    },

    'formatDate': function(time) {
      return moment(time).format('MM/DD h:mmA');
    }
  });

  Template['eventDetail'].events({
    'click #back-btn': function() {
      history.back();
    },

    'click #attendance-btn': function(event) {
      event.preventDefault();
      event.stopPropagation();
      var id = $(event.currentTarget).data('id');
      FlowRouter.go(`/events/${id}/attendance`);
    }
  });

  Template['eventDetail'].onCreated(function() {
    Session.set('viewTitle', 'Event detail');
  });
}
