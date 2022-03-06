<template>
  <el-container>
    <el-aside width="200px">
      <el-menu default-active="2" class="el-menu-vertical-demo">
        <el-menu-item index="0">
          <i class="el-icon-menu"></i>
          <span slot="title">首页</span>
        </el-menu-item>
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>数据</span>
          </template>
          <el-submenu index="1-4">
            <template slot="title">数据列表</template>
            <el-menu-item index="1-4-1">
              <i class="el-icon-menu"></i>选项1
            </el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-menu-item index="2">
          <i class="el-icon-menu"></i>
          <span slot="title">项目管理</span>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="el-icon-setting"></i>
          <span slot="title">设置</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header>Header</el-header>
      <el-main>Main</el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>
<style lang="scss">
.el-form-item__content {
  line-height: 0 !important;
}

.iconfont {
  padding-right: 15px;
}

.home-container {
  height: 100%;
}

.double_click {
  /*取消双击*/
  -moz-user-select: none;
  /*火狐*/
  -webkit-user-select: none;
  /*webkit浏览器*/
  -ms-user-select: none;
  /*IE10*/
  -khtml-user-select: none;
  /*早期浏览器*/
  user-select: none;
}

//头部
.el-header {
  background-image: linear-gradient(to left, #fff1eb 0%, #ace0f9 90%);
  display: flex;
  height: 100%;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #fff;

  div {
    display: flex;
    align-items: center;
    margin-left: 15px;
  }
}
//左边背景颜色
.el-aside {
  background-image: linear-gradient(to top, #a8edea 0%, #fed6e3 100%);
  overflow-x: hidden !important;
  width: 100%;
}
.el-container {
  height: 100%;
}
.el-main {
  width: 100%;
  height: 100%;
  position: relative;
  background-image: linear-gradient(120deg, #89f7fe 0%, #66a6ff 100%);
  z-index: 0;

  //不显示滚动条
  &::-webkit-scrollbar {
    width: 0;
  }

  //左下角半圆
  &::before {
    content: "";
    position: fixed;
    bottom: 0;
    left: 200px;
    z-index: -1;
    width: 100%;
    height: 100%;
    background: linear-gradient(#ee9ca7, #ddfde1);
    clip-path: circle(10% at 0 100%);
  }

  //右上角半圆
  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background: linear-gradient(#b29cee, #ddfde1);
    clip-path: circle(10% at right 0);
  }
}
</style>
