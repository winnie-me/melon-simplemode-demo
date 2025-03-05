<template>
  <v-container class="home">
    <!-- Hero Section -->
    <v-row justify="center">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="font-weight-bold">Welcome to My Vue App</h1>
        <p class="text-subtitle-1">
          This is a simple Vue project template powered by Vuetify. Start building your app with ease!
        </p>
        <v-btn color="primary" class="mt-4" large @click="goToFeatures">
          Get Started
        </v-btn>
      </v-col>
    </v-row>

    <!-- Features Section -->
    <v-row class="mt-8" justify="center">
      <v-col v-for="(feature, index) in features" :key="index" cols="12" sm="6" md="4">
        <v-card class="feature-card">
          <v-card-title class="headline">{{ feature.title }}</v-card-title>
          <v-card-subtitle>{{ feature.subtitle }}</v-card-subtitle>
          <v-card-text>{{ feature.description }}</v-card-text>
          <v-card-actions>
            <v-btn color="primary" text @click="learnMore(feature.link)">Learn More</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      features: [
        {
          title: "Fast & Lightweight",
          subtitle: "Optimized for performance",
          description: "Vue and Vuetify make your app load faster and feel smoother.",
          link: "/performance"
        },
        {
          title: "Responsive Design",
          subtitle: "Mobile-friendly UI",
          description: "Vuetify provides a responsive grid system for all devices.",
          link: "/design"
        },
        {
          title: "Easy to Customize",
          subtitle: "Flexible and modular",
          description: "Modify styles, components, and layouts with ease.",
          link: "/customization"
        }
      ]
    };
  },
  methods: {
    goToFeatures() {
      this.$router.push("/features");
    },
    learnMore(link) {
      this.$router.push(link);
    }
  }
};
</script>

<style scoped>
.home {
  max-width: 800px;
  margin: auto;
  text-align: center;
}
.feature-card {
  transition: transform 0.3s ease-in-out;
}
.feature-card:hover {
  transform: scale(1.05);
}
</style>
