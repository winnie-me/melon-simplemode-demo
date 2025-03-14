<template>
  <v-container fluid>

    <v-row>
      <v-col cols="12">

        <SlotItem title="ex. 유저별 시드곡 [곡목록이면 뭐든 가능]" :elevation="0">
          <UserSeedSongSlot/>
        </SlotItem>

      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <SlotItem title="곡별 태그별 관련곡 (위에서 곡을 선택해주세요)">
          <DetailTagView />
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

export default {
  components: {
    DetailTagView,
    SlotItem,
    UserSeedSongSlot,
    TrendRevivalSlot
  },
  data() {
    return {
      // userStore: useUserStore(),
      selectedSongStore: useSelectedSongStore(),
    };
  },
  mounted() {
    this.selectedSongStore.$patch({ selectedSong: null });
  },
  computed: {
  },
  watch: {
  },

  methods: {

  }
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

::v-deep(.v-slide-group__prev),
::v-deep(.v-slide-group__next) {
  display: none !important;
}

.song-item {
  width: 320px;
}
</style>
