<template>
  <div id="app">
    <el-container>
      <el-header>
        <my-header>
          <my-login_logout_registerd></my-login_logout_registerd>
        </my-header>
      </el-header>
      <el-container>
        <el-aside>
        <my-nav></my-nav>
      </el-aside>
      <el-main>
        <router-view/>
      </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// eslint-disable-next-line camelcase
import my_header from './components/my_header'
import nav from './components/nav'
import login_logout_registerd from './components/login_button'
import { firstGetData } from './api/get_data.js'

export default {
  name: 'app',
  components: {
    'my-header': my_header,
    'my-nav': nav,
    'my-login_logout_registerd': login_logout_registerd
  },
  created () {
    // 调用api函数，返回接收的数据
    firstGetData(this)
    // 数据存储到Vuex中
    // this.$store.commit('set_data', data)
    // console.log(data)
  }
}
</script>

<style lang="scss">
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
  body{
  margin:0;
  padding:0;
  }
  .el-container {
  /*设置内部填充为0，几个布局元素之间没有间距*/
  padding: 0;
  /*外部间距也是如此设置*/
  margin: 0;
  /*统一设置高度为100%*/
  height: 100%;

    .el-header{
    background-color: #B3C0D1;
    padding: 0 !important;
    height: 7em !important;
  }
}

</style>
