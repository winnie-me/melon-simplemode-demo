<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">

        <SlotItem title="" :elevation="0">
          <v-select
            v-model="selectedTaret"
            :items="items"
            item-title="title"
            item-value="value"
            label="target 곡 목록 유형"
          />
        </SlotItem>

      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">

        <SlotItem title="곡/아티스트 타입" :elevation="0">
          <UserSeedSongSlot v-if="selectedTaret === 'UserSeedSongs'"
                            :persistState="true"/>
          <UserSeedArtistSlot v-if="selectedTaret === 'UserSeedArtists'"
                              :persistState="true"/>
        </SlotItem>

      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <SlotItem title="곡/아티스트별 태그별 관련곡 (위에서 선택해주세요)">
          <DetailTagView :selected-type="selectedTaret"/>
        </SlotItem>
      </v-col>
    </v-row>

  </v-container>
</template>


<script>
import {useUserStore} from "@/stores/userStore";
import {useSelectedSongStore} from "@/stores/selectedSongStore.js";
import SlotItem from "@/components/SlotItem.vue";
import UserSeedSongSlot from "@/components/UserSeedSongSlot.vue";
import TrendRevivalSlot from "@/components/TrendRevivalSlot.vue";
import DetailTagView from "@/components/DetailTagView.vue";
import UserSeedArtistSlot from "@/components/UserSeedArtistSlot.vue";
import {useSelectedArtistStore} from "@/stores/selectedArtistStore.js";

export default {
  components: {
    UserSeedArtistSlot,
    DetailTagView,
    SlotItem,
    UserSeedSongSlot,
    TrendRevivalSlot
  },
  data() {
    return {
      // userStore: useUserStore(),
      selectedSongStore: useSelectedSongStore(),
      selectedArtistStore: useSelectedArtistStore(),

      items: [
        {
          title: '유저별 시드 곡',
          value: 'UserSeedSongs',
        },
        {
          title: '유저별 시드 아티스트',
          value: 'UserSeedArtists',
        },
      ],

      selectedTaret: 'UserSeedArtists',//'UserSeedSongs',
    };
  },
  mounted() {
    this.selectedSongStore.$patch({selectedSong: null});
    this.selectedArtistStore.$patch({selectedArtist: null});
  },
  computed: {},
  watch: {
    "selectedTaret": {
      handler(newVal, oldVal) {
        console.log("selectedTaret 변경:", newVal); //  ? newVal.title : newVal

        this.selectedSongStore.$patch({selectedSong: null});
        this.selectedArtistStore.$patch({selectedArtist: null})
        // this.fetchKeywordList();
        // this.keywordList = [];
        // this.subSongList = [];
        // this.selectedKeyword = ""
      },
    },
  },

  methods: {}
};
</script>

<style scoped>
.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.content-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  padding: 0px;
}

.content-container > * {
  flex-grow: 1; /* 내부 요소가 남은 공간을 전부 채움 */
  width: 100%;
  height: 100%;
}

/*.custom-slide-group {
  display: flex;
  gap: 12px; !* 요소 간 간격 *!
}*/

/*::v-deep(.v-slide-group__prev),
::v-deep(.v-slide-group__next) {
  display: none !important;
}*/

.song-item {
  width: 320px;
}
</style>

