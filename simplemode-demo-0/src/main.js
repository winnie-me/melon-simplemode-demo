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

const app = createApp(App)

// ✅ getOS 함수 정의
const getOS = () => {
  const userAgent = navigator.userAgent || navigator.vendor || window.opera;

  if (/android/i.test(userAgent)) {
    return "Android";
  } else if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
    return "iOS";
  } else if (/Macintosh|Mac OS X/.test(userAgent)) {
    return "macOS";
  } else if (/Windows NT/.test(userAgent)) {
    return "Windows";
  } else {
    return "Unknown";
  }
};

/*const playSong = (song) => {
  event.stopPropagation()

  switch (this.$getOS()) {
    case "Android":
    case "iOS":
      window.location.href = `melonapp://play?cid=${song.song_id}&ctype=1&openplayer=N&releaseRepeat=N&excludeSongList=Y`
      console.log("Android|iOS");
      break;
    case "macOS":
      window.location.href = `melonplayer://play?ref=XXX&cid=${song.song_id}&ctype=song&menuid=1234`; // URL 실행
      break;
    // case "Windows":
    //   console.log("목요일");
    //   break;
    default:
      console.log("잘못된 입력");
  }
}*/

// ✅ Vue 전역 함수로 등록
app.config.globalProperties.$getOS = getOS;
// app.config.globalProperties.$playSong = playSong;

app.use(createPinia())
  .use(router)
  .use(vuetify)
  .mount('#app');
