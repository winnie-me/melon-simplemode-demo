<template>
  <v-container fluid>

    <v-row>
      <v-col cols="12">
        <v-slide-group v-model="selectedTag" center-active>
          <v-slide-group-item v-for="(tagName, tagIndex) in tagList" :key="tagIndex"
                              :value="tagName">
            <v-btn class="mx-1" density="compact" variant="tonal"
                   :color="selectedTag === tagName ? 'blue-accent-4' : 'green-darken-1'"
                   @click="fetchInitialData(tagName)">
              {{ tagName }}
            </v-btn>
          </v-slide-group-item>
        </v-slide-group>
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
      tagList: [],
      songList: [],
      selectedTag: null,
    };
  },
  watch: {},
  mounted() {
    this.selectedTag = this.route.query.tag
    console.log('title', this.selectedTag)

    this.fetchInitialData(this.route.query.tag);
    this.fetchTagData();
  },
  methods: {
    async fetchInitialData(title) {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/seasonality/played-detail?seasonality=${title ?? this.selectedTag}`)
        const data = await response.json();
        this.songList = data.data[0].songs
        // console.log('response', this.selectedTag, data.data[0].songs)
        this.selectedTag = title
      } catch (error) {
        console.error('Error fetching data:', error);
        this.songList = [];
      }
    },
    async fetchTagData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/seasonality/played-list`);
        const data = await response.json();
        this.tagList = data.data[0].contents.map(item => item.title)

        // console.log('this.tagList', this.tagList)
      } catch (error) {
        console.error('Error fetching data:', error);
        this.tagList = [];
      }
    },

  }
};
</script>

<style scoped>

::v-deep(.v-slide-group__prev),
::v-deep(.v-slide-group__next) {
  display: none !important;
}

</style>
