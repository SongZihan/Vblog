<!--导航栏,导航栏中只加载分栏信息-->
<template>
  <el-row class="tac" justify="center">
    <el-col :span="24" >
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item v-for="(item,index) in items" :key="index">
        <i class="el-icon-menu"></i>
        <span slot="title">{{item.title}}</span>
      </el-menu-item>
    </el-menu>
  </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'nav',
  data: function () {
    return {
      items: this.$store.state.data
    }
  }
}
</script>
