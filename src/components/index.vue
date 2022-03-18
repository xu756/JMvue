<template>
  <div>
    <el-row>
      <el-col class="Data_Size" :span="4" :offset="1">
        <h1>播放量</h1>

        <p>5229</p>
      </el-col>

      <el-col class="Data_Size" :span="4" :offset="2">
        <h1>浏览量</h1>

        <p>5229</p>
      </el-col>

      <el-col class="Data_Size" :span="4" :offset="2">
        <h1>今日访问量</h1>

        <p>5229</p>
      </el-col>

      <el-col class="Data_Size" :span="4" :offset="2">
        <h1>播放量</h1>

        <p>5229</p>
      </el-col>
    </el-row>

    <el-row>
      <el-col class="Data_Map" :span="11">
        <div id="main" style="width: 100%; height: 300px"></div>
      </el-col>

      <el-col class="Data_Map" :span="11" :offset="1">sss</el-col>
    </el-row>
  </div>
</template>
<style lang="scss">
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}

.Data_Size {
  border-radius: 4px;
  text-align: center;
  background-color: azure;
  padding: 20px 0;
  p {
    margin-top: 20px;
    height: 30px;
    &:hover {
      color: rgb(9, 184, 184);
      font-size: 25px;
    }
  }
}

.Data_Map {
  border-radius: 4px;
  background-color: azure;
}
</style>
<script>
export default {
  methods: {
    map_Data() {
      // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById("main"));

      // 指定图表的配置项和数据
      var option = {
        title: {
          text: "今日浏览量",
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        tooltip: {},
        legend: {
          data: ["销量"],
        },
        xAxis: {
          data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        },
        yAxis: {},
        series: [
          {
            name: "销量",
            type: "bar",
            data: [5, 20, 36, 10, 10, 20],
          },
        ],
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    },
  },
  mounted() {
    this.map_Data();
  },
};
</script>
