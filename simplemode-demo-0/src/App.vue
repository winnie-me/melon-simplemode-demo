<template>
  <v-app>
    <!-- 네비게이션 드로어 -->
    <v-navigation-drawer
      v-model="drawer"
      :width="153"
      :permanent="$vuetify.display.mdAndUp"
      temporary
    >
      <v-list-item title="SimpleMode"></v-list-item>
      <v-divider></v-divider>
      <v-list>
        <v-list-item>
          <v-select
            label="user id"
            :items="userIds"
            style="max-width: 200px;"
            v-model="store.selectedUserId"
          ></v-select>
        </v-list-item>
        <v-list-item link to="/ex-card-0">Card</v-list-item>
        <!--        <v-list-item link to="/accordion-list-0">Expand</v-list-item>-->
        <v-list-item link to="/accordion-list-1">Expand 2</v-list-item>
<!--        <v-list-item link to="/accordion-list-2">Expand 3</v-list-item>-->
      </v-list>
    </v-navigation-drawer>

    <!-- 메인 컨텐츠 영역 -->
    <v-main>
      <!--      <v-container fluid>-->
      <v-container :style="{ width: mainWidth }" class="content-container">
        <RouterView/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
// import AccordionListView from "@/views/AccordionListView.vue";
import { useUserStore } from "@/stores/userStore";

export default {
  //   components: {
  //   AccordionListView, // 등록 필요
  // },
  data() {
    return {
      store: useUserStore(),
      drawer: true,
      userIds: ['46536104', '59040609'],
    };
  },
  computed: {
    // 📌 화면 크기에 따라 메인 컨텐츠 width 조정
    mainWidth() {
      // if (this.$vuetify.display.xl) return "100vw"; // 큰 화면에서 80% 사용
      // if (this.$vuetify.display.lg) return "100vw"; // 일반 화면에서 85%
      // if (this.$vuetify.display.md) return "100vw"; // 태블릿에서 90%
      return "90vw"; // 모바일에서 거의 풀스크린
    }
  },
  methods: {
    toggleDrawer() {
      this.drawer = !this.drawer;
    },
    selectItem(item) {
      console.log(`${item} 선택됨`);
    }
  }
};
</script>

<style scoped>
.content-container {
  //display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
</style>
