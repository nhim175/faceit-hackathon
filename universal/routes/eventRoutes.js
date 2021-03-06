import { renderApp } from './helpers.js';

// TODO: call this in entry file
export default function () {
  FlowRouter.route('/events', {
    action: () => renderApp('events')
  });

  FlowRouter.route('/events/:id', {
    action: (params, queryParams) => renderApp('eventDetail', params, queryParams)
  });

  FlowRouter.route('/events/:id/attendance', {
    action: (params, queryParams) => renderApp('eventAttendance', params, queryParams)
  });
}
