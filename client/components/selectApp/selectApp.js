// TODO: call this in entry file
export default function (Template) {
  Template['selectApp'].helpers({
  });

  Template['selectApp'].events({
    'click #events-link': function() {
      FlowRouter.go('/events');
    }
  });
}
