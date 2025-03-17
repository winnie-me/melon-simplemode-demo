<template>
  <v-container>
    <!-- 📌 ApexCharts -->
    <v-card class="pa-3 mb-6">
      <v-card-title>ApexCharts</v-card-title>
      <v-divider></v-divider>
      <v-container>
        <apexchart type="bar" height="300" :options="chartOptions" :series="chartSeries" />
      </v-container>
    </v-card>

    <!-- 📌 Chart.js -->
    <v-card class="pa-3">
      <v-card-title>Chart.js</v-card-title>
      <v-divider></v-divider>
      <v-container>
        <BarChart :chart-data="chartData" :chart-options="chartJsOptions" />
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";
import {defineComponent, ref} from "vue";
// import {Chart as ChartJS, BarElement, CategoryScale, LinearScale, Tooltip, Legend} from "chart.js";
import { Chart as ChartJS, BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from "chart.js";
import {BarChart} from "vue-chart-3";
import { onMounted } from "vue";


// Chart.js 기능 등록
// ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

ChartJS.register(BarController, BarElement, CategoryScale, LinearScale, Tooltip, Legend);

export default defineComponent({
  components: {apexchart: VueApexCharts, BarChart},
  setup() {
    const chartSeries = ref([
      {name: "E (외향)", data: [60, 0, 0, 0]},
      {name: "I (내향)", data: [40, 0, 0, 0]},
      {name: "S (현실형)", data: [0, 55, 0, 0]},
      {name: "N (직관형)", data: [0, 45, 0, 0]},
      {name: "T (사고형)", data: [0, 0, 50, 0]},
      {name: "F (감정형)", data: [0, 0, 50, 0]},
      {name: "J (판단형)", data: [0, 0, 0, 65]},
      {name: "P (인식형)", data: [0, 0, 0, 35]},
    ]);

    const chartOptions = ref({
      chart: {stacked: true, toolbar: {show: false}, stackType: "100%"},
      plotOptions: {bar: {horizontal: true}},
      xaxis: {categories: ["E/I", "S/N", "T/F", "J/P"]},
      colors: ["#FF5733", "#3498DB", "#2ECC71", "#B2A5FF", "#FB9EC6", "#F9CB43", "#FBA518", "#1ABC9C"],
      tooltip: {
        custom: function ({series, seriesIndex, dataPointIndex, w}) {
          const item = w.config.series[seriesIndex];
          const name = item.name;
          const value = item.data[dataPointIndex];

          // ✅ MBTI 설명 추가
          const descriptions = {
            "E (외향)": ["💬 사교적", "🌍 활동적", "📢 표현력 뛰어남"],
            "I (내향)": ["📚 혼자 있는 걸 좋아함", "🧘 조용한 환경 선호", "📝 글로 표현하는 걸 선호"],
            "S (현실형)": ["📊 데이터 중심", "🔎 세부 사항을 신경 씀", "🔗 현실적인 접근 방식"],
            "N (직관형)": ["💡 아이디어 중시", "🌌 큰 그림을 보는 것 선호", "🎭 창의적인 해결책"],
            "T (사고형)": ["⚖️ 논리적 사고", "📌 객관적", "🛠️ 분석적 접근"],
            "F (감정형)": ["❤️ 감정 중시", "🤝 조화를 중요하게 생각함", "💞 사람과의 관계 중시"],
            "J (판단형)": ["📅 계획적", "🏆 목표 설정 중요", "⏳ 일정 엄수"],
            "P (인식형)": ["🎲 즉흥적", "🔀 융통성 있음", "⚡ 변화에 적응 빠름"],
          };

          const descriptionList = descriptions[name] || ["설명 없음"];

          return `
            <div class="tooltip-container">
              <v-card class="pa-3" elevation="4">
                <v-card-title class="text-h6">${name}</v-card-title>
                <v-card-subtitle class="text-blue">${value}%</v-card-subtitle>
                <v-divider></v-divider>
                <v-list dense>
                  ${descriptionList
            .map((desc) => `<v-list-item><v-icon left>mdi-star</v-icon><v-list-item-title>${desc}</v-list-item-title></v-list-item>`)
            .join("")}
                </v-list>
              </v-card>
            </div>
          `;
        },
      },
    });

    const chartData = ref({
      labels: ["E/I", "S/N", "T/F", "J/P"],
      datasets: chartSeries.value.map((item) => ({
        label: item.name,
        data: item.data,
        backgroundColor: chartOptions.value.colors[chartSeries.value.indexOf(item)],
      })),
    });

    const chartJsOptions = ref({
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {display: false},
        tooltip: {
          enabled: true,
          callbacks: {
            title: (tooltipItems) => tooltipItems[0].dataset.label,
            label: (tooltipItem) => `${tooltipItem.raw}%`,
            afterLabel: (tooltipItem) => {
              const descriptions = {
                "E (외향)": ["💬 사교적", "🌍 활동적", "📢 표현력 뛰어남"],
                "I (내향)": ["📚 혼자 있는 걸 좋아함", "🧘 조용한 환경 선호", "📝 글로 표현하는 걸 선호"],
                "S (현실형)": ["📊 데이터 중심", "🔎 세부 사항을 신경 씀", "🔗 현실적인 접근 방식"],
                "N (직관형)": ["💡 아이디어 중시", "🌌 큰 그림을 보는 것 선호", "🎭 창의적인 해결책"],
                "T (사고형)": ["⚖️ 논리적 사고", "📌 객관적", "🛠️ 분석적 접근"],
                "F (감정형)": ["❤️ 감정 중시", "🤝 조화를 중요하게 생각함", "💞 사람과의 관계 중시"],
                "J (판단형)": ["📅 계획적", "🏆 목표 설정 중요", "⏳ 일정 엄수"],
                "P (인식형)": ["🎲 즉흥적", "🔀 융통성 있음", "⚡ 변화에 적응 빠름"],
              };

              return descriptions[tooltipItem.dataset.label] || [];
            },
          },
        },
      },
      scales: {
        x: {stacked: true},
        y: {stacked: true, ticks: {callback: (value) => `${value}%`}},
      },
    });

    return {chartSeries, chartOptions, chartData, chartJsOptions};
  },
});
</script>

<style scoped>
.v-container {
  max-width: 700px;
  margin: auto;
}

.v-card {
  border-radius: 12px;
  background-color: #f9f9f9;
}
</style>
