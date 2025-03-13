<template>
  <v-container>
    <v-slide-group show-arrows>

      <v-slide-group-item v-for="(card, index) in cards" :key="index">
        <v-card class="image-card mx-2" elevation="4" @click="navigateTo('/list-0',card)">
          <v-img
            :src="card.src"
            class="align-end"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="200px"
            cover
          >
            <v-card-title class="text-white" v-text="card.title"></v-card-title>
          </v-img>
        </v-card>
      </v-slide-group-item>
    </v-slide-group>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      cards: [
        {title: "2025-02", src: "https://cdn.vuetifyjs.com/images/cards/house.jpg"},
        {title: "2025-01", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg"},
        {title: "2024-12", src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg"},
        {title: "2024-11", src: "https://cdn.vuetifyjs.com/images/cards/house.jpg"},
        {title: "2024-10", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg"},
        {title: "2024-09", src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg"},
      ]
    };
  },
  methods: {
    navigateTo(path, theme) {
      this.$router.push({path: path, query: {id: theme.id, name: theme.name}});
    }
  }
};
</script>

<style scoped>
.image-card {
  width: 150px;
  height: 100px;
  border-radius: 10px;
  overflow: hidden;
}
</style>
