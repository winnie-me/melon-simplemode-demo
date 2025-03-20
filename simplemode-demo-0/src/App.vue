<template>
  <v-app>

    <v-navigation-drawer
      v-model="drawer"
      :width="153"
      :permanent="$vuetify.display.mdAndUp"
      :temporary="!$vuetify.display.mdAndUp">
      <v-list-item title="AI 기능"/>
      <v-divider/>

      <v-select
        v-model="userStore.userId"
        @change="handleUserChange"
        :items="userList"
        label="User ID 선택"
        density="compact"
      />
      <v-select
        v-model="userStore.dt"
        @change="handleDtChange"
        :items="dtList"
        label="날짜 선택"
        density="compact"
      />
<!--      <v-list>-->
        <!--        <v-list-item>-->
        <!--        </v-list-item>-->
        <!--        <v-list-item>-->
        <!--        </v-list-item>-->
        <v-list-item link to="/simplemode-list" title="전체 기능 목록"/>
        <v-list-item link to="/tag-based-song-explorer" title="곡별 태그 탐색 기능"/>
        <!--        <v-list-item link to="/">개인화 플리 확인</v-list-item>-->
<!--      </v-list>-->
    </v-navigation-drawer>

    <!-- 메인 컨텐츠 영역 -->
    <v-main style="max-width: 100%; width: 100%;">
      <v-container :style="{ width: mainWidth }" class="content-container">
        <RouterView/> <!-- :key="userStore.userId" -->
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import {useDisplay} from "vuetify";
import {useUserStore} from "@/stores/selectedUserStore";
import {computed} from "vue";

export default {
  data() {
    return {
      // store: useUserStore(),
      userStore: useUserStore(),
      display: useDisplay(),
      drawer: true,
      userIds: ['46536104', '59040609', '37884321', '52894215', '59337842'],
    };
  },
  mounted() {
    // this.userStore.fetchUserData();
  },
  computed: {
    mainWidth() {
      return "95vw";
    },
    userList() {
      return Object.keys(this.userStore.userDtMap || {})
    },
    dtList() {
      return this.userStore.userDtMap?.[this.userStore.userId] || []
    }
  },
  methods: {
    handleUserChange: () => {
      this.userStore.setUserId(this.userStore.userId);
    },
    handleDtChange: () => {
      this.userStore.setDt(this.userStore.dt);
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
