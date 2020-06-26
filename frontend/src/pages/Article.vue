<template>
  <div>
    <el-row>
      <el-col><el-button type="danger" icon="el-icon-delete" @click="delete_article" circle></el-button></el-col>
      <el-col><el-button type="primary" icon="el-icon-edit" @click="edit_article" circle></el-button></el-col>
    </el-row>
    <el-row>
      <el-col><h1>{{title}}</h1></el-col>
    </el-row>
    <el-row>
      <el-col>
        <mavon-editor v-model="content" v-bind="option"/>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <div v-for="(i,index) in comment" :key="index">
      <el-row>
        <el-col>
          {{'nickname:' + i[2]}}
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          {{'content:' + i[1]}}
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          {{'upload time::' + i[3]}}
        </el-col>
      </el-row>
    </div>

  </div>
</template>

<script>
// import VueMarkdown from 'vue-markdown'
import { firstGetData } from '../api/get_data'

export default {
  name: 'Article',
  data () {
    return {
      all: this.$route.params.data,
      id: this.$route.params.data.data[0][0],
      title: this.$route.params.data.data[0][1],
      content: this.$route.params.data.data[0][2],
      update_time: this.$route.params.data.data[0][3],
      comment: this.$route.params.data.data[1],
      option: {
        toolbarsFlag: false, subfield: false, defaultOpen: 'preview'
      }
    }
  },
  methods: {
    delete_article () {
      this.$axios({
        method: 'post',
        url: '/api/delete_article',
        data: { title: this.title }
      }).then(
        (res) => {
          if (res.data.code === 200) {
            // 删除成功返回上一步路由并重载数据
            firstGetData(this)
            this.$router.go(-1)
            // this.$router.push('/')
          }
        }
      )
    },
    edit_article () {
      this.$router.push({
        name: 'Write',
        params: {
          title: this.title,
          content: this.content,
          article_type: this.$route.params.data.data[0][3]
        }
      })
    }
  }
  // components: {
  //   VueMarkdown
  // }
}
</script>

<style>
</style>
