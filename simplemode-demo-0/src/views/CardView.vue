<template>
  <v-container>
    <v-slide-group show-arrows>
      <v-slide-group-item v-for="(theme, index) in themes" :key="index">
        <v-card
          :style="{ backgroundColor: theme.color }"
          class="theme-card mx-2"
          elevation="4"
          @click="navigateTo('/list-0',theme)"
        >
          <v-card-title class="theme-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          </v-card-title>
        </v-card>
      </v-slide-group-item>
    </v-slide-group>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      themes: [
        {name: "Nature", color: "#4CAF50", id: 1},
        {name: "Ocean", color: "#2196F3", id: 2},
        {name: "Sunset", color: "#FF9800", id: 3},
        {name: "Galaxy", color: "#673AB7", id: 4},
        {name: "Desert", color: "#FF5722", id: 5},
        {name: "Mountain", color: "#795548", id: 6}
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
.theme-card {
  width: 250px;
  height: 150px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  border-radius: 10px;
  padding: 16px;
  text-align: center;
  cursor: pointer;
  transition: transform 0.2s;
}

.theme-card:hover {
  transform: scale(1.05);
}

.theme-text {
  font-size: 24px;
  text-align: center;
  word-wrap: break-word;
  white-space: normal;
  overflow-wrap: break-word;
}
</style>
