<template>
  <v-container fluid class="list-container">
    <v-row>
      <v-col cols="12" sm="12" md="12" lg="12">
        <v-list>
          <SongListItem
            v-if="selectedSongStore.selectedSong"
            :song="selectedSongStore.selectedSong"
            @playSong="playSong"
          />
        </v-list>
      </v-col>
    </v-row>

    <!-- 태그 -->
    <v-row>
      <v-col cols="12">
        <v-slide-group show-arrows class="pa-2">
          <v-slide-group-item v-for="(tagInfo, tagIndex) in keywordList" :key="tagIndex" v-if="selectedSongStore.selectedSong">
            <v-btn class="mx-1" density="compact" variant="tonal" color="green-darken-1"
                   @click="loadSubSongList(selectedSongStore.selectedSong.song_id, tagInfo.id)">
              {{ tagInfo.title }}
            </v-btn>
          </v-slide-group-item>
        </v-slide-group>
      </v-col>
    </v-row>


    <!--    서브곡 -->
    <v-row>
      <v-col cols="12" sm="12" md="12" lg="12">
        <v-list>
          <SongListItem
            v-for="item in subSongList"
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
import {useSelectedSongStore} from "@/stores/selectedSongStore.js";

export default {
  components: {SongListItem},
  props: {
/*    selectedSong: {
      type: Object,
      default: null // 초기값을 null로 설정
    }*/
  },
  data() {
    return {
      items: [],
      keywordList: [],
      subSongList: [],
      selectedSongStore: useSelectedSongStore(),
    };
  },
  watch: {
    selectedSong(newVal) {
      if (!newVal) {
        this.keywordList = [];
        this.subSongList = [];
      }
      this.fetchInitialData();
    }
  },
  mounted() {
    this.fetchInitialData();
  },
  methods: {
    async fetchInitialData() {
      if (!this.selectedSongStore.selectedSong) return;

      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/collections/song-key-mapping?song_id=${this.selectedSongStore.selectedSong.song_id}`); // 실제 API URL로 변경
        const data = await response.json();
        console.log('keys', data.data[0].keys)
        this.items = data.data; // 데이터를 상태에 저장
        this.keywordList = data.data[0].keys
      } catch (error) {
        console.error('Error fetching data:', error);
        this.items = [];
        this.keywordList = [];

      }
    },
    async loadSubSongList(song_id, key_id) {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/collections/song-key-collection?song_id=${song_id}&key_id=${key_id}`); // 실제 API URL로 변경
        const data = await response.json();
        console.log('loadSubSongList', data.data[0].songs)
        // this.items = data.data; // 데이터를 상태에 저장
        // this.keywordList = data.data[0].keys
        this.subSongList = data.data[0].songs
      } catch (error) {
        console.error('Error fetching data:', error);
        this.items = [];
      }
    },
    playSong(song_id) {
      const url = `melonplayer://play?ref=XXX&cid=${song_id}&ctype=song&menuid=1234`;
      window.location.href = url; // URL 실행
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
</style>
