<template>
  <v-slide-group>

    <v-slide-group-item v-if="artistLists.length > 0 && artistLists[0].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[0]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="artistLists.length > 1 && artistLists[1].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[1]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="artistLists.length > 2 && artistLists[2].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[2]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="artistLists.length > 3 && artistLists[3].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[3]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="artistLists.length > 4 && artistLists[4].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[4]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="artistLists.length > 5 && artistLists[5].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[5]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="artistLists.length > 6 && artistLists[6].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[6]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="artistLists.length > 7 && artistLists[7].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[7]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="artistLists.length > 8 && artistLists[8].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[8]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="artistLists.length > 9 && artistLists[9].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[9]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="artistLists.length > 10 && artistLists[10].length > 0">
      <div class="d-flex flex-column ma-1">
        <ArtistItem
          v-for="item in artistLists[10]"
          :key="item.artist_id"
          :artist="item"
          :persistState="persistState"
        />
      </div>
    </v-slide-group-item>

  </v-slide-group>
</template>
<script>

// import SongItem from "@/components/SongItem.vue";
import ArtistItem from "@/components/ArtistItem.vue";
import {useUserStore} from "@/stores/userStore.js";

export default {
  components: {
    ArtistItem,
  },
  props: {
    persistState: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
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
    this.fetchInitialData();
  },
  computed: {},
  methods: {
    async fetchInitialData() {
      console.log('UserSeedArtistSlot.vue')
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
