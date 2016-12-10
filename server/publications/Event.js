// TODO: call this in entry file
export default function () {
  Meteor.publish('Event', function () {
    return Event.find();
  });
}
