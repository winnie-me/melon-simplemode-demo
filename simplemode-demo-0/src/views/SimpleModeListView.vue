<template>
  <v-container fluid>

    <v-row>
      <v-col cols="12">

        <SlotItem title="유저별 시드곡">
          <template #subtitle>
            <a
              :href="'https://www.melon.com/mymusic/recent/mymusicrecentsong_list.htm?memberKey='+store.selectedUserId"
              target="_blank">최근들은</a>
          </template>
          <UserSeedSongSlot/>
        </SlotItem>

      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <SlotItem title="역주행곡">
          <TrendRevivalSlot/>
        </SlotItem>
      </v-col>
    </v-row> <!-- TagBasedSongExplorer -->

  </v-container>
</template>


<script>
import {useUserStore} from "@/stores/userStore";
import SlotItem from "@/components/SlotItem.vue";
import UserSeedSongSlot from "@/components/UserSeedSongSlot.vue";
import TrendRevivalSlot from "@/components/TrendRevivalSlot.vue";

export default {
  components: {
    SlotItem,
    UserSeedSongSlot,
    TrendRevivalSlot
  },
  data() {
    return {
      store: useUserStore(),
    };
  },
  mounted() {
  },
  computed: {
    /*    computedSelectedUserId() {
          return this.store.selectedUserId; // store의 selectedUserId를 computed로 반환
        }*/
  },
  watch: {
    /*    computedSelectedUserId(newVal) {
          if (newVal) {
            this.selectedUserId = newVal; // 반응형 변수에 저장
            // this.fetchInitialData();
          }
        }*/
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

::v-deep(.v-slide-group__prev),
::v-deep(.v-slide-group__next) {
  display: none !important;
}

.song-item {
  width: 300px;
}


::v-deep(.v-card-title + .v-card-text) {
  padding: 0;
}


/*::v-deep(.v-card)
{
  padding: 8px !important; !* 기본 padding을 강제로 덮어쓰기 *!
}*/

/*::v-deep(.v-list-item)
{
  padding: 4px !important; !* 기본 padding을 강제로 덮어쓰기 *!
}*/
</style>
