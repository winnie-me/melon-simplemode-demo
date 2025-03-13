<template>
  <v-list-item @click="playSong(song)" v-if="song.song_id">
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

<script>
import {useSelectedSongStore} from "@/stores/selectedSongStore.js";

export default {
  props: {
    song: {
      type: Object,
      required: true,
    },
  },
  setup() {
    const selectedSongStore = useSelectedSongStore();
    return {
      selectedSongStore,
    };
  },
  data() {
    return {
      domParser: new DOMParser(),
      // selectedSongStore: useSelectedSongStore(),
    };
  },
  methods: {
    decodeText(html) {
      const doc = this.domParser.parseFromString(html, "text/html");
      return doc.documentElement.textContent;
    },
    playSong(song) {
      window.location.href = `melonplayer://play?ref=XXX&cid=${song.song_id}&ctype=song&menuid=1234`; // URL 실행
      event.stopPropagation()
      // this.selectedSongStore.selectedSong = song
      this.selectedSongStore.$patch({ selectedSong: song });
    }
  },
};
</script>

<style scoped>
.song-item {
  width: 300px;
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
