import config from '../universal/config';

import createMainRoutes from '../universal/routes/mainRoutes';
import createAppRoutes from '../universal/routes/appRoutes';
import createEventRoutes from '../universal/routes/eventRoutes';

import createHome from './components/home/home';
import createSelectApp from './components/selectApp/selectApp';
import createHeader from './components/header/header';
import createEvents from './components/events/events';
import createEventDetail from './components/eventDetail/eventDetail';
import createAppHeader from './components/appHeader/appHeader';

createMainRoutes(FlowRouter);
createAppRoutes(FlowRouter);
createEventRoutes(FlowRouter);

createHome(Template);
createHeader(Template);
createSelectApp(Template);
createEvents(Template);
createEventDetail(Template);
createAppHeader(Template);
