import FIEvent from '/universal/models/Event';
import FIAttendee from '/universal/models/Attendee';
import moment from 'moment';

export default function (Template) {

  Template['eventDetail'].helpers({
    'event': function() {
      return FIEvent.findOne(this.params.id);
    },

    'getUser': function(userId) {
      return Meteor.users.findOne(userId);
    },

    'checkIns': function() {
      return FIAttendee.find({
        eventId: this.params.id,
        checkedIn: true
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
      return moment(time).format('HH:mmA');
    },

    'formatDate': function(time) {
      return moment(time).format('MM/DD HH:mmA');
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
