<template>
  <div>

    <el-row>
      <el-col>
        <el-input placeholder="请输入内容" v-model="submit_form.title">
          <template slot="prepend">标题</template>
        </el-input>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <mavon-editor v-model="submit_form.content" @save="save"/>
      </el-col>
    </el-row>
    <el-divider>文章分类</el-divider>
    <el-row>
      <el-col>
        <el-radio-group v-model="submit_form.article_type">
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
      submit_form: {
        title: '',
        article_type: '',
        content: ''
      },
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
      if (this.submit_form.title === '') {
        this.$notify.error({
          title: '错误',
          message: '请输入标题'
        })
      } else if (this.submit_form.article_type === '') {
        this.$notify.error({
          title: '错误',
          message: '请选择分类'
        })
      } else if (this.submit_form.content === '') {
        this.$notify.error({
          title: '错误',
          message: '请输入内容'
        })
      } else {
        this.$axios({
          method: 'post',
          url: '/api/add_article',
          data: this.submit_form
        }).then(function (res) {
          if (res.data.code === 200) {
            this.$notify({
              title: '成功',
              message: res.data.msg,
              type: 'success'
            })
          }
        })
      }
    }
  }
}

</script>
