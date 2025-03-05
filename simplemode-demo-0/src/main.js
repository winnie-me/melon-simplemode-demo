import './assets/main.css';

import {createApp} from 'vue';
import {createPinia} from 'pinia';

import App from './App.vue';
import router from './router';

// ✅ Vuetify 가져오기
import {createVuetify} from 'vuetify';
import 'vuetify/styles'; // Vuetify 스타일 추가

// ✅ Vuetify 컴포넌트 & 디렉티브 자동 등록
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

const vuetify = createVuetify({
  components,  // Vuetify의 모든 컴포넌트 등록
  directives,  // Vuetify의 모든 디렉티브 등록
});

createApp(App)
  .use(createPinia())
  .use(router)
  .use(vuetify)
  .mount('#app');
