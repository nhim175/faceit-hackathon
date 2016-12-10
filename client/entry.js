import config from '../universal/config';
import createMainRoutes from '../universal/routes/mainRoutes';
import createAppRoutes from '../universal/routes/appRoutes';
import createHome from './components/home/home';
import createSelectApp from './components/selectApp/selectApp';
import createHeader from './components/header/header';

createMainRoutes(FlowRouter);
createAppRoutes(FlowRouter);

createHome(Template);
createHeader(Template);
createSelectApp(Template);
