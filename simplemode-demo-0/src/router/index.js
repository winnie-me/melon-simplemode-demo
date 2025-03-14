import {createRouter, createWebHashHistory, createWebHistory} from 'vue-router'
// import AccordionListView from "@/views/AccordionListView.vue";
import ExampleCardView from "@/views/ExampleCardView.vue";
import ListView from "@/views/ListView.vue";
import AccordionListView2 from "@/views/AccordionListView2.vue";
import TrendRevivalListView from "@/views/TrendRevivalListView.vue";
import SimpleModeListView from "@/views/SimpleModeListView.vue";
import TagBasedSongExplorer from "@/views/TagBasedSongExplorer.vue";

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
    }, // tag-based-song-explorer
    {
      path: '/tag-based-song-explorer',
      name: 'tag-based-song-explorer',
      component: TagBasedSongExplorer,
    },

    {
      // list-0
      path: '/ex-card-0',
      name: 'ex-card-0',
      component: ExampleCardView,
    },
    {
      path: '/list-0',
      name: 'list-0',
      component: ListView,
    },
    /*    {
          path: '/accordion-list-0',
          name: 'accordion-list-0',
          component: AccordionListView,
        },*/

/*    {
      path: '/accordion-list-2',
      name: 'accordion-list-2',
      component: AccordionListView3,
    },*/
  ],
})

export default router
