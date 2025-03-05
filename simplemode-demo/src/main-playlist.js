import { createApp } from 'vue';
import { createVuetify } from 'vuetify';

import App from './App.vue';
import router from './router/index.js';

import 'vuetify/styles'; // Vuetify 스타일 적용
import './assets/main.css'; // 글로벌 CSS

// Vuetify 인스턴스 생성
const vuetify = createVuetify();

// Vue 앱 생성 및 플러그인 등록
createApp(App)
  .use(vuetify)
  // .use(router)
  .mount('#app');
