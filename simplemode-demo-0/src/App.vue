<template>
  <v-app>

    <v-navigation-drawer
      v-model="drawer"
      :width="153"
      :permanent="$vuetify.display.mdAndUp"
      :temporary="!$vuetify.display.mdAndUp">
      <v-list-item title="AI 기능"/>
      <v-divider/>

<!--          <v-select
            label="user id"
            :items="store.userList"
            style="max-width: 200px;"
            v-model="store.selectedUserId"
          />-->
<!--
            v-model="tmpUserId"
            @keydown.enter="onEnter"
-->
          <v-autocomplete
            label="memberKey"
            :items="store.userList"
            :model-value="store.selectedUserId"
            @update:model-value="onUserIdSelected"
          />
        <v-list-item link to="/simplemode-list">전체 기능 목록</v-list-item>
        <v-list-item link to="/tag-based-song-explorer">태그 탐색 기능</v-list-item>
        <!--        <v-list-item link to="/">개인화 플리 확인</v-list-item>-->
    </v-navigation-drawer>

    <!-- 메인 컨텐츠 영역 -->
    <v-main style="max-width: 100%; width: 100%;">
      <v-container :style="{ width: mainWidth }" class="content-container">
        <RouterView/>
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
      // userIds: ['46536104', '59040609', '37884321', '52894215', '59337842', '28350538'],
      tmpUserId: null,
    };
  },
  mounted() {
    this.tmpUserId = this.store.selectedUserId
  },
  computed: {
    mainWidth() {
      return "90vw";
    },
  },
  methods: {
/*    onEnter(event){
      console.log('updateSelectedUser enter', event)
      // this.store.setUserId(this.tmpUserId)
    },*/
    onUserIdSelected(newUserId){
      console.log('value changed', newUserId)
      this.store.setUserId(newUserId)
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
