<template>
  <v-container fluid>

    <v-row>
      <v-col cols="12">
        <v-slide-group v-model="selectedTag" center-active>
          <v-slide-group-item v-for="(tagName, tagIndex) in tagList" :key="tagIndex" :value="tagName">
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
          <SongListItem
            v-for="item in songList"
            :key="item.song_id"
            :song="item"
            @playSong="playSong"
          />
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import SongListItem from "@/components/SongListItem.vue";
import {useRoute} from "vue-router";

export default {
  components: {SongListItem},
  setup() {
    const route = useRoute();
    return {
      route,
    };
  },
  props: {
    /*    cardTitle: {
          type: String,
          required: true,
        },*/
  },
  data() {
    return {
      tagList: [],
      songList: [],
      selectedTag: null,
    };
  },
  watch: {
    /*    cardTitle(newVal) {
          if (!newVal) {
            this.songList = [];
            // this.subSongList = [];
          }
          this.fetchInitialData();
        }*/
  },
  mounted() {
    this.selectedTag = this.route.query.tag
    console.log('title', this.selectedTag)
    this.fetchInitialData(this.route.query.tag);
    this.fetchTagData();
  },
  methods: {
    async fetchInitialData(title) {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/trending-revival/detail?peak_month=${title ?? this.selectedTag}`); // 실제 API URL로 변경
        const data = await response.json();
        this.songList = data.data[0].songs
        console.log('response', this.selectedTag, data.data[0].songs)
        this.selectedTag = title
      } catch (error) {
        console.error('Error fetching data:', error);
        this.songList = [];
      }
    },
    async fetchTagData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/trending-revival/list`);
        const data = await response.json();
        this.tagList = data.data[0].contents.map(item => item.title)
        // this.contents = data.data[0].contents;
        console.log('this.tagList', this.tagList)
      } catch (error) {
        console.error('Error fetching data:', error);
        this.tagList = [];
      }
    },
    playSong(song_id) {
      window.location.href = `melonplayer://play?ref=XXX&cid=${song_id}&ctype=song&menuid=1234`; // URL 실행
    }
  }
};
</script>

<style scoped>
.clickable-item {
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.avatar-img {
  width: 100%; /* 부모(v-avatar)의 너비를 100%로 설정 */
  height: 100%; /* 부모(v-avatar)의 높이를 100%로 설정 */
  object-fit: cover; /* 이미지가 꽉 차면서 비율을 유지하도록 설정 */
}

.list-container {
  max-width: 1200px; /* 너무 넓어지는 것을 방지 */
  margin: 0 auto; /* 중앙 정렬 */
}

::v-deep(.v-slide-group__prev),
::v-deep(.v-slide-group__next) {
  display: none !important;
}

.focused-btn {
  border: 2px solid blue !important;
  box-shadow: 0 0 8px blue !important;
}
</style>
