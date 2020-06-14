<!--右上角登录管理菜单-->
<template>
  <div>
    <!--    <el-dropdown split-button type="primary">-->
    <!--      <router-link to="Login">登录</router-link>-->
    <!--      <el-dropdown-menu slot="dropdown" class="dropdwn">-->
    <!--        <el-dropdown-item v-if="!is_login" >-->
    <!--          <router-link to="Login">登录</router-link>-->
    <!--        </el-dropdown-item>-->
    <!--        <el-dropdown-item v-if="!is_login">-->
    <!--          <router-link to="Registered">注册</router-link>-->
    <!--        </el-dropdown-item>-->
    <!--        <el-dropdown-item v-if="is_login" @click="logout">注销</el-dropdown-item>-->
    <!--      </el-dropdown-menu>-->
    <!--    </el-dropdown>-->
    <el-dropdown @command="handleCommand" trigger="click">
  <span class="el-dropdown-link">
    下拉菜单<i class="el-icon-arrow-down el-icon--right"></i>
  </span>
      <el-dropdown-menu slot="dropdown" >
        <el-dropdown-item v-show="!this.$store.state.is_login" command="a" >登录</el-dropdown-item>
        <el-dropdown-item v-show="!this.$store.state.is_login" command="b" >注册</el-dropdown-item>
        <el-dropdown-item v-show="this.$store.state.is_login" command="c" >注销</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
export default {
  name: 'login_logout_registerd',
  data: function () {
    return {
    }
  },
  // computed: {
  //   refresh_my_state () {
  //     console.log(this.$store.state.is_login)
  //     return this.$store.state.is_login
  //   }
  // },
  methods: {
    handleCommand (command) {
      if (command === 'a') {
        this.$router.push('/Login')
      } else if (command === 'b') {
        this.$router.push('/Registered')
      } else {
        // 取消登录
        this.$store.commit('del_token')
        // this.is_login = this.$store.state.is_login
        // console.log(this.is_login)
      }
    }
  }

}
</script>

<style lang="scss">
  .el-dropdown a {
    text-decoration: none;
    color: white;
  }

  .el-dropdown-menu a {
    text-decoration: none;
    color: #606266;
  }
  .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
  }
</style>
