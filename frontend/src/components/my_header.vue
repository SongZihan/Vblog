<template>
  <div class="header_container">
    <el-row :gutter="20">
      <el-col :span="6" :offset="1">
        <h1>宋子寒的个人博客</h1>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="6" :offset="3">
        <h3>QQ:2403353662</h3>
        <h3>Email:s2403353662@gmail.com</h3>
      </el-col>
      <el-col :span="6" :offset="9">
        <slot>
<!--           <el-button type="primary">主要按钮</el-button>-->
        </slot>
      </el-col>
    </el-row>
  </div>

</template>

<script>
export default {
  name: 'my_header',
  data: function () {
    return {}
  }
}
</script>

<style lang="scss" scoped>
  .header_container {
    background-image: url("../../public/header.jpeg");
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;

    h1 {
      margin: 0;
      padding: 0.7em 0 0 0;
    }

    h3 {
      margin: 0;
    }
  }

</style>
