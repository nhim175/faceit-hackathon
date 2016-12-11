import FIEvent from '/universal/models/Event';
import FIAttendee from '/universal/models/Attendee';

export default function (Template) {
  Template['eventAttendance'].helpers({
    'event': function() {
      return FIEvent.findOne(this.params.id);
    },

    'getUser': function(userId) {
      return Meteor.users.findOne(userId);
    },

    'getAvatar': function(user) {
      if (user.profile && user.profile.avatar) {
        return user.profile.avatar
      } else {
        return 'http://placehold.it/128x128';
      }
    },

    'attendees': function() {
      return FIAttendee.find({
        eventId: this.params.id
      }, {
        sort: {
          checkedIn: -1
        }
      });
    }
  });

  Template['eventAttendance'].events({
    'click #back-btn': function() {
      history.back();
    },

    'click .user-list-item': function(event) {
      var userId = $(event.currentTarget).data('id');
      FlowRouter.go(`/users/${userId}`);
    }
  });

  Template['eventAttendance'].onCreated(function() {
    Session.set('viewTitle', 'Event attendance');
  });
}
