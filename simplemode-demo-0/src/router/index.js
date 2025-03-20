import {createRouter, createWebHashHistory} from 'vue-router'
import TrendRevivalListView from "@/views/TrendRevivalListView.vue";
import SimpleModeListView from "@/views/SimpleModeListView.vue";
import TagBasedSongExplorer from "@/views/TagBasedSongExplorer.vue";
import CustomCollectionListView from "@/views/CustomCollectionListView.vue";
import SeasonalityListView from "@/views/SeasonalityListView.vue";
// import {useUserStore} from "@/stores/selectedUserStore.js";

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
    {
      path: '/seasonality',
      name: 'seasonality',
      component: SeasonalityListView,
    },

  ],
})

// 🔹 모든 라우트 이동 전에 `fetchUserData()` 실행
/*router.beforeEach(async (to, from, next) => {
  const userStore = useUserStore();

  if (!userStore.userId) {
    await userStore.fetchUserData();
  }

  next();
});*/

export default router
