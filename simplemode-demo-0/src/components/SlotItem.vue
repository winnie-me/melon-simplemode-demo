<template>
  <v-card :elevation="elevation">
    <v-card-title class="white--text text-h6">
      {{ title }}
    </v-card-title>
    <v-card-subtitle>
      <slot name="subtitle"/>
    </v-card-subtitle>
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
  },
  elevation: {
    type: Number,
    // required: true
    default: 1,
  }
});
</script>
