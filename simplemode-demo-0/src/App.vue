<template>
  <v-app>

    <v-navigation-drawer
      v-model="drawer"
      :width="153"
      :permanent="$vuetify.display.mdAndUp"
      :temporary="!$vuetify.display.mdAndUp">
      <v-list-item title="AI 기능"/>
      <v-divider/>

      <v-list>
        <v-list-item>
          <v-select
            label="user id"
            :items="userIds"
            style="max-width: 200px;"
            v-model="store.selectedUserId"
          />
        </v-list-item>
        <v-list-item link to="/simplemode-list">전체 기능 목록</v-list-item>
        <v-list-item link to="/tag-based-song-explorer">곡별 태그 탐색 기능</v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- 메인 컨텐츠 영역 -->
    <v-main style="max-width: 100%; width: 100%;"> <!--  :style="{ marginLeft: drawerVisible ? '153px' : '0' }" -->
      <v-container :style="{ width: mainWidth }" class="content-container">
        <RouterView :key="store.selectedUserId"/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import {useUserStore} from "@/stores/userStore";
import {useDisplay} from "vuetify";

export default {
  data() {
    return {
      store: useUserStore(),
      display: useDisplay(),
      drawer: true,
      userIds: ['46536104', '59040609', '37884321', '52894215', '59337842'],
    };
  },
  mounted() {
  },
  computed: {
    mainWidth() {
      return "90vw";
    },
    drawerVisible() {
      return this.display.mdAndUp.value && this.drawer.value;
    },
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
  justify-content: center;
  align-items: center;
  height: 100%;
}

::v-deep(.v-container) {
  padding: 10px;
  margin: 0;
}

::v-deep(.v-card-text) {
  padding: 10px
}
</style>
