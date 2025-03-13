<template>
  <v-list-item @click="handleClick">
    <template v-slot:prepend>
      <v-avatar rounded="lg" size="48">
        <img
          :src="`https://cdnimg.melon.co.kr/${song.img}/melon/resize/282/quality/80/optimize`"
          class="avatar-img"
        />
      </v-avatar>
    </template>
    <v-list-item-title>{{ song.title }}</v-list-item-title>
    <v-list-item-subtitle>
      {{ song.artist_names.join(",") }}
    </v-list-item-subtitle>
  </v-list-item>
</template>

<script>
export default {
  props: {
    song: {
      type: Object,
      required: true,
    },
  },
  emits: ["playSong", "clearSongs"],
  methods: {
    handleClick() {
      this.$emit("playSong", this.song.song_id);
      this.$emit("clearSongs");
    },
  },
};
</script>
