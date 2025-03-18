<template>
<!-- 글자만 있는 카드 col 당 2개씩 노출하는 레이아웃 -->
  <v-slide-group>

    <v-slide-group-item v-if="itemLists.length > 0 && itemLists[0].length > 0">
      <div class="d-flex flex-column ma-1">
        <CustomItem
          v-for="item in itemLists[0]"
          :key="item.const_id"
          :item="item"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="itemLists.length > 2 && itemLists[2].length > 0">
      <div class="d-flex flex-column ma-1">
        <CustomItem
          v-for="item in itemLists[2]"
          :key="item.const_id"
          :item="item"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="itemLists.length > 3 && itemLists[3].length > 0">
      <div class="d-flex flex-column ma-1">
        <CustomItem
          v-for="item in itemLists[3]"
          :key="item.const_id"
          :item="item"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="itemLists.length > 4 && itemLists[4].length > 0">
      <div class="d-flex flex-column ma-1">
        <CustomItem
          v-for="item in itemLists[4]"
          :key="item.const_id"
          :item="item"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="itemLists.length > 5 && itemLists[5].length > 0">
      <div class="d-flex flex-column ma-1">
        <CustomItem
          v-for="item in itemLists[5]"
          :key="item.const_id"
          :item="item"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="itemLists.length > 6 && itemLists[6].length > 0">
      <div class="d-flex flex-column ma-1">
        <CustomItem
          v-for="item in itemLists[6]"
          :key="item.const_id"
          :item="item"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="itemLists.length > 7 && itemLists[7].length > 0">
      <div class="d-flex flex-column ma-1">
        <CustomItem
          v-for="item in itemLists[7]"
          :key="item.const_id"
          :item="item"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="itemLists.length > 8 && itemLists[8].length > 0">
      <div class="d-flex flex-column ma-1">
        <CustomItem
          v-for="item in itemLists[8]"
          :key="item.const_id"
          :item="item"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="itemLists.length > 9 && itemLists[9].length > 0">
      <div class="d-flex flex-column ma-1">
        <CustomItem
          v-for="item in itemLists[9]"
          :key="item.const_id"
          :item="item"
        />
      </div>
    </v-slide-group-item>

    <v-slide-group-item v-if="itemLists.length > 10 && itemLists[10].length > 0">
      <div class="d-flex flex-column ma-1">
        <CustomItem
          v-for="item in itemLists[10]"
          :key="item.const_id"
          :item="item"
        />
      </div>
    </v-slide-group-item>

  </v-slide-group>

</template>
<script>
import SongItem from "@/components/SongItem.vue";
import {useUserStore} from "@/stores/userStore.js";
import CustomItem from "@/components/CustomItem.vue";

export default {
  components: {
    CustomItem,
    SongItem
  },
  props: {},
  setup() {
    const store = useUserStore();
    return {
      store,
    };
  },
  data() {
    return {
      card: {title: "Card 1", subtitle: "Subtitle 1", description: "Description 1"},
/*      imgList: [
        "https://cdn.vuetifyjs.com/images/cards/house.jpg",
        "https://cdn.vuetifyjs.com/images/cards/road.jpg",
        "https://cdn.vuetifyjs.com/images/cards/plane.jpg",
        "https://cdn.vuetifyjs.com/docs/images/cards/purple-flowers.jpg",
        "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
        "https://cdn.vuetifyjs.com/images/cards/foster.jpg",
        "https://cdn.vuetifyjs.com/images/cards/docks.jpg",
        "https://cdn.vuetifyjs.com/images/cards/cooking.png",
      ],*/
      cards: [
        {id: 0, title: "비오는 날 듣기 좋은 카더가든 노래", src: "https://cdn.vuetifyjs.com/images/cards/house.jpg"},
        {id: 1, title: "드라이브할 때 듣기 좋은 브릿팝", src: "https://cdn.vuetifyjs.com/images/cards/road.jpg"},
      ],

      itemLists: [], // ✅ 2차원 배열 저장
    };
  },
  mounted() {
    this.fetchInitialData();
  },
  computed: {

  },
  methods: {
    async fetchInitialData() {
      try {
        const response = await fetch(`https://winnie-bigquery-api-77vot6b6va-du.a.run.app/custom-collections/user-profile-customs?user_id=${this.store.selectedUserId}`);
        const data = await response.json();

        this.splitSongs(data.data[0].customs)

        // console.log('this.customs', data.data[0].customs)

      } catch (error) {
        console.error('Error fetching data:', error);
        this.itemLists = [];
      }
    },
    splitSongs(allSongs) { // 화면에 맞게 카드당 4곡씩 넣기
      const chunkSize = 2; // ✅ 4개씩 분할
      this.itemLists = [];

      for (let i = 0; i < allSongs.length; i += chunkSize) {
        this.itemLists.push(allSongs.slice(i, i + chunkSize));
      }
    },
  },
};
</script>

