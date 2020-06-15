<!--导航栏,导航栏中只加载分栏信息-->
<template>
  <el-row class="tac" justify="center">
    <el-col :span="24">
      <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
        <el-radio-button :label="false">展开</el-radio-button>
        <el-radio-button :label="true">收起</el-radio-button>
      </el-radio-group>
      <el-menu
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        :collapse="isCollapse"
      active-text-color="#409EFF"
      text-color="#303133">
        <el-menu-item v-for="(item,index) in this.$store.state.data" :key="index" :index="index" @click="to_path(index)">
          <i class="el-icon-menu"></i>
          <span slot="title">{{item[0]}}</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'nav',
  data () {
    return {
      // items: this.$store.state.data
      isCollapse: true
    }
  },
  methods: {
    to_path (index) {
      console.log('=====')
      this.$router.push('/classify/' + index + '')
    }
  }
}
</script>

<style>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
</style>
