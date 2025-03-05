<template>
  <v-container class="music-player">
    <!-- 현재 재생 중인 곡 -->
    <v-card class="player-card">
      <v-row align="center">
        <v-col cols="2">
          <v-img :src="currentTrack.image" contain height="50"></v-img>
        </v-col>
        <v-col>
          <strong>{{ currentTrack.title }}</strong> - {{ currentTrack.artist }}
        </v-col>
        <v-col cols="2">
          <v-btn icon @click="togglePlay">
            <v-icon>{{ isPlaying ? 'mdi-pause' : 'mdi-play' }}</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-card>

    <!-- 플레이리스트 -->
    <v-list>
      <v-list-item
        v-for="(track, index) in playlist"
        :key="track.id"
        @click="playTrack(track, index)"
      >
        <template v-slot:default>
          <v-row align="center">
            <v-col cols="2">
              <v-img :src="track.image" contain height="50"></v-img>
            </v-col>
            <v-col>
              <span>{{ track.title }}</span> - <small>{{ track.artist }}</small>
            </v-col>
          </v-row>
        </template>
      </v-list-item>
    </v-list>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      isPlaying: false,
      currentTrack: {
        id: null,
        title: 'Cruel Summer',
        artist: 'Taylor Swift',
        image: 'https://link-to-cruel-summer-image.jpg',
      },
      playlist: [
        { id: 1, title: 'toxic till the end', artist: '로제', image: 'https://link-to-image1.jpg' },
        { id: 2, title: 'Obsessed', artist: 'Ayumu Imazu', image: 'https://link-to-image2.jpg' },
        { id: 3, title: 'Toothbrush', artist: 'Marielle Kraft', image: 'https://link-to-image3.jpg' },
        { id: 4, title: 'Tango', artist: 'ABIR', image: 'https://link-to-image4.jpg' },
        { id: 5, title: 'next door', artist: 'Amelia Moore & ASTN', image: 'https://link-to-image5.jpg' },
        { id: 6, title: 'Birthday', artist: 'Anne-Marie', image: 'https://link-to-image6.jpg' },
        { id: 7, title: 'I Like Me Better', artist: 'Lauv', image: 'https://link-to-image7.jpg' },
      ],
    };
  },
  methods: {
    togglePlay() {
      this.isPlaying = !this.isPlaying;
    },
    playTrack(track, index) {
      // 현재 재생 중인 곡을 업데이트
      this.currentTrack = track;

      // 플레이리스트에서 해당 곡 제거하고, 컨트롤러 바로 밑에 삽입
      this.playlist.splice(index, 1); // 기존 위치에서 제거
      this.playlist.unshift(track); // 컨트롤러 아래로 이동
    },
  },
};
</script>

<style scoped>
.music-player {
  max-width: 500px;
  margin: auto;
}
.player-card {
  padding: 10px;
  margin-bottom: 10px;
}
.v-list-item {
  cursor: pointer;
}
</style>
