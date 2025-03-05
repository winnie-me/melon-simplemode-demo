import {createRouter, createWebHashHistory, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AccordionListView from "@/views/AccordionListView.vue";
import ExampleCardView from "@/views/ExampleCardView.vue";
import ListView from "@/views/ListView.vue";

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
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
    {
      path: '/accordion-list-0',
      name: 'accordion-list-0',
      component: AccordionListView,
    },
  ],
})

export default router
