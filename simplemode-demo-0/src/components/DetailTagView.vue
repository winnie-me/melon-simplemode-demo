<template>
  <v-container fluid>

    <v-row>
      <v-col cols="12">
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
        <v-slide-group class="px-2" v-model="selectedKeyword">
          <v-slide-group-item v-for="(tagInfo, tagIndex) in keywordList" :key="tagIndex"
                              :value="tagInfo.title" v-if="selectedSongStore.selectedSong">
            <v-btn class="mx-1"
                   density="compact" variant="tonal"
                   :color="selectedKeyword === tagInfo.title ? 'blue-accent-4' : 'green-darken-1'"
                   @click="loadSubSongList(selectedSongStore.selectedSong.song_id, tagInfo)">
              {{ tagInfo.title }}
            </v-btn>
          </v-slide-group-item>
        </v-slide-group>
      </v-col>
    </v-row>


    <!--    서브곡 -->
    <v-row>
      <v-col cols="12">
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
import {useUserStore} from "@/stores/userStore.js";
import {nextTick} from "vue";

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
      selectedUserStore: useUserStore(), // selectedUserId
      selectedKeyword: "",
    };
  },
  watch: {

    "selectedSongStore.selectedSong": {
      handler(newVal, oldVal) {
        console.log("선택된 곡 변경:", newVal ? newVal.title : newVal);
        this.fetchInitialData();
        this.keywordList = [];
        this.subSongList = [];
        this.selectedKeyword = ""
      },
      deep: true, // ✅ 객체 내부 속성까지 감지할 경우 필요
      immediate: true, // ✅ 초기 실행 여부 (옵션)
    },
    "selectedUserStore.selectedUserId": {
      handler(newVal, oldVal) {
        console.log("유저 변경:", newVal);
        // this.fetchInitialData();
        this.selectedSongStore.$patch({selectedSong: null});
        this.keywordList = [];
        this.subSongList = [];
        this.selectedKeyword = ""
      },
      deep: true, // ✅ 객체 내부 속성까지 감지할 경우 필요
      immediate: true, // ✅ 초기 실행 여부 (옵션)
    },

  },
  mounted() {
    this.fetchInitialData();
  },
  methods: {
    async fetchInitialData() {
      console.log('fetchInitialData')
      if (!this.selectedSongStore.selectedSong) return;

      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/collections/song-key-mapping?song_id=${this.selectedSongStore.selectedSong.song_id}`); // 실제 API URL로 변경
        const data = await response.json();
        console.log('keys', data.data[0].keys)
        this.items = data.data; // 데이터를 상태에 저장
        this.keywordList = data.data[0].keys

        // ✅ 첫 번째 키워드를 자동 선택
        if (this.keywordList.length > 0) {
          this.selectedKeyword = this.keywordList[0].title;

          // ✅ DOM 업데이트 후 클릭 이벤트 실행
          await nextTick();
          // this.handleKeywordClick(this.selectedKeyword);
          await this.loadSubSongList(this.selectedSongStore.selectedSong.song_id, this.keywordList[0])
        }
      } catch (error) {
        console.error('Error fetching data:', error);
        this.items = [];
        this.keywordList = [];

      }
    },
    async loadSubSongList(song_id, keyInfo) {
      this.selectedKeyword = keyInfo.title

      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/collections/song-key-collection?song_id=${song_id}&key_id=${keyInfo.id}`); // 실제 API URL로 변경
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

::v-deep(.v-col) {
  padding: 4px;
}
</style>
