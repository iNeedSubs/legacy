import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import { FontAwesomeIcon } from '@/plugins/fa';

createApp(App)
  .use(router)
  .component('fa', FontAwesomeIcon)
  .mount('#app');
