<template>
  <div>
    <el-row>
      <el-col><h1>{{title}}</h1></el-col>
    </el-row>
    <el-row>
      <el-col>
        <vue-markdown>{{content}}</vue-markdown>
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
import VueMarkdown from 'vue-markdown'

export default {
  name: 'Article',
  data () {
    return {
      all: this.$route.params.data,
      title: this.$route.params.data.data[0][1],
      content: this.$route.params.data.data[0][2],
      update_time: this.$route.params.data.data[0][4],
      comment: this.$route.params.data.data[1]
    }
  },
  components: {
    VueMarkdown
  }
}
</script>

<style scoped>

</style>
