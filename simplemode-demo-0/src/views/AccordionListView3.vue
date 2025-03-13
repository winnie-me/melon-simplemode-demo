<template>
  <v-container fluid>
    <v-row no-gutters>
      <!-- 왼쪽 영역 (화면 1 그룹) -->
      <v-col cols="6">
        <v-row>
          <v-col cols="12"><h3>화면 1</h3></v-col>
        </v-row>
        <v-row>
          <v-col cols="12"><h3>화면 1</h3></v-col>
        </v-row>
        <v-row>
          <v-col cols="12"><h3>화면 1</h3></v-col>
        </v-row>
      </v-col>

      <!-- 오른쪽 최상단 영역 (화면 2, 전체 높이 차지) -->
      <v-col cols="6">
        <v-sheet height="100vh" class="d-flex align-center justify-center">
          <h3>화면 2</h3>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
/* 오른쪽 컬럼이 화면 전체 높이를 차지하도록 설정 */
.v-col:nth-child(2) {
  height: 100vh;
}
</style>
