<template>
  <v-container fluid>

    <v-row>
      <v-col cols="12">
        <h2 class="ma-1" v-if="customItem">{{ customItem.title }}</h2>
        <v-chip v-if="customItem" class="mx-1" density="compact" variant="tonal"
                :color="'green-darken-1'">
          {{ 'theme: ' + customItem.theme }}
        </v-chip>
        <v-chip v-if="customItem" class="mx-1" density="compact" variant="tonal"
                :color="'green-darken-1'">
          {{ 'style: ' + customItem.style }}
        </v-chip>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-list>
          <SongItem
            v-for="item in songList"
            :key="item.song_id"
            :song="item"
          />
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import SongItem from "@/components/SongItem.vue";
import {useRoute} from "vue-router";

export default {
  components: {SongItem},
  setup() {
    const route = useRoute();
    return {
      route,
    };
  },
  props: {},
  data() {
    return {
      customItem: null,
      songList: [],
    };
  },
  watch: {},
  mounted() {
    this.fetchInitialData();
  },
  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/custom-collections/custom-collection?id=${this.route.query.id}`)
        const data = await response.json();
        this.customItem = data.data[0]
        this.songList = data.data[0].songs
        // console.log('response', data.data[0].songs)
      } catch (error) {
        console.error('Error fetching data:', error);
        this.songList = [];
      }
    },
  }
};
</script>

