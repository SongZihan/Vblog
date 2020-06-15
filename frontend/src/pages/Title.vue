<template>
  <div>
    <el-row v-for="(i,index) in my_data.slice(1)" :key="index">
      <el-col >
        <div @click="get_one_page(i[0])">
        <el-card class="box-card" shadow="hover" >
          <div slot="header" class="clearfix">
            <span><h2>{{i[1]}}</h2></span>
<!--            <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>-->
          </div>
          <div class="text item">
            {{'更新时间 ' + i[3]}}--{{'阅读数' + i[4]}}--{{'评论数' + i[5]}}
          </div>
        </el-card>
          </div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import { get_one_page } from '../api/get_data'

export default {
  data () {
    return {}
  },
  computed: {
    // 计算属性实时返回state中的变化
    my_data () {
      // const data = this.$store.state.data[this.$route.params.num]
      // console.log('0+++++', data)
      return this.$store.state.data[this.$route.params.num]
    }
  },
  methods: {
    get_one_page (article_id) {
      console.log('a click')
      get_one_page(this, article_id)
    }
  }

}

</script>

<style>
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
</style>
