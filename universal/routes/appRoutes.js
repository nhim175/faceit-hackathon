import { renderBasic, renderSlim } from './helpers.js';

// TODO: call this in entry file
export default function (FlowRouter) {
  FlowRouter.route('/', {
    action: () => renderSlim('selectApp')
  });
}
