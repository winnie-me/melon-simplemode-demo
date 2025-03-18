<template>

  <v-card :to="navigateObj" color="white"
          :style="{ padding: '0px', width: cardWidth }" :elevation="0">
    <v-card-title class="white--text text-h6">
      {{ content.title }}
    </v-card-title>
    <v-card-text>
      <v-list>
        <SongItem
          v-for="item in content.songs.slice(0, 4)"
          :key="item.song_id"
          :song="item"
          :disableTooltip="disableTooltip"
        />
      </v-list>
    </v-card-text>
  </v-card>

</template>
<script>
import SongItem from "@/components/SongItem.vue"

export default {
  name: 'SongListCard',
  components: {SongItem},
  props: {
    content: {
      type: Object,
      required: true,
    },
    disableTooltip: {
      type: Boolean,
      required: false,
      default: true,
    },
    cardWidth: {
      type: String,
      required: false,
      default: '300px',
    },
    navigateObj: {
      type: Object,
      required: false,
      default: {path: '/'} // , query: {tag: '2023-09'}
    }
  }
}
</script>

