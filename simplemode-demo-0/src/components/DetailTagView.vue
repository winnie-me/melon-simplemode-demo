<template>
  <v-container fluid>

    <v-row>
      <v-col cols="12">
        <v-list>
          <SongItem
            v-if="selectedSongStore.selectedSong && selectedType === 'UserSeedSongs'"
            :song="selectedSongStore.selectedSong"
          />
<!--
            :persistState="true"
            :persistState="true"
-->
          <ArtistItem
            v-if="selectedArtistStore.selectedArtist && selectedType === 'UserSeedArtists'"
            :artist="selectedArtistStore.selectedArtist"
          />
        </v-list>
      </v-col>
    </v-row>

    <!-- 태그 -->
    <v-row>
      <v-col cols="12">
        <v-slide-group class="px-2" v-model="selectedKeyword">
          <v-slide-group-item v-for="(tagInfo, tagIndex) in keywordList" :key="tagIndex"
                              :value="tagInfo.title"
                              v-if="selectedSongStore.selectedSong || selectedArtistStore.selectedArtist">
            <v-btn class="mx-1"
                   density="compact" variant="tonal"
                   :color="selectedKeyword === tagInfo.title ? 'blue-accent-4' : 'green-darken-1'"
                   @click="loadSubSongList(tagInfo)">
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
          <SongItem
            v-for="item in subSongList"
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
import {useSelectedSongStore} from "@/stores/selectedSongStore.js";
import {useUserStore} from "@/stores/userStore.js";
import {nextTick} from "vue";
import ArtistItem from "@/components/ArtistItem.vue";
import {useSelectedArtistStore} from "@/stores/selectedArtistStore.js";

export default {
  components: {ArtistItem, SongItem},
  props: {
    selectedType: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      keywordList: [],
      subSongList: [],
      selectedSongStore: useSelectedSongStore(),
      selectedArtistStore: useSelectedArtistStore(),
      selectedUserStore: useUserStore(),
      selectedKeyword: "",
    };
  },
  watch: {
    "selectedSongStore.selectedSong": {
      handler(newVal, oldVal) {
        console.log("선택된 곡 변경:", newVal ? newVal.title : newVal);
        this.fetchKeywordList();
        this.keywordList = [];
        this.subSongList = [];
        this.selectedKeyword = ""
      },
      deep: true, // ✅ 객체 내부 속성까지 감지할 경우 필요
      immediate: true, // ✅ 초기 실행 여부 (옵션)
    },

    "selectedArtistStore.selectedArtist": {
      handler(newVal, oldVal) {
        console.log("선택된 아티스트 변경:", newVal ? newVal.artist_name : newVal);
        this.fetchKeywordList();
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
    this.fetchKeywordList();
  },
  methods: {
    async fetchKeywordList() {
      if (!this.selectedSongStore.selectedSong && !this.selectedArtistStore.selectedArtist) return;

      try {
        const keywordListAPI = this.getKeywordListAPI();
        if (typeof keywordListAPI !== 'string') return

        const response = await fetch(keywordListAPI);
        const data = await response.json();

        this.keywordList = data.data[0].keys

        // ✅ 첫 번째 키워드를 자동 선택
        if (this.keywordList.length > 0) {
          this.selectedKeyword = this.keywordList[0].title;

          // ✅ DOM 업데이트 후 클릭 이벤트 실행
          await nextTick();
          await this.loadSubSongList(this.keywordList[0])
        }
      } catch (error) {
        console.error('Error fetching data:', error);
        this.keywordList = [];
      }
    },
    async loadSubSongList(keyInfo) {
      this.selectedKeyword = keyInfo.title

      try {
        const subSongListAPI = this.getSubSongListAPI(keyInfo);

        const response = await fetch(subSongListAPI)
        const data = await response.json();
        this.subSongList = data.data[0].songs
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    getKeywordListAPI() {
      let url;
      switch (this.selectedType) {
        case 'UserSeedSongs':
          url = `https://winnie-bigquery-api-77vot6b6va-du.a.run.app/collections/song-key-mapping?song_id=${this.selectedSongStore.selectedSong.song_id}`
          break
        case 'UserSeedArtists':
          url = `https://winnie-bigquery-api-77vot6b6va-du.a.run.app/artist-collections/artist-key-mapping?artist_id=${this.selectedArtistStore.selectedArtist.artist_id}`
          break
        default:
          return;
      }
      return url
    },
    getSubSongListAPI(keyInfo) {
      let url;
      switch (this.selectedType) {
        case 'UserSeedSongs':
          const song_id = this.selectedSongStore.selectedSong.song_id
          url = `https://winnie-bigquery-api-77vot6b6va-du.a.run.app/collections/song-key-collection?song_id=${song_id}&key_id=${keyInfo.id}`
          break
        case 'UserSeedArtists':
          const artist_id = this.selectedArtistStore.selectedArtist.artist_id
          url = `https://winnie-bigquery-api-77vot6b6va-du.a.run.app/artist-collections/artist-key-collection?artist_id=${artist_id}&key_id=${keyInfo.id}`
          break
        default:
          return;
      }
      return url
    },
  }
};
</script>

<style scoped>

::v-deep(.v-col) {
  padding: 4px;
}
</style>
