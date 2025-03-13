<template>
  <!--  <v-container>-->
  <v-slide-group>
    <v-slide-group-item v-for="(content, index) in contents" :key="index">
      <v-card @click="navigateTo(content.title)">
        <v-card-title class="white--text text-h6">
          {{ content.title }}
        </v-card-title>
        <v-card-text>
          <v-list class="song-item">
            <SongListItem
              v-for="item in content.songs"
              :key="item.song_id"
              :song="item"
            />
          </v-list>
        </v-card-text>
      </v-card>
    </v-slide-group-item>


<!--    <v-slide-group-item v-for="(card, index) in cards" :key="index">
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
    </v-slide-group-item>-->
  </v-slide-group>
  <!--  </v-container>-->
</template>

<script>
import SongListItem from "@/components/SongListItem.vue";

export default {
  components: {SongListItem},
  data() {
    return {
      contents: [],
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
  // emits: ["clickCard"],
  mounted() {
    this.fetchInitialData();
  },
  methods: {
    handleClick(card) {
      this.$emit("clickCard", card.title);
    },
    navigateTo(title) {
      this.$router.push({path: '/trend-revival-list', query: {tag: title}});
    },

    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/trending-revival/list`);
        const data = await response.json();
        this.contents = data.data[0].contents;
        console.log('this.contents', data.data[0].contents)
      } catch (error) {
        console.error('Error fetching data:', error);
        this.contents = [];
      }
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

::v-deep(.v-slide-group__prev),
::v-deep(.v-slide-group__next) {
  display: none !important;
}

</style>
