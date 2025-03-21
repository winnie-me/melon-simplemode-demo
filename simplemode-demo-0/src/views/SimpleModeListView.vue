<template>
  <v-container fluid>

    <v-row>
      <v-col cols="12">
        <SlotItem title="유저별 시드 테마" :elevation="0">
          <UserSeedCustomSlot/>
        </SlotItem>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <SlotItem title="유저별 시드곡" :elevation="0">
          <template #subtitle>
            <a target="_blank"
               :href="'https://www.melon.com/mymusic/recent/mymusicrecentsong_list.htm?memberKey='+store.selectedUserId">최근들은</a>
          </template>
          <UserSeedSongSlot/>
        </SlotItem>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <SlotItem title="유저별 시드 아티스트" :elevation="0">
          <UserSeedArtistSlot/>
        </SlotItem>
      </v-col>
    </v-row>


    <v-row>
      <v-col cols="12">
        <SlotItem title="역주행곡" :elevation="0">
          <TrendRevivalSlot/>
        </SlotItem>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <SlotItem title="Seasonality" :elevation="0">
          <SeasonalitySlot/>
        </SlotItem>
      </v-col>
    </v-row>

    <!--    <v-row>
          <v-col cols="12">
            <SlotItem title="Listening Personality">
              <ListeningPersonalitySlot/>
            </SlotItem>
          </v-col>
        </v-row>-->

    <!--    <v-row>
          <v-col cols="12">
            <SlotItem title="유저별 팬덤 아티스트">
            </SlotItem>
          </v-col>
        </v-row>-->

  </v-container>
</template>


<script>
import {useUserStore} from "@/stores/userStore";
import SlotItem from "@/components/SlotItem.vue";
import UserSeedSongSlot from "@/components/UserSeedSongSlot.vue";
import TrendRevivalSlot from "@/components/TrendRevivalSlot.vue";
import UserSeedCustomSlot from "@/components/UserSeedCustomSlot.vue";
import ExampleCardView from "@/views/ExampleCardView.vue";
import UserSeedArtistSlot from "@/components/UserSeedArtistSlot.vue";
import ListeningPersonalitySlot from "@/components/ListeningPersonalitySlot.vue";
import SeasonalitySlot from "@/components/SeasonalitySlot.vue";

export default {
  components: {
    SeasonalitySlot,
    ListeningPersonalitySlot,
    UserSeedArtistSlot,
    UserSeedCustomSlot,
    SlotItem,
    UserSeedSongSlot,
    TrendRevivalSlot,
    ExampleCardView
  },
  data() {
    return {
      store: useUserStore(),
    };
  },
  mounted() {
  },
  computed: {},
  watch: {},

  methods: {}
};
</script>

<style scoped>

.content-container > * {
  flex-grow: 1; /* 내부 요소가 남은 공간을 전부 채움 */
  width: 100%;
  height: 100%;
}

::v-deep(.v-slide-group__prev),
::v-deep(.v-slide-group__next) {
  display: none !important;
}

::v-deep(.v-card-title + .v-card-text) {
  padding: 0;
}

</style>
