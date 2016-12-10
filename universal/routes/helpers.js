export function renderBasic(template) {
  return BlazeLayout.render('basicLayout', {
    content: template, header: 'header', footer: 'footer'
  });
}

export function renderSlim(template) {
  return BlazeLayout.render('basicLayout', { content: template });
}

export function renderApp(template, params) {
  return BlazeLayout.render('appLayout', {
    content: template, appHeader: 'appHeader', data: {
      params: params
    }
  });
}
