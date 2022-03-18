<template>
  <el-card>
    <el-form label-width="80px" :inline="true">
      <el-form-item label="项目名">
        <el-input v-model="Active_Data.ProjectName"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="New_Project()">创建</el-button>
      </el-form-item>
    </el-form>
    <el-table :data="tableData" stripe style="width: 100%" v-loading="loading">
      <el-table-column type="index" align="center" label="索引" width="100"></el-table-column>
      <el-table-column label="项目名" prop="ProjectName" width="300"></el-table-column>
      <el-table-column label="创建时间" prop="CreatTime" width="300"></el-table-column>
      <el-table-column label="最后一次修改时间"  prop="LoginTime" width="300"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" type="primary" @click="View_col(scope.row)">查看</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="current_page"
      :page-sizes="[5, 10, 20]"
      :page-size="Page_Size"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total"
    ></el-pagination>
  </el-card>
</template>

<script>
export default {
  data() {
    return {
      //获取数据
      tableData: [],
      //加载
      loading: true,
      // 总数据
      total: 10,
      //对话框是否显示
      dialogVisible: false,
      //新建，编辑，删除数据
      Active_Data: {},
      // 每页多少条数据
      Page_Size: 10,
      // 当前页数
      current_page: 1,
    };
  },
  methods: {
    //获取数据
    async Get_Data() {
      const { data: res } = await this.$http.post("GetProjectList", {
        Page_Size: this.Page_Size,
        current_page: this.current_page,
        total: this.total,
        token: window.sessionStorage.getItem("token"),
        userID: window.sessionStorage.getItem("userID"),
      });

      // 对时间格式化
      for (let i = 0; i < res.data.length; i++) {
        // 创建时间格式化
        var CreatTime = new Date(res.data[i].CreatTime);
        res.data[i].CreatTime = CreatTime.toLocaleString();
        // 保存时间格式化
        var time = new Date(res.data[i].LoginTime);
        res.data[i].LoginTime = time.toLocaleString();
      }
      this.tableData = res.data;
      this.total = res.total;

      //加载状况
      this.loading = res.meta.code == 200 ? false : true;
    },

    //删除
    async handleDelete(row) {
      const { data: res } = await this.$http.post("DeleteProject", {
        id: row.id,
        token: window.sessionStorage.getItem("token"),
        userID: window.sessionStorage.getItem("userID"),
      });
      //消息确认
      this.$message({
        message: res.meta.msg,
        type: res.meta.code == 200 ? "success" : "error",
      });
      //刷新数据
      this.Get_Data();
    },
    //创建项目
    async New_Project() {
      const { data: res } = await this.$http.post("Create_Project", {
        New_Project: this.Active_Data.ProjectName,
        token: window.sessionStorage.getItem("token"),
        userID: window.sessionStorage.getItem("userID"),
      });
      //消息确认
      this.$message({
        message: res.meta.msg,
        type: res.meta.code == 200 ? "success" : "error",
      });
      //刷新数据
      this.Get_Data();
      this.Active_Data = {};
    },
    // 每页数量改变
    handleSizeChange(val) {
      this.Page_Size = val;
      this.Get_Data();
    },
    // 当前页数改变
    handleCurrentChange(val) {
      this.current_page = val;
      this.Get_Data();
    },
    //查看数据  跳转
    View_col(val) {
      this.$router.push("/project/id=" + val.id)
    }
  },
  mounted() {
    this.Get_Data();
    //var a = JSON.stringify(this.tableData); //对象转json
    // console.log(a);
    // var b = JSON.parse(a); //json转对象
    //console.log(b);
  },
};
</script>
