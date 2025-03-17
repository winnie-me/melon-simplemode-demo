<template>
  <v-slide-group>

    <v-slide-group-item>
      <div class="d-flex flex-column ma-1">
        <h3 class="mx-2 mb-2">2월 15일</h3>
        <ListeningPersonalityItem/>
        <ListeningPersonalityItem :title="'국내'"/>
        <ListeningPersonalityItem :title="'해외'"/>
      </div>
    </v-slide-group-item>
    <v-slide-group-item>
      <div class="d-flex flex-column ma-1">
        <h3 class="mx-2 mb-2">2월 16일</h3>
        <ListeningPersonalityItem/>
        <ListeningPersonalityItem :title="'국내'"/>
        <ListeningPersonalityItem :title="'해외'"/>
      </div>
    </v-slide-group-item>
    <v-slide-group-item>
      <div class="d-flex flex-column ma-1">
        <h3 class="mx-2 mb-2">2월 17일</h3>
        <ListeningPersonalityItem/>
        <ListeningPersonalityItem :title="'국내'"/>
        <ListeningPersonalityItem :title="'해외'"/>
      </div>
    </v-slide-group-item>
    <v-slide-group-item>
      <div class="d-flex flex-column ma-1">
        <h3 class="mx-2 mb-2">2월 18일</h3>
        <ListeningPersonalityItem/>
        <ListeningPersonalityItem :title="'국내'"/>
        <ListeningPersonalityItem :title="'해외'"/>
      </div>
    </v-slide-group-item>
    <v-slide-group-item>
      <div class="d-flex flex-column ma-1">
        <h3 class="mx-2 mb-2">2월 19일</h3>
        <ListeningPersonalityItem/>
        <ListeningPersonalityItem :title="'국내'"/>
        <ListeningPersonalityItem :title="'해외'"/>
      </div>
    </v-slide-group-item>

  </v-slide-group>
</template>
<script>

import SongItem from "@/components/SongItem.vue";
import ArtistItem from "@/components/ArtistItem.vue";
import {useUserStore} from "@/stores/userStore.js";
import ListeningPersonalityItem from "@/components/ListeningPersonalityItem.vue";

export default {
  components: {
    ListeningPersonalityItem,
    ArtistItem,
    SongItem
    // SongItem
  },
  props: {},
  setup() {
    const store = useUserStore();
    return {
      store,
    };
  },
  data() {
    return {
      cards: [
        {title: "비오는 날 듣기 좋은 카더가든 노래", src: "https://cdn.vuetifyjs.com/images/cards/house.jpg"},
        {title: "드라이브할 때 듣기 좋은 브릿팝", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg"},
        {title: "김건모의 발라드", src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg"},
        {title: "마이앤트메리 대표곡", src: "https://cdn.vuetifyjs.com/images/cards/house.jpg"},
        {title: "시부야케이 대표곡", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg"},
        {title: "Bruno Mars 숨은 명곡", src: "https://cdn.vuetifyjs.com/images/cards/plane.jpg"},
      ],
      artistLists: [], // ✅ 2차원 배열 저장
    };
  },
  mounted() {
    // this.fetchInitialData();
  },
  computed: {},
  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/artist-collections/user-profile-artists?user_id=${this.store.selectedUserId}`);
        const data = await response.json();

        this.splitArtists(data.data[0].artists)
        // this.songs = data.data[0].songs;
        console.log('this.artists', data.data[0].artists)

      } catch (error) {
        console.error('Error fetching data:', error);
        this.artistLists = [];
      }
    },
    splitArtists(allArtists) { // 화면에 맞게 카드당 4곡씩 넣기
      const chunkSize = 2; // ✅ 4개씩 분할
      this.artistLists = [];

      for (let i = 0; i < allArtists.length; i += chunkSize) {
        this.artistLists.push(allArtists.slice(i, i + chunkSize));
      }
    },
  },
};
</script>
<style scoped>
/* 가로 스크롤 가능하도록 설정 */
.v-slide-group {
  white-space: nowrap;
  overflow-x: auto;
}

/* 개별 컬럼 스타일 */
.column-container {
  min-width: 200px; /* 각 컬럼의 최소 너비 */
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
