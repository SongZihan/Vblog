<template>
  <div>

    <el-row>
      <el-col>
        <el-input placeholder="请输入内容" v-model="title">
      <template slot="prepend">标题</template>
    </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <mavon-editor v-model="value" @save="save"/>
      </el-col>
    </el-row>
        <el-divider>文章分类</el-divider>
    <el-row>
      <el-col>
        <el-radio-group v-model="classify">
      <el-radio :label="item[0]" v-for="(item,index) in this.$store.state.data" :key='index'>{{item[0]}}</el-radio>
      <el-radio :label="input_class">
        <el-input placeholder="请输入内容" v-model="input_class">
          <template slot="prepend">新增分类</template>
        </el-input>
      </el-radio>
    </el-radio-group>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <el-button type="primary" @click="submit_article">提交文章</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'Write',
  data: function () {
    return {
      title: '',
      classify: '',
      value: '',
      input_class: ''
    }
  },
  methods: {
    // 尝试save事件
    save (md, html) {
      console.log(this.value)
      // console.log(this.title)
    },
    // 提交文章
    submit_article () {

    }
  }
}

</script>
