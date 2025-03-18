import {createRouter, createWebHashHistory} from 'vue-router'
import TrendRevivalListView from "@/views/TrendRevivalListView.vue";
import SimpleModeListView from "@/views/SimpleModeListView.vue";
import TagBasedSongExplorer from "@/views/TagBasedSongExplorer.vue";
import CustomCollectionListView from "@/views/CustomCollectionListView.vue";

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/simplemode-list", // 기본 페이지 리다이렉트
    },
    {
      path: '/simplemode-list',
      name: 'simplemode-list',
      component: SimpleModeListView,
    },

    {
      path: '/trend-revival-list',
      name: 'trend-revival-list',
      component: TrendRevivalListView,
    },
    {
      path: '/tag-based-song-explorer',
      name: 'tag-based-song-explorer',
      component: TagBasedSongExplorer,
    },
    {
      path: '/custom-collection-detail',
      name: 'custom-collection-detail',
      component: CustomCollectionListView,
    },

  ],
})

export default router
