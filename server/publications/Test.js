// TODO: call this in entry file
export default function () {
  Meteor.publish('Test', function () {
    return Test.find();
  });
}
