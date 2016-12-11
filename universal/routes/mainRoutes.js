import { renderBasic, renderSlim } from './helpers.js';

export default function (FlowRouter) {
  FlowRouter.notFound = {
    action: () => renderSlim('notFound')
  };
}
