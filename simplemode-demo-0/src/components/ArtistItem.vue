<template>

  <v-card class="ma-1 d-flex flex-column align-center" elevation="0" style="width: 170px"
          @click="persistStateStore(artist)" :ripple="this.persistState"
          :style="{ 'pointer-events': !persistState ? 'none' : 'auto' }">
    <v-avatar rounded="circle" size="115">
      <img
        :src="`https://cdnimg.melon.co.kr/${artist.img}/melon/resize/282/quality/80/optimize`"
        class="avatar-img"/>
    </v-avatar>
    <v-card-subtitle class="my-1" style="color: black">{{
        decodeText(artist.artist_name)
      }}
    </v-card-subtitle>
  </v-card>

</template>

<script>
import {useSelectedArtistStore} from "@/stores/selectedArtistStore.js";

export default {
  props: {
    artist: {
      type: Object,
      required: true,
    },
    persistState: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  setup(props) {
    const selectedArtistStore = useSelectedArtistStore();
    return {
      selectedArtistStore,
    };
  },
  computed: {},
  data() {
    return {
      domParser: new DOMParser(),
    };
  },
  methods: {
    decodeText(html) {
      const doc = this.domParser.parseFromString(html, "text/html");
      return doc.documentElement.textContent;
    },
    persistStateStore(target) {
      if (this.persistState) {
        this.selectedArtistStore.$patch({selectedArtist: target});
      }
    }
  },
};
</script>

<style scoped>

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.custom-tooltip ::v-deep(.v-overlay__content) {
  background-color: #dcedc8 !important; /* ✅ Light Green Lighten-5 색상 */
  color: black !important; /* ✅ 텍스트 색상 변경 */
  opacity: 0.9;
}

</style>
