import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Playlist from '../views/Playlist.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/playlist-0', name: 'Playlist', component: Playlist },
];

const index = createRouter({
  history: createWebHistory(),
  routes,
});

export default index;
