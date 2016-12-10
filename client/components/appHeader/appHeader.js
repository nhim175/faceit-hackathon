// TODO: call this in entry file
export default function (Template) {
  Template['appHeader'].helpers({
    viewTitle: function() {
      return Session.get('viewTitle');
    }
  });

  Template['appHeader'].events({
    'click #back-btn': function() {
      history.back();
    }
  });
}
