<template>
  <!--  <v-container>-->
  <v-slide-group>

    <v-slide-group-item v-for="(card, index) in cards" :key="index">
      <v-card class="image-card mx-2" elevation="4" @click="handleClick(card)">
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
  <!--  </v-container>-->
</template>

<script>
export default {
  data() {
    return {

      cards: [
        {title: "비오는 날 듣기 좋은 카더가든 노래", src: "https://cdn.vuetifyjs.com/images/cards/house.jpg"},
        {title: "드라이브할 때 듣기 좋은 브릿팝", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg"},
        {title: "김건모의 발라드", src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg"},
        {title: "마이앤트메리 대표곡", src: "https://cdn.vuetifyjs.com/images/cards/house.jpg"},
        {title: "시부야케이 대표곡", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg"},
        {title: "Bruno Mars 숨은 명곡", src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg"},
      ]
    };
  },
  emits: ["clickCard"],
  methods: {
    handleClick(card) {
      this.$emit("clickCard", card.title);
    },
    navigateTo(path, theme) {
      this.$router.push({path: path, query: {id: theme.id, name: theme.name}});
    },

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

/*::v-deep(.v-slide-group__prev),
::v-deep(.v-slide-group__next) {
  display: none !important;
}*/
</style>
