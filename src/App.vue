<template>
  <div id="app">
    <router-view />
  </div>
</template>
<style lang="scss">
* {
  padding: 0;
  margin: 0;
}

body,
html,
#app {
  width: 100%;
  height: 100%;
  color: #000000;
  font-family: Arial, Helvetica, sans-serif;
}
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
</style>
