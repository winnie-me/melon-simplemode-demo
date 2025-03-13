<template>
  <v-slide-group>

    <v-slide-group-item>
      <v-list class="song-item">
        <SongListItem
          v-for="item in song_list_1"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>

    <v-slide-group-item>
      <v-list class="song-item">
        <SongListItem
          v-for="item in song_list_2"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item>
      <v-list class="song-item">
        <SongListItem
          v-for="item in song_list_3"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
    <v-slide-group-item>
      <v-list class="song-item">
        <SongListItem
          v-for="item in song_list_4"
          :key="item.song_id"
          :song="item"
        />
      </v-list>
    </v-slide-group-item>
  </v-slide-group>
</template>
<script>
import SongListItem from "@/components/SongListItem.vue";
import {useUserStore} from "@/stores/userStore.js";

export default {
  components: {
    SongListItem
  },
  props: {
  },
  setup() {
    const store = useUserStore();
    return {
      store,
    };
  },
  data() {
    return {
      songs: [],
      song_list_1: [],
      song_list_2: [],
      song_list_3: [],
      song_list_4: [],
    };
  },
  mounted() {
    this.fetchInitialData();
  },
  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/collections/user-profile-songs?user_id=${this.store.selectedUserId}`);
        const data = await response.json();
        this.songs = data.data[0].songs;
        console.log('this.songs', data.data[0].songs)

        this.song_list_1 = data.data[0].songs.slice(0, 4)
        this.song_list_2 = data.data[0].songs.slice(4, 8)
        this.song_list_3 = data.data[0].songs.slice(8, 12)
        this.song_list_4 = data.data[0].songs.slice(12, 16)
      } catch (error) {
        console.error('Error fetching data:', error);
        this.songs = [];
      }
    },
  },
};
</script>
<style>
.song-item {
  width: 320px;
}
</style>
