<template>
  <div id="LoginBody">
    <div id="LoginBox">
      <div id="LoginBoxlogo">
        <img src="../assets/logo.png" />
      </div>
      <el-form
        ref="LoginFormref"
        :model="LoginFrom"
        class="login_form"
        :rules="LoginForm_rules"
      >
        <el-form-item prop="username">
          <el-input
            v-model="LoginFrom.username"
            prefix-icon="iconfont icon-yonghu1"
            placeholder="用户名"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            v-model="LoginFrom.password"
            prefix-icon="iconfont icon-mima"
            placeholder="密码"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <v-sidentify @GetYzm="GetYzm" ref="ReGetYzm"></v-sidentify>
          <el-input
            class="YzmBox"
            v-model="yzm"
            placeholder="验证码"
          ></el-input>
        </el-form-item>
        <el-form-item class="login_form_button">
          <el-button type="success" @click="LoginSubmit()">登录</el-button>
          <el-button type="info" @click="Login_Ref()">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
import Sidentify from "../components/identify.vue";
export default {
  name: "login",
  data() {
    return {
      //登录信息
      LoginFrom: {
        username: "admin",
        password: "123456",
      },
      //表单验证
      LoginForm_rules: {
        username: [
          { required: true, message: "请输入登录名称", trigger: "change" },
          {
            min: 3,
            max: 10,
            message: "长度在 3 到 10 个字符",
            trigger: "change",
          },
        ],
        password: [
          { required: true, message: "请输入登录密码", trigger: "change" },
          {
            min: 6,
            max: 15,
            message: "长度在 6 到 15 个字符",
            trigger: "change",
          },
        ],
      },
      //验证码
      Yzm: "",
      //输入的验证码
      yzm: "",
    };
  },
  methods: {
    //登录按钮
    LoginSubmit() {
      this.$refs.LoginFormref.validate(async (valid) => {
        //获取表单验证结果
        this.yzm = this.Yzm; //登录不用验证码
        if (valid && this.yzm == this.Yzm) {
          const { data: res } = await this.$http.post("login", this.LoginFrom);
          console.log(res);
          if (res.meta.code !== 200) {
            this.$message(res.meta.msg);
          } else {
            this.$message({ message: res.meta.msg, type: "success" });
            window.sessionStorage.setItem("token", res.data.token);
            window.sessionStorage.setItem("userID", res.data.id);
            this.$router.push("/");
          }
        } else {
          this.$message.error("请重新输入登录信息");
          this.yzm = "";
          this.Login_Ref();
          this.ReGetYzm();
        }
      });
    },
    //重置表单
    Login_Ref() {
      this.$refs.LoginFormref.resetFields();
    },
    //接收验证码
    GetYzm(data) {
      this.Yzm = data;
    },
    //重新获取验证码
    ReGetYzm() {
      this.$refs.ReGetYzm.CreatYzm();
    },
  },
  components: {
    "v-sidentify": Sidentify,
  },
};
</script>
<style lang="scss">
#LoginBody {
  width: 100%;
  height: 100%;
  background: url(../assets/bg.jpg) center center no-repeat;
  background-size: 100% 100%;

  #LoginBox {
    width: 340px;
    height: 300px;
    padding: 30px;
    border-radius: 15px;
    position: absolute;
    top: calc(50% - 160px);
    left: calc(50% - 200px);
    background-color: rgba(240, 248, 255, 0.9);

    #LoginBoxlogo {
      width: 100px;
      height: 100px;
      border: 1px solid #eee;
      border-radius: 50%;
      padding: 10px;
      position: absolute;
      left: 50%;
      transform: translate(-50%, calc(-50% - 30px));
      background-color: #fff;

      img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background-color: #eee;
      }
    }

    .login_form {
      position: absolute;
      bottom: 30px;
      width: 340px;
      padding: 0 20px;
      box-sizing: border-box;
    }

    .login_form_button {
      text-align: right;
    }

    .YzmBox {
      width: 120px;
      float: right;
    }
  }
}
</style>