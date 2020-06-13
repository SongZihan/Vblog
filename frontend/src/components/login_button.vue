<!--右上角登录管理菜单-->
<template>
  <div>
    <el-dropdown split-button type="primary">
      <router-link to="Login">登录</router-link>
      <el-dropdown-menu slot="dropdown" class="dropdwn">
        <el-dropdown-item v-if="!is_login" >
          <router-link to="Login">登录</router-link>
        </el-dropdown-item>
        <el-dropdown-item v-if="!is_login">
          <router-link to="Registered">注册</router-link>
        </el-dropdown-item>
        <el-dropdown-item v-if="is_login" @click="logout">注销</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
export default {
  name: 'login_logout_registerd',
  data: function () {
    return {
      is_login: this.$store.state.is_login
    }
  },
  methods: {
    logout: function () {

    }
  }

}
</script>

<style lang="scss">
  .el-dropdown a {
    text-decoration : none;
    color: white;
  }
  .el-dropdown-menu a {
    text-decoration : none;
    color: #606266;
  }
</style>
