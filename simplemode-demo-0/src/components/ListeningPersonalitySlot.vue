<template>
  <v-slide-group>

    <v-slide-group-item>
      <!--        <h3 class="mx-2 mb-2">2월 15일</h3>-->
      <ListeningPersonalityItem :content="lp_all" v-if="lp_all"/>
    </v-slide-group-item>

    <v-slide-group-item>
      <ListeningPersonalityItem :title="'국내'" :content="lp_kpop" v-if="lp_kpop"/>
    </v-slide-group-item>

    <v-slide-group-item>
      <ListeningPersonalityItem :title="'해외'" :content="lp_pop" v-if="lp_pop"/>
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
      lp_all: null,
      lp_pop: null, // CC0014
      lp_kpop: null, // CC0006
    };
  },
  mounted() {
    this.fetchInitialData();
  },
  computed: {},
  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/listening-personality/list?user_id=${this.store.selectedUserId}`);
        const data = await response.json();

        // 데이터 구조 확인 후 안전하게 접근
        if (!data || !data.data || !data.data[0] || !data.data[0].contents) {
          throw new Error("Invalid response structure: Missing contents");
        }

        // this.splitArtists(data.data[0].contents)
        // 데이터가 존재하는 경우에만 값을 할당
        this.lp_all = data.data[0].contents['all'] || null
        this.lp_pop = data.data[0].contents['CC0014'] || null
        this.lp_kpop = data.data[0].contents['CC0006'] || null


        console.log('this.lp', data.data[0].contents['all'])

      } catch (error) {
        console.error('Error fetching data:', error);
        // this.artistLists = [];
        this.lp_all = null
        this.lp_pop = null
        this.lp_kpop = null
      }
    },
    /*    splitArtists(allArtists) { // 화면에 맞게 카드당 4곡씩 넣기
          const chunkSize = 2; // ✅ 4개씩 분할
          this.artistLists = [];

          for (let i = 0; i < allArtists.length; i += chunkSize) {
            this.artistLists.push(allArtists.slice(i, i + chunkSize));
          }
        },*/
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
