
const Test = new Mongo.Collection('Test');

Test.attachSchema(
    new SimpleSchema({
    title: {
      type: String
    },
    content: {
      type: String
    },
    createdAt: {
      type: Date,
      denyUpdate: true
    }
  })
);

// Collection2 already does schema checking
if (Meteor.isServer) {
  Test.allow({
    insert : () => false,
    update : () => false,
    remove : () => false
  });
}

export default Test;
