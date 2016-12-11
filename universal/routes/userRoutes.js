import { renderApp } from './helpers.js';

// TODO: call this in entry file
export default function (FlowRouter) {
  FlowRouter.route('/users/:id', {
    action: (params, queryParams) => renderApp('userDetail', params, queryParams)
  });
}
