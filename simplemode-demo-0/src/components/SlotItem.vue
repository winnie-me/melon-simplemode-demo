<template>
  <v-card class="pa-4">
    <v-card-title class="white--text text-h6">
      {{ title }}
    </v-card-title>
    <v-card-text>
      <slot/>
    </v-card-text>
  </v-card>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  }
});
</script>
