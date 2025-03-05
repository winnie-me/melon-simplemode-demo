<template>
  <v-app>
    <v-container>
      <h2 class="mb-4">순서를 변경할 수 있는 리스트</h2>

      <!-- ✅ 드래그 가능한 리스트 -->
      <draggable v-model="items" item-key="id" animation="200" class="drag-area" ghost-class="ghost">
        <template #item="{ element, index }">
          <v-list-item>
            <template v-slot:prepend>
              <v-avatar rounded="lg" size="48">
                <img :src="element.thumbnail" class="avatar-img" />
              </v-avatar>
            </template>

            <v-list-item-title>{{ element.title }}</v-list-item-title>
            <v-list-item-subtitle>{{ element.artist }}</v-list-item-subtitle>

            <template v-slot:append>
              <v-icon>mdi-drag</v-icon> <!-- 드래그 아이콘 -->
            </template>
          </v-list-item>
        </template>
      </draggable>
    </v-container>
  </v-app>
</template>

<script>
import draggable from 'vuedraggable';

export default {
  components: { draggable },
  data() {
    return {
      items: [
        { id: 1, title: 'Song 1', artist: 'Artist 1', thumbnail: 'https://via.placeholder.com/50' },
        { id: 2, title: 'Song 2', artist: 'Artist 2', thumbnail: 'https://via.placeholder.com/50' },
        { id: 3, title: 'Song 3', artist: 'Artist 3', thumbnail: 'https://via.placeholder.com/50' },
      ],
    };
  }
};
</script>

<style>
/* 드래그 중인 아이템 스타일 */
.ghost {
  opacity: 0.5;
  background: #ddd;
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.drag-area {
  background: white;
  padding: 10px;
  border-radius: 8px;
}
</style>
