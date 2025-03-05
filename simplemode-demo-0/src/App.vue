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
        <v-list-item link to="/ex-card-0">Card</v-list-item>
        <v-list-item link to="/accordion-list-0">Expand</v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- 상단 앱 바 -->
<!--    <v-app-bar elevation="4">
      <v-app-bar-nav-icon @click="toggleDrawer" v-if="$vuetify.display.smAndDown"></v-app-bar-nav-icon>
      <v-toolbar-title>My App</v-toolbar-title>
    </v-app-bar>-->

    <!-- 메인 컨텐츠 영역 -->
    <v-main>
      <v-container fluid>
        <RouterView />
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue';

const drawer = ref(true);

const toggleDrawer = () => {
  drawer.value = !drawer.value;
};
</script>
