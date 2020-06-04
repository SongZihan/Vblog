<template>
  <div id="app">
    <el-container>
      <el-header>
        <my-header></my-header>
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
import { firstGetData } from './api/get_data.js'

export default {
  name: 'app',
  components: {
    'my-header': my_header,
    'my-nav': nav
  },
  created () {
    // 调用api函数，返回接收的数据
    const data = firstGetData()
    // 数据存储到Vuex中
    this.$store.commit('set_data', data)
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
