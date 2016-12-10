import moment from 'moment';
import FIEvent from '/universal/models/Event';

export default function (Template) {
  Template['events'].helpers({
    'events': function() {
      return FIEvent.find();
    },

    'formatDate': function(time) {
      return moment(time).format('MM/DD HH:mmA');
    }
  });

  Template['events'].events({
    'click .event-list-item'(event) {
      var id = $(event.currentTarget).data('id');
      FlowRouter.go(`/events/${id}`);
    },

    'click #back-btn': function() {
      history.back();
    }
  });

  Template['events'].onCreated(function() {
    Session.set('viewTitle', 'Current events');
  });
}
