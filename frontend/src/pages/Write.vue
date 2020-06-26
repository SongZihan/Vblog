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
      input_class: '',
      id: '',
      time: ''
    }
  },
  // 循环保存
  mounted () {
    // 每隔60s自动存储草稿
    this.time = setInterval(this.save, 6000)

    // 检测路由传参
    console.log('====', this.$route.params)
    if (this.$route.params !== '' && this.$route.params.data) {
      this.submit_form.title = this.$route.params.data[1]
      this.submit_form.content = this.$route.params.data[2]
      this.id = this.$route.params.data[0]
    } else if (this.$route.params.title) {
      var find_title = false
      // 到draft_data中寻找重名的文章，如果有则获取那个文章的数据
      for (var i in this.$store.state.draft_data) {
        console.log(this.$store.state.draft_data[i])
        if (this.$store.state.draft_data[i][1] === this.$route.params.title) {
          this.submit_form.title = this.$store.state.draft_data[i][1]
          this.submit_form.content = this.$store.state.draft_data[i][2]
          this.id = this.$store.state.draft_data[i][0]
          find_title = true
          break
        }
      }
      // 如果未找到重名则执行第一次创建草稿程序
      if (find_title !== true) {
        this.submit_form.title = this.$route.params.title
        this.submit_form.content = this.$route.params.content
        this.submit_form.article_type = this.$route.params.article_type
      }
    }
  },
  methods: {
    // 提交草稿
    save (md, html) {
      if (this.submit_form.title === '') {
        this.$notify.error({
          title: '错误',
          message: '请输入标题'
        })
      } else {
        // 判断有无id，这是区分第一次保存和多次保存的依据
        if (this.id === '') {
          // 没有id则表示是第一次保存
          this.$axios({
            method: 'post',
            url: '/api/manage_draft',
            data: {
              title: this.submit_form.title,
              content: this.submit_form.content,
              type: 'add'
            }
          }).then((res) => {
            // 接收返回的id保存到this.id
            if (res.data.code === 200) {
              this.id = res.data.data
              console.log(this.id)
            }
          })
        } else {
          this.$axios({
            method: 'post',
            url: '/api/manage_draft',
            data: {
              title: this.submit_form.title,
              content: this.submit_form.content,
              id: this.id,
              type: 'add'
            }
          })
        }
      }
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
        })
        //   .then((res) => {
        //   // 请求成功返回成功信息
        //   if (res.data.code === 200) {
        //     this.$notify({
        //       title: '成功',
        //       message: res.data.msg,
        //       type: 'success'
        //     })
        //   }
        // })
      }
    }
  },
  beforeDestroy () {
    // 删除定时器
    clearInterval(this.time)
  }

}

</script>
