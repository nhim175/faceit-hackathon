// TODO: call this in entry file
export default function () {
  Meteor.publish('User', function () {
    return User.find();
  });
}
