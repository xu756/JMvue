<template>
  <el-container>
    <el-aside width="200px">
      <el-menu default-active="2" class="el-menu-vertical-demo">
        <el-menu-item index="1" @click="routerTo('/index')">
          <i class="el-icon-menu"></i>
          <span slot="title">首页</span>
        </el-menu-item>
        <el-submenu index="1-4">
          <template slot="title">项目列表</template>
          <el-menu-item index="1-4-1" @click="routerTo('/project')">
            <i class="el-icon-menu"></i>我的项目
          </el-menu-item>
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
      <el-header>
        <div></div>
        <div>
          <el-button type="info" @click="loginout">退出按钮</el-button>
        </div>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      name: 544,
    };
  },
  methods: {
    /*退出 */
    loginout() {
      window.sessionStorage.clear();
      this.$http.post("loginout", {
        id: window.sessionStorage.getItem("userID"),
        token: window.sessionStorage.getItem("token"),
      });
      this.$router.push("/login");
    },
    /*子路由*/
    routerTo(path) {
      this.$router.push(path);
    },
    async islogin() {
      var { data: s } = await this.$http.post("islogin", {
        id: window.sessionStorage.getItem("userID"),
        token: window.sessionStorage.getItem("token"),
      });
      if (s.meta.code == 400) {
        this.$message({ message: s.meta.msg, type: "error" });
        this.$router.push("/login");
        clearInterval(this.sh);
      }
    },
  },
  created() {
    setInterval(this.islogin, 10000);
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
