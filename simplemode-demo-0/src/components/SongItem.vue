<template>

  <v-tooltip :disabled="true" class="custom-tooltip" location="bottom">
    <template v-slot:activator="{ props }">

      <v-list-item @click="playSong(song);persistStateStore(song)" v-if="song.song_id"
                   v-bind="props">
        <template v-slot:prepend>
          <v-avatar rounded="lg" size="48">
            <img
              :src="`https://cdnimg.melon.co.kr/${song.img}/melon/resize/282/quality/80/optimize`"
              class="avatar-img"
            />
          </v-avatar>
        </template>
        <v-list-item-title>{{ decodeText(song.title) }}</v-list-item-title>
        <v-list-item-subtitle>
          {{ decodeText(song.artist_names.join(",")) }}
        </v-list-item-subtitle>
      </v-list-item>

    </template>
    점수:
    {{ song.const_score }}
  </v-tooltip>

</template>

<script>
import {useSelectedSongStore} from "@/stores/selectedSongStore.js";

export default {
  props: {
    song: {
      type: Object,
      required: true,
    },
    disableTooltip: {
      type: Boolean,
      required: false,
      default: true,
    },
    persistState: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  setup(props) {
    const selectedSongStore = useSelectedSongStore();
    return {
      selectedSongStore,
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
    playSong(song) {
      event.stopPropagation()

      switch (this.$getOS()) {
        case "Android":
        case "iOS":
          window.location.href = `melonapp://play?cid=${song.song_id}&ctype=1&openplayer=N&releaseRepeat=N&excludeSongList=Y`
          console.log("Android|iOS");
          break;
        case "macOS":
          window.location.href = `melonplayer://play?ref=XXX&cid=${song.song_id}&ctype=song&menuid=1234`; // URL 실행
          break;
        // case "Windows":
        //   console.log("목요일");
        //   break;
        default:
          console.log("잘못된 입력");
      }
    },
    persistStateStore(target) {
      if (this.persistState) {
        this.selectedSongStore.$patch({selectedSong: target});
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
